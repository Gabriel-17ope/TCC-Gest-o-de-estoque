from banco_dados import db
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from main import app
from models.moledo_produto import *
from models.modelo_fornecedor import *
from models.modelo_movimento_estoque import *
from models.modelo_produto_fornecedor import *


@app.route('/dashboard')
def dashboard():
    total_produtos = Produto.query.count()
    total_fornecedores = Fornecedor.query.count()
    total_vendas = db.session.query(db.func.sum(Produto.preco * Movimentacao_Estoque.quantidade)).filter(Movimentacao_Estoque.tipo == 'venda').scalar()
    return render_template('dashboard.html', total_produtos=total_produtos, total_fornecedores=total_fornecedores, total_vendas=total_vendas)
