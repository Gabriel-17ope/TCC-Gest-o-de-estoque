# app.py

from flask import Flask, render_template
from banco_dados import db
from routes.produto import produto_blueprint

from models.categoria import categoria
from models.moledo_produto import Produto

from routes.fornecedor import fornecedor_blueprint
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'database.db')}"

# Configuração do banco de dados
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'database.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializando o banco de dados
db.init_app(app)

# Registrando os blueprints
app.register_blueprint(produto_blueprint, url_prefix='/produtos')
app.register_blueprint(fornecedor_blueprint, url_prefix='/fornecedores')

# Rota de homepage (página principal)
@app.route("/")
def homepage():
    return render_template("Tela_login_principal_cadastro/tela_principal.html")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Cria as tabelas se não existirem
    app.run(debug=True)
