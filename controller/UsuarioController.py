from urllib import request
from flask import request, jsonify

from model.Usuario import Usuario, db
from repository.UsuarioRepository import UsuarioRepository
from service.UsuarioService import UsuarioService

class UsuarioController:
    def __init__(self, app):
        self.app = app

        @self.app.route('/')
        def index():
            return "Hello, world!"

        @self.app.route('/usuarios', methods=['GET'])
        def listar_usuarios():
            usuarios = UsuarioService.obter_todos_usuarios()
            return "Usuários: " + ", ".join([usuario.nome for usuario in usuarios])


        @self.app.route('/usuarios', methods=['POST'])
        def criar_usuario():
            # Verifica se o conteúdo da solicitação é JSON
            if not request.is_json:
                return jsonify({"error": "O corpo da solicitação deve ser um JSON"}), 400

            # Obtém os dados JSON do corpo da solicitação
            data = request.json

            # Verifica se os campos 'nome' e 'email' estão presentes no JSON
            if 'nome' not in data or 'email' not in data:
                return jsonify({"error": "O JSON deve conter campos 'nome' e 'email'"}), 400

            # Extrai os dados do JSON
            nome = data['nome']
            email = data['email']

            # Chama o método do serviço para criar o usuário
            novo_usuario = UsuarioService.criar_usuario(nome, email)

            # Retorna uma mensagem de sucesso com o nome do usuário criado
            return jsonify({"message": f"Usuário {novo_usuario.nome} criado com sucesso"}), 201


        @self.app.route('/agendar')
        def agendar():
            # Aqui você pode adicionar a lógica para permitir que os usuários agendem um horário na barbearia
            return "Página de agendamento"

        @self.app.route('/servicos')
        def listar_servicos():
            # Aqui você pode adicionar a lógica para listar os serviços oferecidos pela barbearia
            return "Lista de serviços oferecidos pela barbearia"
