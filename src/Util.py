"""
responsavel por manter as funcionalidades essenciais para o aplicativo
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
        This class initializes an instance of a SentenceTransformer-based model
        for generating embeddings efficiently. Specifically, it uses the
        'all-MiniLM-L6-v2' pre-trained model from SentenceTransformers.

        Attributes
        ----------
        model : SentenceTransformer
            The sentence transformer instance initialized with the
            'sentence-transformers/all-MiniLM-L6-v2' model to generate
            sentence embeddings.
        """
        self.model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

    def generate_embeddings(self, setences):
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=220)
        split_setences = text_splitter.split_text(setences)
        return split_setences, self.model.encode(split_setences)




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
            split_setences, embeddings = self.embeddingUtil.generate_embeddings(doc.page_content)

            protocol_data = {"id": uuid.uuid4(),
                             "name": file_name,
                             "embedding": embeddings.tolist(),
                             "textos": split_setences,
                             "texto": textos,
                             }

            laudoPDF = LaudoPDF(**protocol_data)
            especialidade, modalidade, resumo = self.agentes.processar_laudo(laudoPDF)
            laudoPDF.especialidade = especialidade
            laudoPDF.modalidade = modalidade
            laudoPDF.sumarizacao = resumo
            upsert_to_qdrant(laudoPDF)


