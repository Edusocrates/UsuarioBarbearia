from flask import render_template

class UsuarioController:
    def __init__(self, app):
        self.app = app

        @self.app.route('/')
        def index():
            return "Hello, world!"

        @self.app.route('/usuarios')
        def listar_usuarios():
            # Aqui você pode adicionar a lógica para listar os usuários da barbearia
            return "Lista de usuários da barbearia"

        @self.app.route('/agendar')
        def agendar():
            # Aqui você pode adicionar a lógica para permitir que os usuários agendem um horário na barbearia
            return "Página de agendamento"

        @self.app.route('/servicos')
        def listar_servicos():
            # Aqui você pode adicionar a lógica para listar os serviços oferecidos pela barbearia
            return "Lista de serviços oferecidos pela barbearia"
