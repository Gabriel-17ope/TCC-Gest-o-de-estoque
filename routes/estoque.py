from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from werkzeug.utils import secure_filename
import uuid
from firebase_config import bucket, db  # Importa o bucket e o db corretamente

estoque_blueprint = Blueprint('estoque', __name__, template_folder='templates')


# Renderiza a tela de estoque
@estoque_blueprint.route('/')
def tela_estoque():
    return render_template('Estoque/Tela_estoque.html')

# Endpoint para obter a lista de fornecedores
@estoque_blueprint.route('/fornecedores', methods=['GET'])
def obter_fornecedores():
    try:
        fornecedores_ref = db.collection('fornecedores').stream()
        fornecedores = [
            {'id': doc.id, 'nomeFantasia': doc.to_dict().get('nomeFantasia')} 
            for doc in fornecedores_ref
        ]
        return jsonify(fornecedores)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Renderiza a tela de cadastro de produto e processa o envio de dados
@estoque_blueprint.route('/cadastro', methods=['GET', 'POST'])
def tela_estoque_cadastro():
    if request.method == 'POST':
        # Obtendo dados do formulário
        nome_produto = request.form.get('nomeProduto')
        valor_produto = request.form.get('valorProduto')
        fornecedor_id = request.form.get('fornecedor_id')
        quantidade = request.form.get('quantidade')
        quantidade_minima = request.form.get('quantidade_minima')
        imagem = request.files.get('imagemProduto')

        if not fornecedor_id:
            flash("Por favor, selecione um fornecedor.")
            return redirect(url_for('estoque.tela_estoque_cadastro'))
        
        # Verifica se o fornecedor existe no Firestore
        fornecedor_ref = db.collection('fornecedores').document(fornecedor_id).get()
        if not fornecedor_ref.exists:
            flash("Fornecedor não encontrado. Verifique sua seleção.")
            return redirect(url_for('estoque.tela_estoque_cadastro'))
        
        # Validação básica para garantir que os campos principais foram preenchidos
        if not nome_produto or not valor_produto or not fornecedor_id or not quantidade or not quantidade_minima:
            flash("Todos os campos obrigatórios devem ser preenchidos!")
            return render_template('Estoque/Cadastro_Produto.html')

        try:
            # Geração de um produto_id único
            produto_id = str(uuid.uuid4())

            # Verifica se há imagem para fazer upload
            if imagem:
                filename = secure_filename(imagem.filename)
                unique_filename = f"produtos/{uuid.uuid4()}.{filename.split('.')[-1]}"

                blob = bucket.blob(unique_filename)

                try:
                    blob.upload_from_file(imagem, content_type=imagem.content_type)
                    blob.make_public()
                    imagem_url = blob.public_url
                except Exception as e:
                    print(f"Erro no upload da imagem: {e}")
                    imagem_url = None
            else:
                imagem_url = None

            # Salva os dados no Firestore
            produtos_ref = db.collection('produtos')
            produto_data = {
                'produto_id': produto_id,  # Incluindo produto_id no Firestore
                'nomeProduto': nome_produto,
                'valorProduto': float(valor_produto),
                'fornecedor_id': fornecedor_id,
                'quantidade': int(quantidade),
                'quantidade_minima': int(quantidade_minima),
                'imagem': imagem_url
            }

            produtos_ref.add(produto_data)  # Salvando no Firestore
            flash("Produto cadastrado com sucesso!")
            return redirect(url_for('estoque.tela_estoque'))
        except Exception as e:
            print(f"Erro ao salvar no Firestore: {e}")
            flash("Erro ao salvar o produto!")
            return render_template('Estoque/Tela_estoque_cadastro_produtos.html')

    return render_template('Estoque/Tela_estoque_cadastro_produtos.html')
