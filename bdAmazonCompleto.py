import pymysql
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

pymysql.install_as_MySQLdb()

engine = sqlalchemy.create_engine("mysql://CAUA:SQL538@localhost/BD")

Base = sqlalchemy.ext.declarative.declarative_base()

class Amazon(Base):
    __tablename__ = "produtos de cozinha mapeados"
    ID = Column(Integer, primary_key=True, autoincrement=True)
    Produto = Column(String(300))
    Valor = Column(String(300))
    Marca = Column(String(100))
    MaterialOuCor = Column(String(100))

Base.metadata.create_all(engine)

TheSession = sessionmaker(bind=engine)
session = TheSession()