from urllib import request
from flask import render_template

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
            data = request.json
            nome = data.get('nome')
            email = data.get('email')
            novo_usuario = UsuarioService.criar_usuario(nome, email)
            return f"Usuário {novo_usuario.nome} criado com sucesso"


        @self.app.route('/agendar')
        def agendar():
            # Aqui você pode adicionar a lógica para permitir que os usuários agendem um horário na barbearia
            return "Página de agendamento"

        @self.app.route('/servicos')
        def listar_servicos():
            # Aqui você pode adicionar a lógica para listar os serviços oferecidos pela barbearia
            return "Lista de serviços oferecidos pela barbearia"
