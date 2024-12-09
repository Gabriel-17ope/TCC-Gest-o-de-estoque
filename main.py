from flask import Flask, render_template
from routes.estoque import estoque_blueprint
from routes.financeiro import financeiro_blueprint
from routes.fornecedor import fornecedor_blueprint
from routes.relatorios import relatorios_blueprint
from firebase_config import Config

# Inicializando o Flask
app = Flask(__name__)

# Configurando a SECRET_KEY
app.secret_key = Config.SECRET_KEY

# Registrando os Blueprints
app.register_blueprint(estoque_blueprint, url_prefix='/estoque')
app.register_blueprint(fornecedor_blueprint, url_prefix='/fornecedor')
app.register_blueprint(financeiro_blueprint, url_prefix='/financeiro')
app.register_blueprint(relatorios_blueprint, url_prefix='/relatorio')

# Rota de homepage
@app.route("/")
def homepage():
    return render_template("Tela_login_principal_cadastro/tela_principal.html")

# Executando o servidor
if __name__ == "__main__":
    app.run(debug=True)
