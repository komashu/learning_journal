from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    DateTime,
    String
)
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .meta import Base


now = datetime.now()
engine = create_engine('sqlite:///')
db = sessionmaker(bind=engine)
session = db()


#class MyModel(Base):
#    __tablename__ = 'models'
#    id = Column(Integer, primary_key=True)
#    name = Column(Text)
#    value = Column(Integer)

class Entry(Base):
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    title = Column(String(255), unique=True, nullable=False)
    body = Column(Text)
    created = Column(DateTime, default=now)
    edited = Column(DateTime, default=now)

    @classmethod
    def all(cls):
        return session.query(Entry).order_by(Entry.created)

    @classmethod
    def by_id(cls):
        return session.query(Entry).order_by(Entry.id)




Index('entry', Entry.title, unique=True, mysql_length=255)
