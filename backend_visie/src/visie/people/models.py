import datetime

from visie.infrastructure.database.models_base.base import Base
from sqlalchemy import Column, Integer, String, Date


class People(Base):
    __tablename__ = 'pessoas'

    id_pessoa = Column(Integer, primary_key=True)
    nome = Column(String(100))
    rg = Column(String(15))
    cpf = Column(String(15), unique=True)
    data_nascimento = Column(Date)
    data_admissao = Column(Date, default=datetime.date.today())
    funcao = Column(String)

