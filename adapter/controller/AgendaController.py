from urllib import request
from flask import request, jsonify

from entities.Agenda import db
from core.service.AgendaService import AgendaService

class AgendaController:
    def __init__(self, app):
        self.app = app

        @self.app.route('/agendamentos', methods=['GET'])
        def obter_todos_agendamentos():
            # Obtém todos os agendamentos do serviço
            agendamentos = AgendaService.obter_todos_agendamentos()

            # Converte os objetos de agendamento para um formato serializável (dicionário)
            agendamentos_json = []
            for agendamento in agendamentos:
                data_formatada = agendamento.data_agendamento.strftime('%d/%m/%Y')

                agendamento_json = {
                    'id_agendamento': agendamento.id_agendamento,
                    'nome_cliente': agendamento.nome_cliente,
                    'data_agendamento': data_formatada,
                    'nome_profissional': agendamento.nome_profissional,
                    'servico': agendamento.servico
                    # Adicione outros campos conforme necessário
                }
                agendamentos_json.append(agendamento_json)

            # Retorna a lista de agendamentos em JSON com o código de status 200
            return jsonify(agendamentos_json), 200