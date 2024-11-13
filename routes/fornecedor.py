# routes/fornecedor.py

from flask import Blueprint, render_template, request, redirect, url_for
from banco_dados import db
from models.modelo_fornecedor import Fornecedor

# Criando o blueprint para fornecedores
fornecedor_blueprint = Blueprint('fornecedor', __name__, template_folder='templates')

# Rota para cadastrar um fornecedor
@fornecedor_blueprint.route('/cadastro', methods=['GET', 'POST'])
def cadastro_fornecedor():
    if request.method == 'POST':
        nome = request.form['nome']
        cnpj = request.form['cnpj']
        endereco = request.form['endereco']
        
        novo_fornecedor = Fornecedor(nome=nome, cnpj=cnpj, endereco=endereco)
        db.session.add(novo_fornecedor)
        db.session.commit()
        
        return redirect(url_for('fornecedor.lista_fornecedores'))
    
    return render_template('Fornecedor/cadastro_fornecedor.html')

# Rota para listar todos os fornecedores
@fornecedor_blueprint.route('/lista')
def lista_fornecedores():
    fornecedores = Fornecedor.query.all()
    return render_template('Fornecedor/Tela_fornecedores.html', fornecedores=fornecedores)
