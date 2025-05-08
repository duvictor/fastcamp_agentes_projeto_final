"""
responsavel por manter as funcionalidades essenciais para o aplicativo
Paulo Victor Dos Santos 2025
Universidade Federal de Goiás
"""

import re
import uuid

from crewai import Agent, Task
# from langchain.document_loaders import PyPDFLoader
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
from data.Protocolo import LaudoPDF
import uuid
from transformers import AutoTokenizer, AutoModel
from src.Agentes import AgenteLaudoMedico
from src.QdrantConection import upsert_to_qdrant


class Embedder:
    """
    Provides functionality to generate embeddings for given text using a
    pre-trained SentenceTransformer model.

    This class leverages the 'sentence-transformers/all-MiniLM-L6-v2' pre-trained
    model to encode text into embeddings. It also uses a text splitter to divide
    text into manageable chunks for processing.

    :ivar model: The pre-trained SentenceTransformer model used for generating embeddings.
    :type model: SentenceTransformer
    """
    def __init__(self):
        """
        Represents a class that initializes a tokenizer and a sentence transformer model
        for natural language processing tasks.

        Attributes
        ----------
        tokenizer : AutoTokenizer
            The tokenizer from the `sentence-transformers/all-MiniLM-L6-v2` model.
        model : SentenceTransformer
            The sentence transformer model from `sentence-transformers/all-MiniLM-L6-v2`.

        Methods
        -------
        This class does not define any methods explicitly, but it initializes two
        key components, tokenizer and model, used for text encoding and transformation.
        """
        self.tokenizer = AutoTokenizer.from_pretrained('sentence-transformers/all-MiniLM-L6-v2')
        self.model = AutoModel.from_pretrained('sentence-transformers/all-MiniLM-L6-v2')


    # def custom_embeddings(self, text: str) -> list[float]:
    #     # Tokenize and get model outputs
    #     inputs = self.tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    #     outputs = self.model(**inputs)
    #
    #     # Use mean pooling to get text embedding
    #     embeddings = outputs.last_hidden_state.mean(dim=1)
    #
    #     # Convert to list of floats and return
    #     return embeddings[0].tolist()

    def generate_embeddings(self, sentences: str) -> list[float]:
        # Tokenize and get model outputs
        inputs = self.tokenizer(sentences, return_tensors="pt", padding=True, truncation=True)
        outputs = self.model(**inputs)

        # Use mean pooling to get text embedding
        embeddings = outputs.last_hidden_state.mean(dim=1)

        # Convert to list of floats and return
        return embeddings[0].tolist()

    def generate_split_sentences(self, sentences):
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=220)
        split_sentences = text_splitter.split_text(sentences)
        return split_sentences




class PdfUtil:
    """
    Utility class for handling PDF-related operations.

    This class is used to perform operations such as extracting content
    from PDF files. It provides methods to simplify the process of
    working with PDF documents, particularly for reading and parsing purposes.
    """
    def __init__(self):
        """
        This class implements the initialization of the base class through its constructor,
        ensuring that the parent class is set up properly. It does not contain additional
        attributes or methods. The primary purpose is to extend functionality from the base
        class through inheritance.

        Attributes:
            None

        """
        super().__init__()


    def extract_page_content(self, pdf_path):
        """
        Extracts the content from all pages of the given PDF file.

        The method utilizes the PyPDFLoader library to read and process the
        provided PDF file path and returns the content contained within the
        PDF. Each page's content is extracted and returned as documents.

        :param pdf_path: The file path to the target PDF file whose content is to
            be extracted.
        :type pdf_path: str
        :return: A list of documents containing the extracted content from the
            PDF file.
        :rtype: list
        """
        loader = PyPDFLoader(pdf_path)
        docs = loader.load()
        return docs



class TextUtil:
    """
    Provides functionality to process PDF files, extract their content, and generate embeddings
    for further processing and storage. The `TextUtil` class integrates several utilities and
    components, including PDF content extraction, embedding generation, and medical report
    processing.

    Detailed description:
    - Extracts textual content from PDF files using `PdfUtil`.
    - Generates embeddings for split sentences in the text using `Embedder`.
    - Utilizes a medical report agent, `AgenteLaudoMedico`, to process the report and determine
      its specialty and modality.
    - Upserts the processed report data, including the embeddings, text, and metadata, into storage
      via `upsert_to_qdrant`.

    :ivar pdfUtil: Utility to extract content from PDF files.
    :type pdfUtil: PdfUtil
    :ivar embeddingUtil: Utility to generate embeddings for textual content.
    :type embeddingUtil: Embedder
    :ivar agentes: Agent responsible for processing medical reports.
    :type agentes: AgenteLaudoMedico
    """
    def __init__(self):
        """
        Initializes the class with instances of PdfUtil, Embedder, and AgenteLaudoMedico.

        Attributes
        ----------
        pdfUtil : PdfUtil
            Instance of PdfUtil used for handling PDF-related operations.
        embeddingUtil : Embedder
            Instance of Embedder used for text embedding operations.
        agentes : AgenteLaudoMedico
            Instance of AgenteLaudoMedico for managing medical report agents.
        """
        self.pdfUtil = PdfUtil()
        self.embeddingUtil = Embedder()
        self.agentes = AgenteLaudoMedico()

    def process_pdf(self, temp_file, file_name):
        """
        Processes a PDF file by extracting its content, generating embeddings, and organizing
        the data into a structured format.

        This function leverages utility methods to extract page content from a given PDF file,
        generate embeddings for the content, and organize the results in a structured dictionary.
        The information is then processed and enriched with additional attributes before being
        stored in a targeted system.

        :param temp_file: Temporary file representing the source PDF.
        :type temp_file: TemporaryFile
        :param file_name: Name of the PDF file.
        :type file_name: str
        :return: None
        """
        docs = self.pdfUtil.extract_page_content(temp_file)
        for doc in docs:
            textos = doc.page_content

            especialidade, modalidade, resumo = self.agentes.processar_laudo(textos)

            split_sentences = self.embeddingUtil.generate_split_sentences(doc.page_content)

            for split_local in split_sentences:

                embeddings = self.embeddingUtil.generate_embeddings(split_local)

                protocol_data = {"id": uuid.uuid4(),
                                 "name": file_name,
                                 "embedding": embeddings,
                                 "texto": split_local,
                                 "page_content": textos,
                                 }

                laudoPDF = LaudoPDF(**protocol_data)

                laudoPDF.especialidade = especialidade
                laudoPDF.modalidade = modalidade
                laudoPDF.sumarizacao = resumo
                upsert_to_qdrant(laudoPDF)
            # closeQdrant()


