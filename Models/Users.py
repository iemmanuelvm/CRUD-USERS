import uuid

from db import db


class UserModel(db.Model):
    # CREATE TABLE IN DATABASE
    __tablename__ = "user"

    # USER ATRIBUTES
    id = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()), unique=True)
    name = db.Column(db.String(256), nullable=False)
    last_name = db.Column(db.String(256), nullable=False)
    email = db.Column(db.String(256), nullable=False)
    phone = db.Column(db.String(256), nullable=False)