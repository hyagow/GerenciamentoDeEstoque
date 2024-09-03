from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from db.database import SessionLocal
from schemas.schemas import Produto, Movimentacao, Localizacao, ProdutoCreate, MovimentacaoCreate, LocalizacaoCreate
from crud.crud import create_products, get_product, create_movimentation, create_localization, get_relatory_inventory


routers = APIRouter(tags=['Funções de Gerenciamento'])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@routers.post("/produtos/", response_model=Produto)
def criar_produto(produto: ProdutoCreate, db: Session = Depends(get_db)):
    return create_products(db=db, produto=produto)

@routers.get("/produtos/", response_model=list[Produto])
def listar_produtos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_product(db=db, skip=skip, limit=limit)

@routers.post("/movimentacoes/", response_model=Movimentacao)
def criar_movimentacao(movimentacao: MovimentacaoCreate, db: Session = Depends(get_db)):
    return create_movimentation(db=db, movimentacao=movimentacao)

@routers.post("/localizacoes/", response_model=Localizacao)
def criar_localizacao(localizacao: LocalizacaoCreate, db: Session = Depends(get_db)):
    return create_localization(db=db, localizacao=localizacao)

