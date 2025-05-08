"""
responsavel por manter todos os modelos que serão utilizados nos protocolos
"""
from dataclasses import Field
from typing import List, Optional
from uuid import UUID, uuid4

from pydantic import BaseModel
from pydantic import AnyUrl



# @dataclass
class LaudoPDF(BaseModel):
    """
    Represents the LaudoPDF model used for handling and encapsulating the details
    of a PDF document in the context of a system dealing with reports or
    medical summaries.

    This class is designed to serve as a structured way to handle and process
    the information contained in a PDF. It provides attributes for capturing
    essential details like name, main text, specialized field, modality,
    summarized content, embeddings, and more.

    :ivar id: Unique identifier for the LaudoPDF instance.
    :type id: UUID
    :ivar name: Name or title of the PDF document.
    :type name: str
    :ivar texto: The primary text content of the PDF.
    :type texto: str
    :ivar especialidade: The specialized field related to the PDF document.
    :type especialidade: Optional[str]
    :ivar modalidade: Modality associated with the PDF document.
    :type modalidade: Optional[str]
    :ivar textos: List of extracted strings or blocks of texts from the PDF.
    :type textos: List[str]
    :ivar sumarizacao: Optional summarized version of the main text.
    :type sumarizacao: Optional[str]
    :ivar embedding: Embedding vectors associated with the document content.
    :type embedding: List
    """
    id: UUID
    name: str
    texto: str
    especialidade: Optional[str] = None
    modalidade: Optional[str] = None
    textos: List[str]
    sumarizacao: Optional[str] = None
    embedding: List

    # palavra_chaves: List[str]
    # modalidade:str
    # especialidade:str