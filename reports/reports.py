from sqlalchemy.orm import Session
from models.models import Produto, Movimentacao
from datetime import datetime

def relatorio_estoque_baixo(db: Session, threshold: int):
    return db.query(Produto).filter(Produto.quantidade_inicial < threshold).all()

def relatorio_excesso_estoque(db: Session, threshold: int):
    return db.query(Produto).filter(Produto.quantidade_inicial > threshold).all()

def relatorio_movimentacao(db: Session, start_date: datetime, end_date: datetime):
    return db.query(Movimentacao).filter(Movimentacao.data_operacao >= start_date, 
                                         Movimentacao.data_operacao <= end_date).all()
