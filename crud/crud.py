from sqlalchemy.orm import Session
from schemas.schemas import ProdutoCreate, MovimentacaoCreate, LocalizacaoCreate
from models.models import Produto, Movimentacao, Localizacao

def create_product(db: Session, produto: ProdutoCreate):
    db_produto = Produto(**produto.dict())
    db.add(db_produto)
    db.commit()
    db.refresh(db_produto)
    return db_produto

def get_products(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Produto).offset(skip).limit(limit).all()

def create_movimentation(db: Session, movimentacao: MovimentacaoCreate):
    db_movimentacao = Movimentacao(**movimentacao.dict())
    db.add(db_movimentacao)
    db.commit()
    db.refresh(db_movimentacao)
    return db_movimentacao

def create_localization(db: Session, localizacao: LocalizacaoCreate):
    db_localizacao = Localizacao(**localizacao.dict())
    db.add(db_localizacao)
    db.commit()
    db.refresh(db_localizacao)
    return db_localizacao

