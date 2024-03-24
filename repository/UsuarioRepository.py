from model.Usuario import Usuario, db

# usuario_repository.py
class UsuarioRepository:
    @staticmethod
    def obter_todos_usuarios():
        return Usuario.query.all()

    @staticmethod
    def criar_usuario(nome, email):
        novo_usuario = Usuario(nome=nome, email=email)
        db.session.add(novo_usuario)
        db.session.commit()
        return novo_usuario