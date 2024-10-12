from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Classe que possui o modelo dos Produtos
class ProdutoBase(BaseModel):
    codigo: str
    nome: str
    descricao: Optional[str] = None
    categoria: Optional[str] = None
    preco: float
    quantidade_inicial: int
    localizacao: Optional[str] = None

# Classe somente para uso especifico (criação)
class ProdutoCreate(ProdutoBase):
    pass

# Classe para identificação do produto.
class Produto(ProdutoBase):
    id: int

    class Config:
        orm_mode = True

# Classe para o modelo das movimentações.
class MovimentacaoBase(BaseModel):
    produto_id: int
    quantidade: int
    tipo_operacao: str
    motivo: Optional[str] = None

# Classe para a criação de movimentos.
class MovimentacaoCreate(MovimentacaoBase):
    pass

# Classe para a movimentação.
class Movimentacao(MovimentacaoBase):
    id: int
    data_operacao: datetime

    class Config:
        orm_mode = True
        
# Classe para a base da localização.
class LocalizacaoBase(BaseModel):
    produto_id: int
    localizacao_atual: str

# Classe para a base de Criação da Localização
class LocalizacaoCreate(LocalizacaoBase):
    pass

# Classe para a localização.
class Localizacao(LocalizacaoBase):
    id: int
    data_atualizacao: datetime

    class Config:
        orm_mode = True