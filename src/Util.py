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

    def __init__(self):
        self.model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

    def generate_embeddings(self, setences):
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=220)
        split_setences = text_splitter.split_text(setences)
        return split_setences, self.model.encode(split_setences)




class PdfUtil:

    def __init__(self):
        super().__init__()


    def extract_page_content(self, pdf_path):
        loader = PyPDFLoader(pdf_path)
        docs = loader.load()
        return docs



class TextUtil:

    def __init__(self):
        self.pdfUtil = PdfUtil()
        self.embeddingUtil = Embedder()
        self.agentes = AgenteLaudoMedico()

    def process_pdf(self, temp_file, file_name):

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
            especialidade, modalidade = self.agentes.processar_laudo(laudoPDF)
            laudoPDF.especialidade = especialidade
            laudoPDF.modalidade = modalidade
            upsert_to_qdrant(laudoPDF)


