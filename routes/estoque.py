from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
import uuid
from firebase_config import bucket, db  # Importa o bucket e o db corretamente


estoque_blueprint = Blueprint('estoque', __name__, template_folder='templates')

@estoque_blueprint.route('/')  # Definindo a raiz da rota como '/'
def tela_estoque():
    return render_template('Estoque/Tela_estoque.html')

@estoque_blueprint.route('/cadastro',methods=['GET','POST'])
def tela_estoque_cadastro():
    if request.method == 'POST':
        nomeProduto = request.form.get('nomeProduto')
        valorProduto = request.form.get('valorProduto')
        nome_fantasia = request.form.get('quantidade')

        imagemProduto = request.files.get('imagemProduto')

        # Verifica se todos os campos foram preenchidos
        if not razao_social or not cnpj or not nome_fantasia or not imagem:
            flash("Todos os campos são obrigatórios, incluindo a imagem!")
            return render_template('Fornecedor/Tela_fornecedor_cadastro.html')

        try:
            # Verifica se a imagem foi fornecida
            if imagem:
                # Fazendo upload da imagem para o Firebase Storage
                filename = secure_filename(imagem.filename)
                unique_filename = f"fornecedores/{uuid.uuid4()}.{filename.split('.')[-1]}"

                print(f"Nome do arquivo recebido: {filename}")
                print(f"Nome único gerado para upload: {unique_filename}")

                # Upload no Firebase Storage
                blob = bucket.blob(unique_filename)

                # Tenta fazer o upload do arquivo
                try:
                    blob.upload_from_file(imagem, content_type=imagem.content_type)
                    print(f"Upload realizado com sucesso para: {unique_filename}")
                    blob.make_public()  # Torna o arquivo acessível publicamente
                    imagem_url = blob.public_url  # URL pública da imagem
                    print(f"Imagem carregada com sucesso! URL pública: {imagem_url}")
                except Exception as upload_error:
                    print(f"Erro ao fazer upload da imagem para o Firebase: {upload_error}")
                    imagem_url = None
            else:
                imagem_url = None  # Caso a imagem não tenha sido fornecida

            # Referência ao Firestore para salvar os dados do fornecedor
            fornecedores_ref = db.collection('fornecedores')

            # Dados do fornecedor a serem armazenados
            fornecedor_data = {
                'razaoSocial': razao_social,
                'cnpj': cnpj,
                'nomeFantasia': nome_fantasia,
                'imagem': imagem_url  # Salvando a URL da imagem no Firestore
            }

            # Adicionar os dados no Firestore
            fornecedores_ref.add(fornecedor_data)

            flash("Fornecedor cadastrado com sucesso!")
            return redirect(url_for('fornecedor.tela_fornecedor'))

        except Exception as e:
            flash(f"Erro ao salvar os dados ou enviar a imagem: {e}")
            return render_template('Fornecedor/Tela_fornecedor_cadastro.html')

    return render_template('Fornecedor/Tela_fornecedor_cadastro.html')
