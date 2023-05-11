import sqlalchemy
import pymysql
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

pymysql.install_as_MySQLdb()

engine = sqlalchemy.create_engine("mysql://CAUA:SQL538@localhost/BD")

Base = sqlalchemy.ext.declarative.declarative_base()

class Amazon(Base):
    __tablename__ = "produtos_de_cozinha"
    id = Column(Integer,primary_key=True,autoincrement=True) 
    titulo = Column(String(300))
    preco = Column(String(20))

Base.metadata.create_all(engine)

TheSession = sessionmaker(bind=engine)
session = TheSession()