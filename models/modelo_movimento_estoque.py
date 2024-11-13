from banco_dados import db
from datetime import datetime

class MovimentacaoEstoque(db.Model):
    __tablename__ = 'movimentacao_estoque'
    
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.DateTime, default=datetime.utcnow)
    quantidade = db.Column(db.Integer, nullable=False)
    tipo = db.Column(db.String(50), nullable=False)  # Ex: 'entrada', 'saida'
    produto_id = db.Column(db.Integer, db.ForeignKey('produto.id'), nullable=False)
    
    produto = db.relationship('Produto', backref='movimentacoes')
    
    def __repr__(self):
        return f"<MovimentacaoEstoque {self.tipo} - {self.quantidade} unidades>"
