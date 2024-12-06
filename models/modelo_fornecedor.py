from banco_dados import db

class Fornecedor(db.Model):
    __tablename__ = 'fornecedor'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    endereco = db.Column(db.String(200))

    produtos = db.relationship('Produto', back_populates='fornecedor')

    def __repr__(self):
        return f"<Fornecedor {self.nome}>"
