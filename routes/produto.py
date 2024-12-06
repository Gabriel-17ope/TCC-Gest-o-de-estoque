# routes/produto.py

from flask import Blueprint, render_template, request, redirect, url_for
from banco_dados import db
from models.moledo_produto import Produto
from app import db
from models.categoria import categoria


# Criando o blueprint para produtos
produto_blueprint = Blueprint('produto', __name__, template_folder='templates')

# Rota para cadastrar um produto
@produto_blueprint.route('/cadastro', methods=['GET', 'POST'])
def cadastro_produto():
    if request.method == 'POST':
        nome = request.form['nome']
        descricao = request.form['descricao']
        preco = request.form['preco']
        quantidade = request.form['quantidade']
        categoria_id = request.form['categoria_id']
        fornecedor_id = request.form['fornecedor_id']
        imagem = request.form['imagem']
        
        novo_produto = Produto(nome=nome, descricao=descricao, preco=preco, quantidade=quantidade, categoria_id=categoria_id, fornecedor_id=fornecedor_id, imagem=imagem)
        db.session.add(novo_produto)
        db.session.commit()
        
        return redirect(url_for('produto.lista_produtos'))
    
    return render_template('Estoque/Tela_cadastro_produto.html')

# Rota para listar todos os produtos
@produto_blueprint.route('/estoque')
def lista_produtos():
    produtos = Produto.query.all()
    return render_template('Estoque/Tela_estoque.html', produtos=produtos)
