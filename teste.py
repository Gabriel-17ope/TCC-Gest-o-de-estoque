# firebase_fornecedor.py

import firebase_admin
from firebase_admin import credentials, firestore

# Inicialize o Firebase com o arquivo de chave de serviço
cred = credentials.Certificate('firebase_key.json')  # Substitua pelo caminho correto
firebase_admin.initialize_app(cred)

# Função para obter e imprimir os dados de fornecedores
def imprimir_fornecedores():
    # Referência à coleção ou caminho do seu banco de dados
    db = firestore.client()  # ou firebase_admin.db se usar Realtime Database
    fornecedores_ref = db.collection('fornecedores')  # Supondo que a coleção se chame 'fornecedores'

    # Recupera os documentos de fornecedores
    fornecedores = fornecedores_ref.stream()

    # Itera sobre os fornecedores e imprime no terminal
    for fornecedor in fornecedores:
        data = fornecedor.to_dict()  # Converte o documento para um dicionário
        print("Dados do Fornecedor:")
        print(f"Razão Social: {data.get('razaoSocial')}")
        print(f"CNPJ: {data.get('cnpj')}")
        print(f"Nome Fantasia: {data.get('nomeFantasia')}")
        print("-" * 50)

# Chama a função para imprimir os dados no console
if __name__ == '__main__':
    imprimir_fornecedores()
    
