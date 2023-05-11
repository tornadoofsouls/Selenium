import pymysql
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

pymysql.install_as_MySQLdb()

engine = sqlalchemy.create_engine("mysql://CAUA:SQL538@localhost/BD")

Base = sqlalchemy.ext.declarative.declarative_base()

class Amazon(Base):
    __tablename__ = "CotacaoDolar"
    id = Column(Integer,primary_key=True,autoincrement=True) 
    Data = Column(String(10))
    Valor = Column(String(10))

Base.metadata.create_all(engine)

TheSession = sessionmaker(bind=engine)
session = TheSession()