from flask import Flask
from flask import Flask, render_template
from banco_dados import db
from routes.produto import produto_blueprint
from routes.fornecedor import fornecedor_blueprint
from routes.relatorios import relatorio_blueprint
from routes.financeiro import financeiro_blueprint
import os

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("Tela_login_principal_cadastro/tela_principal.html")

# Configuração da URL do banco de dados SQLite
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'database.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Associa o db ao app uma vez
db.init_app(app)

# Registra os Blueprints
app.register_blueprint(produto_blueprint, url_prefix='/estoque')
app.register_blueprint(fornecedor_blueprint, url_prefix='/fornecedor')
app.register_blueprint(relatorio_blueprint, url_prefix='/relatorio')
app.register_blueprint(financeiro_blueprint, url_prefix='/financeiro')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Cria as tabelas se não existirem
    app.run(debug=True)
