from banco_dados import db

class ProdutoFornecedor(db.Model):
    __tablename__ = 'produto_fornecedor'
    
    id = db.Column(db.Integer, primary_key=True)
    produto_id = db.Column(db.Integer, db.ForeignKey('produto.id'), nullable=False)
    fornecedor_id = db.Column(db.Integer, db.ForeignKey('fornecedor.id'), nullable=False)
    
    produto = db.relationship('Produto', backref='fornecedores')
    fornecedor = db.relationship('Fornecedor', backref='produtos')

    def __repr__(self):
        return f"<ProdutoFornecedor {self.produto_id} - {self.fornecedor_id}>"
