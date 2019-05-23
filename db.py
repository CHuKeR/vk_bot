from sqlalchemy import create_engine, MetaData, func, or_
import logging
from sqlalchemy.orm import Session
from sqlalchemy.orm.query import Query
from models import *


class dbConnector:
    def __init__(self):
        self.Engine = create_engine('sqlite:///database.db',
                                    echo=False)
        Base.metadata.create_all(self.Engine)
        self.session = Session(bind=self.Engine)

    def get_group(self, peer_id):
        item = self.session.query(Dialog).filter(peer_id == Dialog.peer_id).first()
        if item is None:
            self.session.add(Dialog(peer_id=peer_id))
            self.session.commit()
            item = self.session.query(Dialog).filter(peer_id == Dialog.peer_id).first()
            return item
        else:
            return item

    def update_group_autopost(self, peer_id ):
        item = self.session.query(Dialog).filter(Dialog.peer_id == peer_id).first()
        item.autopost = not item.autopost
        self.session.commit()

    def update_group_printlist(self, peer_id):
        item = self.session.query(Dialog).filter(Dialog.peer_id == peer_id).first()
        item.printlist = not item.printlist
        self.session.commit()


