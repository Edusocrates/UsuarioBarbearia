from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from UsuarioBarbeariaApp import app, db  # Importe seu aplicativo Flask e o objeto db

migrate = Migrate(app, db)
manager = Manager(app)

# Adicione os comandos de migração ao gerenciador
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
