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


        @self.app.route('/agendar', methods=['POST'])
        def criar_agendamento():
            # Verifica se o conteúdo da solicitação é JSON
            if not request.is_json:
                return jsonify({"error": "O corpo da solicitação deve ser um JSON"}), 400

            # Obtém os dados JSON do corpo da solicitação
            data = request.json

            # Verifica se os campos necessários estão presentes no JSON
            if 'nome_cliente' not in data or 'data_agendamento' not in data or 'nome_profissional' not in data or 'servico' not in data:
                return jsonify({"error": "O JSON deve conter campos 'nome_cliente', 'data_agendamento', 'nome_profissional' e 'servico'"}), 400

            # Extrai os dados do JSON
            nome_cliente = data['nome_cliente']
            data_agendamento = data['data_agendamento']
            nome_profissional = data['nome_profissional']
            servico = data['servico']

            # Chama o método do serviço para criar o agendamento
            novo_agendamento = AgendaService.criar_agendamento(nome_cliente, data_agendamento, nome_profissional, servico)

            # Retorna uma mensagem de sucesso com os detalhes do agendamento criado
            return jsonify({"message": f"Agendamento para {novo_agendamento.nome_cliente} criado com sucesso",
                            "id_agendamento": novo_agendamento.id_agendamento}), 201