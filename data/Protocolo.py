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