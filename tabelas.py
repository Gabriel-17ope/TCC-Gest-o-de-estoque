from main import app
from banco_dados import db

# Criando as tabelas no banco de dados
with app.app_context():
    db.create_all()
print("Tabelas criadas com sucesso!")