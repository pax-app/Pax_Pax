from database import db
from project import create_app
from Flask import current_app
from database_singleton import Singleton

db = Singleton().database_connection()


class Pax(db.Model):
    __tablename__ = 'PAX'

    pax_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    data = db.Column(db.Date, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
    status = db.Column(db.Enum('F', 'P', 'C', 'I'), nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    provider_id = db.Column(db.Integer, nullable=False)
    chat_id = db.Column(db.Integer, nullable=False)
    address_id = db.Column(db.Integer, nullable=False)

    def __init__(self, data, description, name, price, status, user_id, provider_id, chat_id, address_id):
        self.data = data
        self.description = description
        self.name = name
        self.price = price
        self.status = name
        self.user_id = user_id
        self.provider_id = provider_id
        self.chat_id = chat_id
        self.address_id = address_id

    def to_json(self):
        return {
            'id': self.pax_id,
            'data': self.data,
            'description': self.description,
            'name': self.name,
            'price': self.price,
            'status': self.status,
            'user_id': self.user_id,
            'provider_id': self.provider_id,
            'chat_id': self.chat_id,
            'address_id': self.address_id
        }
