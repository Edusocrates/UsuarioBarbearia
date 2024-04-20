# usuario_model.py
from flask_sqlalchemy import SQLAlchemy

from db import db


class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    senha = db.Column(db.String(200))

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha