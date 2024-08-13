from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Float

class ProductModelResponse(BaseModel):
  id = Column(Integer, primary_key=True, index=True)
  nome = Column(String, index=True)
  categoria = Column(String, index=True)
  qnt_estoque = Column(Integer, index=True)
  preco = Column(Float, index=True)
  loc_deposito = Column(String, index=True)
