from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ProdutoBase(BaseModel):
    codigo: str
    nome: str
    descricao: Optional[str] = None
    categoria: Optional[str] = None
    preco: float
    quantidade_inicial: int
    localizacao: Optional[str] = None

class ProdutoCreate(ProdutoBase):
    pass

