import pymysql
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

pymysql.install_as_MySQLdb()

engine = sqlalchemy.create_engine("mysql://CAUA:SQL538@localhost/BD")

Base = sqlalchemy.ext.declarative.declarative_base()

class CSV(Base):
    __tablename__ = "ler_csv"
    id = Column(Integer,primary_key=True,autoincrement=True)
    Nome = Column(String(30))
    Sobrenome = Column(String(30))
    Email = Column(String(90))
    Email2 = Column(String(90))
    Profissao = Column(String(60)) 

Base.metadata.create_all(engine)

TheSession = sessionmaker(bind=engine)
session = TheSession()