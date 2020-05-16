from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Total(Base):
    __tablename__ = 'total_number'
    __table_args__ = {'mysql_charset': 'utf8'}

    total = Column(String(5), nullable=False, primary_key=True)


class NumberOfRequests(Base):
    __tablename__ = 'number_of_requests'
    __table_args__ = {'mysql_charset': 'utf8'}

    type = Column(String(5), nullable=False, primary_key=True)
    number = Column(String(5), nullable=False)


class Top1(Base):
    __tablename__ = 'top10_by_size'
    __table_args__ = {'mysql_charset': 'utf8'}

    Number = Column(Integer, nullable=False, primary_key=True)
    URL = Column(String(20), nullable=False)
    Code = Column(String(3), nullable=False)
    Size = Column(String(10), nullable=False)
    Count = Column(String(5), nullable=False)


class Top2(Base):
    __tablename__ = 'top10_by_client_error'
    __table_args__ = {'mysql_charset': 'utf8'}

    Number = Column(Integer, nullable=False, primary_key=True)
    URL = Column(String(20), nullable=False)
    Code = Column(String(3), nullable=False)
    IP = Column(String(15), nullable=False)
    Count = Column(String(5), nullable=False)


class Top3(Base):
    __tablename__ = 'top10_by_redirect'
    __table_args__ = {'mysql_charset': 'utf8'}

    Number = Column(Integer, nullable=False, primary_key=True)
    URL = Column(String(20), nullable=False)
    Code = Column(String(3), nullable=False)
    IP = Column(String(15), nullable=False)
    Count = Column(String(5), nullable=False)
