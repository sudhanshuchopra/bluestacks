import sqlalchemy as sa
from sqlalchemy.orm import backref
from sqlalchemy.ext.declarative import declarative_base

from connections import engine

base = declarative_base()
base.metadata.bind = engine
session = sa.orm.scoped_session(sa.orm.sessionmaker())(bind=engine)


class History(base):
    """
    Data Model for history Table
    """
    __tablename__ = 'history'
    id = sa.Column(sa.Integer(), autoincrement=True, primary_key=True)
    search_key = sa.Column(sa.String(150), index=True)
