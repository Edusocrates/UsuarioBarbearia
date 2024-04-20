from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from adapter.controller.UsuarioController import UsuarioController
from adapter.controller.AgendaController import AgendaController
from entities import Usuario, Agenda
from db import db

class UsuarioBarbeariaApp:
    def __init__(self):
        self.app = Flask(__name__)
        self.db = db

        # Configuração do banco de dados MySQL
        # Aqui você precisará configurar a conexão com o banco de dados MySQL
        # Configuração do banco de dados
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:admin@localhost/barbearia'
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True  # Desativando o rastreamento de modificações

        # Inicializa o banco de dados
        self.db.init_app(self.app)

        # Criar as tabelas no banco de dados
        with self.app.app_context():
            self.db.create_all()

        # Instanciando o controlador e passando o serviço
        self.usuario_controller = UsuarioController(self.app)
        self.agenda_controller = AgendaController(self.app)

    def run(self):
        self.app.run(debug=True, port=8080)

if __name__ == '__main__':
    app = UsuarioBarbeariaApp()
    app.run()