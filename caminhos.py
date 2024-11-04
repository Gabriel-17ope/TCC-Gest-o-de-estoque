from main import app
from flask import render_template
#rotas do site
@app.route("/")
def homepage():
     return render_template("Tela_login_principal_cadastro/tela_principal.html")
