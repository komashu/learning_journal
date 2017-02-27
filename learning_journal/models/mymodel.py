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
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import (
  scoped_session,
  sessionmaker,
  )
from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

from .meta import Base


now = datetime.now()
engine = create_engine('sqlite:///learning_journal.sqlite')
db = sessionmaker(bind=engine)
session = db()



class Entry(Base):
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    title = Column(String(255), unique=True, nullable=False)
    body = Column(Text)
    created = Column(DateTime, default=now)
    edited = Column(DateTime, default=now)

    @classmethod
    def all(cls, session=None):
        if session is None:
            session = DBSession
        return session.query(cls).order_by(sa.desc(cls.created)).all()

    @classmethod
    def by_id(cls, id, session=None):
        if session is None:
            session = DBSession
        return session.query(cls).get(id)




Index('entry', Entry.title, unique=True, mysql_length=255)
