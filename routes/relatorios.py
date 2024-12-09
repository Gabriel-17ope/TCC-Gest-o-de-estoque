from flask import Blueprint, render_template, Response, request, redirect, url_for, flash
import csv
from datetime import datetime
from firebase_config import db


# Criando o blueprint para relatórios
relatorios_blueprint = Blueprint('relatorios', __name__, template_folder='templates')


# Função para buscar dados no Firestore com base no intervalo de datas e filtros
def buscar_dados_firestore(data_inicio, data_fim, tipo_relatorio, filtro, valor_filtro):
    dados = []
    try:
        # Convertendo strings de datas para objetos datetime com validação
        data_inicio = datetime.strptime(data_inicio, '%Y-%m-%d')
        data_fim = datetime.strptime(data_fim, '%Y-%m-%d')

        if data_inicio > data_fim:
            raise ValueError("A data de início não pode ser maior que a data final.")

        # Referência correta para a coleção Firestore
        relatorios_ref = db.collection('movimentacoes_financeiras')

        # Lógica para cada tipo de relatório
        if tipo_relatorio == "despesas":
            # Buscar apenas despesas
            query = relatorios_ref \
                .filter("data", ">=", data_inicio.isoformat()) \
                .filter("data", "<=", data_fim.isoformat()) \
                .filter("tipo", "==", "despesa")
        elif tipo_relatorio == "balancete":
            # Buscar entradas e saídas dentro do intervalo de datas
            query = relatorios_ref \
                .where("data", ">=", data_inicio.isoformat()) \
                .where("data", "<=", data_fim.isoformat())
        elif tipo_relatorio == "fluxo_caixa":
            # Buscar todas as movimentações de entradas e saídas no intervalo
            query = relatorios_ref \
                .filter("data", ">=", data_inicio.isoformat()) \
                .filter("data", "<=", data_fim.isoformat())
        elif tipo_relatorio == "dre":
            # Buscar tanto receitas quanto despesas para análise
            query = relatorios_ref \
                .where("data", ">=", data_inicio.isoformat()) \
                .where("data", "<=", data_fim.isoformat())
        else:
            raise ValueError("Tipo de relatório desconhecido.")

        # Executando a consulta no Firestore
        for doc in query.stream():
            # Validando filtros adicionais caso existam
            if filtro and valor_filtro:
                if filtro in doc.to_dict() and doc.to_dict()[filtro] != valor_filtro:
                    continue
            dados.append(doc.to_dict())
            print(dados)

        if not dados:
            flash('Nenhum dado encontrado para os critérios fornecidos.', 'warning')

    except ValueError as ve:
        flash(str(ve), 'error')
    except Exception as e:
        print(f"Erro ao buscar dados no Firestore: {e}")
        flash('Erro ao buscar dados no Firestore.', 'error')

    return dados


# Função para criar CSV para relatório
def criar_csv(headers, dados):
    from io import StringIO

    # Configuração do buffer CSV
    output = StringIO()
    writer = csv.DictWriter(output, fieldnames=headers)

    writer.writeheader()
    for row in dados:
        writer.writerow({
            "data": row.get("data", ""),
            "fornecedor": row.get("fornecedor", ""),
            "produto": row.get("produto", ""),
            "valor": row.get("valor", 0),
        })

    csv_conteudo = output.getvalue()
    output.close()
    return csv_conteudo


# Rota para a tela principal de relatório
@relatorios_blueprint.route('/')
def tela_relatorio():
    # Renderiza a tela principal com opções de relatório como botões
    return render_template('Relatorio/relatorio.html')


# Rota para configurar relatório
@relatorios_blueprint.route('/configurar', methods=["GET", "POST"])
def configurar_relatorio():
    if request.method == 'POST':
        # Capturando dados do formulário
        data_inicio = request.form.get('data_inicio')
        data_fim = request.form.get('data_fim')
        tipo_relatorio = request.form.get('tipo_relatorio')
        filtro = request.form.get('filtro')  # Campo de filtro opcional
        valor_filtro = request.form.get('valor_filtro')  # Campo de filtro opcional

        # Validando os campos obrigatórios
        if not data_inicio or not data_fim:
            flash('Por favor, informe o intervalo de datas.', 'error')
            return redirect(url_for('relatorios.configurar_relatorio'))

        # Buscando dados no Firestore com base no relatório
        dados = buscar_dados_firestore(data_inicio, data_fim, tipo_relatorio, filtro, valor_filtro)

        # Gerando CSV com base no relatório
        headers = ["data", "fornecedor", "produto", "valor"]
        csv_conteudo = criar_csv(headers, dados)

        # Configurando resposta para download
        response = Response(csv_conteudo, content_type='text/csv')
        response.headers["Content-Disposition"] = f'attachment; filename="{tipo_relatorio}_relatorio.csv"'
        return response

    # Se for GET, renderiza a tela de configuração do relatório
    return render_template('Relatorio/configurar.html')
