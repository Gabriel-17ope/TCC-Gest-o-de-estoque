# models/Categoria.py
from banco_dados import db

class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(200))

    produtos = db.relationship('Produto', backref='categoria', lazy=True)
