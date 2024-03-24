from flask import Flask

from controller.UsuarioController import UsuarioController

class UsuarioBarbeariaApp:
    def __init__(self):
        self.app = Flask(__name__)
        self.usuario_controller = UsuarioController(self.app)

    def run(self):
        self.app.run(host='0.0.0.0', port=8080)

if __name__ == '__main__':
    app = UsuarioBarbeariaApp()
    app.run()