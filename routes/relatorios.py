from banco_dados import db
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from main import app

@app.route('/relatorio_dre')
def relatorio_dre():
    receita = db.session.query(db.func.sum(Produto.preco * Movimentacao_Estoque.quantidade)).filter(Movimentacao_Estoque.tipo == 'venda').scalar()
    custo = db.session.query(db.func.sum(Produto.preco * Movimentacao_Estoque.quantidade)).filter(Movimentacao_Estoque.tipo == 'compra').scalar()
    lucro_bruto = receita - custo
    despesas = 5000  # Exemplo de despesas fixas
    lucro_liquido = lucro_bruto - despesas
    return render_template('relatorio_dre.html', receita=receita, custo=custo, lucro_bruto=lucro_bruto, despesas=despesas, lucro_liquido=lucro_liquido)
