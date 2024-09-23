from sqlalchemy.orm import Session
from models.models import Produto, Movimentacao
from datetime import datetime

def relatorio_estoque_baixo(db: Session, threshold: int):
    return db.query(Produto).filter(Produto.quantidade_inicial < threshold).all()
