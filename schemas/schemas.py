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

class Produto(ProdutoBase):
    id: int

    class Config:
        orm_mode = True

class MovimentacaoBase(BaseModel):
    produto_id: int
    quantidade: int
    tipo_operacao: str
    motivo: Optional[str] = None

class MovimentacaoCreate(MovimentacaoBase):
    pass

class Movimentacao(MovimentacaoBase):
    id: int
    data_operacao: datetime

    class Config:
        orm_mode = True

class LocalizacaoBase(BaseModel):
    produto_id: int
    localizacao_atual: str

class LocalizacaoCreate(LocalizacaoBase):
    pass

class Localizacao(LocalizacaoBase):
    id: int
    data_atualizacao: datetime

    class Config:
        orm_mode = True