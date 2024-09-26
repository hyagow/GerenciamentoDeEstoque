import uvicorn
from descricao import descricao
from fastapi import FastAPI
from routers import routers
from db.database import engine
from db.database import Base

# instanciando api
app = FastAPI(title='Sistema Gerenciador de Estoque', description=descricao)

app.include_router(routers.routers)

# Inicializa o banco de dados
Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
  uvicorn.run(app, host='127.0.0.1', port=8080)