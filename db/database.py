from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "mysql+mysqlclient://root:123123123@localhost/my_database"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base: DeclarativeMeta = declarative_base()


my_database = [
  {'id':1, 'nome':'produto1', 'categoria': 'cat1', 'qnt_estoque': 10, 'preco':19238.12},
  {'id':2, 'nome':'produto2', 'categoria': 'cat2', 'qnt_estoque': 20, 'preco':238.10},
]
