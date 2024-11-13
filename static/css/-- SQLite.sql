-- SQLite

CREATE DATABASE Gest_stock;


CREATE TABLE Usuario (
  idUsuario INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  nome VARCHAR(255) NULL,
  login VARCHAR(50) NULL,
  senha VARCHAR(255) NULL,
  PRIMARY KEY(idUsuario)
);

CREATE TABLE Categoria (
  idCategoria INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  nome VARCHAR(255) NULL,
  PRIMARY KEY(idCategoria)
);

CREATE TABLE Produto (
  idProduto INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  Categoria_id INTEGER UNSIGNED NOT NULL,
  preco DECIMAL(10,2) NOT NULL,
  nome VARCHAR(255) NOT NULL,
  quantidade_minima INTEGER UNSIGNED NULL,
  quantidade_atual INTEGER UNSIGNED NOT NULL,
  Imagem BLOB NULL,
  PRIMARY KEY(idProduto),
  INDEX Produto_FKIndex1(Categoria_id),
  FOREIGN KEY(Categoria_id) REFERENCES Categoria(idCategoria)
);

CREATE TABLE Fornecedor (
  idFornecedor INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  nome VARCHAR(255) NOT NULL,
  contato VARCHAR(255) NOT NULL,
  endereco VARCHAR(255) NOT NULL,
  Imagem BLOB NULL,
  PRIMARY KEY(idFornecedor)
);

CREATE TABLE Produto_fornecedor (
  idProduto_fornecedor INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  Fornecedor_id INTEGER UNSIGNED NOT NULL,
  Produto_id INTEGER UNSIGNED NOT NULL,
  data_ultima_compra DATETIME NULL,
  PRIMARY KEY(idProduto_fornecedor),
  INDEX Produto_fornecedor_FKIndex1(Produto_id),
  INDEX Produto_fornecedor_FKIndex2(Fornecedor_id),
  FOREIGN KEY(Produto_id) REFERENCES Produto(idProduto),
  FOREIGN KEY(Fornecedor_id) REFERENCES Fornecedor(idFornecedor)
);

CREATE TABLE Movimentacao_estoque (
  idMovimentacao_estoque INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  Usuario_idUsuario INTEGER UNSIGNED NOT NULL,
  Produto_idProduto INTEGER UNSIGNED NOT NULL,
  data_2 DATETIME NULL,
  Tipo ENUM('Entrada', 'Saída') NULL,
  quantidade INTEGER UNSIGNED NULL,
  PRIMARY KEY(idMovimentacao_estoque),
  INDEX Movimentacao_estoque_FKIndex1(Produto_idProduto),
  INDEX Movimentacao_estoque_FKIndex2(Usuario_idUsuario),
  FOREIGN KEY(Produto_idProduto) REFERENCES Produto(idProduto),
  FOREIGN KEY(Usuario_idUsuario) REFERENCES Usuario(idUsuario)
);

CREATE TABLE Relatorio (
  idRelatorio INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  Usuario_idUsuario INTEGER UNSIGNED NOT NULL,
  tipo_relatorio ENUM('Fluxo_Caixa', 'Balancete', 'DRE', 'Recebimentos') NULL,
  data_inicio DATETIME NULL,
  data_fim DATETIME NULL,
  dados LONGTEXT NULL,
  PRIMARY KEY(idRelatorio),
  INDEX Relatorio_FKIndex1(Usuario_idUsuario),
  FOREIGN KEY(Usuario_idUsuario) REFERENCES Usuario(idUsuario)
);

CREATE TABLE Movimentacao_financeira (
  idMovimentacao_financeira INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  Relatorio_idRelatorio INTEGER UNSIGNED NOT NULL,
  Despesa_idDespesa INTEGER UNSIGNED NOT NULL,
  venda_idvenda INTEGER UNSIGNED NOT NULL,
  tipo ENUM('Entrada', 'Saída') NULL,
  categoria VARCHAR(255) NULL,
  valor DECIMAL(10,2) NULL,
  data_2 DATETIME NULL,
  PRIMARY KEY(idMovimentacao_financeira),
  INDEX Movimentacao_financeira_FKIndex1(venda_idvenda),
  INDEX Movimentacao_financeira_FKIndex2(Despesa_idDespesa),
  INDEX Movimentacao_financeira_FKIndex3(Relatorio_idRelatorio),
  FOREIGN KEY(Relatorio_idRelatorio) REFERENCES Relatorio(idRelatorio),
  FOREIGN KEY(Despesa_idDespesa) REFERENCES Despesa(idDespesa),
  FOREIGN KEY(venda_idvenda) REFERENCES venda(idvenda)
);

CREATE TABLE Despesa (
  idDespesa INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  categoria VARCHAR(255) NULL,
  valor DECIMAL(10,2) NULL,
  data_2 DATETIME NULL,
  PRIMARY KEY(idDespesa)
);

CREATE TABLE venda (
  idvenda INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  valor_total DECIMAL(10,2) NULL,
  metodo_pagamento ENUM('À vista', 'Parcelado', 'Outro') NULL,
  PRIMARY KEY(idvenda)
);
