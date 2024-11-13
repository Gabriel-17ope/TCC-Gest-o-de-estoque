from banco_dados import db

class Produto(db.Model):
    __tablename__ = 'produto'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(200), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id'), nullable=False)
    fornecedor_id = db.Column(db.Integer, db.ForeignKey('fornecedor.id'), nullable=False)
    imagem = db.Column(db.String(100))  # Caminho da imagem do produto
    
    categoria = db.relationship('Categoria', back_populates='produtos')
    fornecedor = db.relationship('Fornecedor', back_populates='produtos')

    def __repr__(self):
        return f"<Produto {self.nome}>"
