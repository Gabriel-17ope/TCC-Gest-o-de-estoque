# routes/financeiro.py
from flask import Blueprint, render_template

# Criando o blueprint para financeiro
financeiro_blueprint = Blueprint('relatorio', __name__, template_folder='templates')

# Rota para a tela principal de financeiro
@financeiro_blueprint.route('/')
def tela_financeiro():
    return render_template('Relatorio/relatorio.html')
