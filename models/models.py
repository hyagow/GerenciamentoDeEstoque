from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Text, Enum, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
# from db.database import Base
import enum

class TipoOperacao(enum.Enum):
    entrada = "entrada"
    saida = "saida"

class Produto(BaseModel):
    __tablename__ = "produtos"
    
    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String, unique=True, index=True)
    nome = Column(String)
    descricao = Column(Text, nullable=True)
    categoria = Column(String, nullable=True)
    preco = Column(Integer)
    quantidade_inicial = Column(Integer)
    localizacao = Column(String, nullable=True)
    movimentacoes = relationship("Movimentacao", back_populates="produto")
    localizacoes = relationship("Localizacao", back_populates="produto")

class Movimentacao(BaseModel):
    __tablename__ = "movimentacoes"
    
    id = Column(Integer, primary_key=True, index=True)
    produto_id = Column(Integer, ForeignKey("produtos.id"))
    quantidade = Column(Integer)
    tipo_operacao = Column(Enum((TipoOperacao)))
    data_operacao = Column(DateTime(timezone=True), server_default=func.now())
    motivo = Column(Text, nullable=True)
    
    produto = relationship("Produto", back_populates="movimentacoes")

class Localizacao(BaseModel):
    __tablename__ = "localizacoes"
    
    id = Column(Integer, primary_key=True, index=True)
    produto_id = Column(Integer, ForeignKey("produtos.id"))
    localizacao_atual = Column(String)
    data_atualizacao = Column(DateTime(timezone=True), server_default=func.now())
    
    produto = relationship("Produto", back_populates="localizacoes")
