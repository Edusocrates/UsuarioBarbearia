from flask_sqlalchemy import SQLAlchemy

from db import db

class Agenda(db.Model):
    id_agendamento = db.Column(db.Integer, primary_key=True)
    nome_cliente = db.Column(db.String(100))
    data_agendamento = db.Column(db.Date)
    nome_profissional = db.Column(db.String(100))
    servico = db.Column(db.String(100))

    def __init__(self, nome_cliente, data_agendamento, nome_profissional, servico):
        self.nome_cliente = nome_cliente
        self.data_agendamento = data_agendamento
        self.nome_profissional = nome_profissional
        self.servico = servico
