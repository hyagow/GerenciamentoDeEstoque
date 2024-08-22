from fastapi import APIRouter, HTTPException, status
from models.models import ProductModelRequest,ProductModelResponse
from db.database import my_database
from sqlalchemy.orm import Session
from db.database import SessionLocal
from typing import List


routers = APIRouter(tags=['Funções de Gerenciamento'])

