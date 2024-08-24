from sqlalchemy.orm import Session
from schemas.schemas import ProdutoCreate, MovimentacaoCreate, LocalizacaoCreate
from models.models import Produto, Movimentacao, Localizacao

def create_product(db: Session, produto: ProdutoCreate):
    db_produto = Produto(**produto.dict())
    db.add(db_produto)
    db.commit()
    db.refresh(db_produto)
    return db_produto

