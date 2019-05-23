from sqlalchemy import Column, Integer, String, ARRAY, Boolean, MetaData
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class Dialog(Base):
    __tablename__ = 'dialogs'
    peer_id = Column(Integer, primary_key=True)
    rules = Column(String, default='')
    autopost = Column(Boolean, default=False)
    printlist = Column(Boolean, default=True)
    template = Column(String, default='')
    key = Column(String, default='')


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    vk_id = Column(Integer)
    peer_id = Column(Integer)
    category = Column(String)
    messages = Column(Integer)