from app import db
from flask import json
import logging
from wallet.messages import DATABASE_ERROR

class Wallet(db.Model):
    __table_args__ = {"schema":"cpex"}
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, unique=True, nullable=False)
    amount = db.Column(db.Numeric(20,4), unique=True, nullable=False)

    def __init__(self, owner_id, amount):
        self.owner_id = owner_id
        self.amount = amount
    
    def to_JSON(self):
        result = {}
        result['amount'] = float(self.amount)
        result['id'] = self.id
        result['owner_id'] = self.owner_id
        return json.dumps(result, indent=4)


def create_wallet(owner_id, amount):
    try:
        wallet = Wallet(owner_id, amount)
        db.session.add(wallet)
        db.session.commit()
    except exc.SQLAlchemyError:
        logging.info(DATABASE_ERROR)   
    return wallet

def read_wallet(id):
    try:
        wallet = Wallet.query.get(id)
    except exc.SQLAlchemyError:
        logging.info(DATABASE_ERROR)
    return wallet

def update_wallet(id, amount):
    try:
        wallet = Wallet.query.get(id)
        wallet.amount = amount
        db.session.commit()
    except exc.SQLAlchemyError:
        logging.info(DATABASE_ERROR)
    return wallet

def delete_wallet(id):
    try:
        Wallet.query.filter(Wallet.id == id).delete()
        db.session.commit()
    except exc.SQLAlchemyError:
        logging.info(DATABASE_ERROR)

