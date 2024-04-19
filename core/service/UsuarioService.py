from adapter.repository.UsuarioRepository import UsuarioRepository


class UsuarioService:
    @staticmethod
    def obter_todos_usuarios():
        return UsuarioRepository.obter_todos_usuarios()

    @staticmethod
    def criar_usuario(nome, email, senha):
        return UsuarioRepository.criar_usuario(nome, email, senha)