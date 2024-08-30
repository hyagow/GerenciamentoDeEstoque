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
