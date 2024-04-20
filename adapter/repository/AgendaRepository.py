from entities.Agenda import Agenda
from db import db

# usuario_repository.py
class AgendaRepository:
    @staticmethod
    def obter_todos_agendamentos():
        return Agenda.query.all()

    @staticmethod
    def criar_agendamento(nome_cliente, data_agendamento, servico, nome_profissional):
        novo_agendamento = Agenda(nome_cliente=nome_cliente, data_agendamento=data_agendamento, servico=servico, nome_profissional=nome_profissional)
        db.session.add(novo_agendamento)
        db.session.commit()
        return novo_agendamento