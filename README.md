Sistema de Gerenciamento de Estoque
Resumo do Trabalho
O Sistema de Gerenciamento de Estoque é uma aplicação desenvolvida para auxiliar micro e pequenas empresas no controle eficiente de seus estoques. O sistema permite o cadastro e gerenciamento de produtos e fornecedores, além de registrar movimentações de entrada e saída. A ferramenta visa proporcionar uma experiência simples e prática, utilizando tecnologias modernas para atender às demandas de gestão de estoque.

Embora em estágio inicial de desenvolvimento, o sistema já conta com funcionalidades fundamentais para o gerenciamento, com futuras expansões planejadas para incluir login, integração com sistemas externos e categorização de produtos.

Explicação Técnica do Código
Estrutura do Projeto
O código segue uma arquitetura modular para facilitar a escalabilidade e manutenção:

Backend: Desenvolvido com Flask (Python), gerencia as operações do sistema e a comunicação com o banco de dados.
Frontend: Utiliza HTML5, CSS3 e React para a interface do usuário, oferecendo uma experiência responsiva e intuitiva.
Banco de Dados: Implementado com o Cloud Firestore, que armazena informações de produtos e fornecedores de forma segura e acessível.
Funcionalidades Implementadas
Cadastro e Gerenciamento:
Permite o cadastro, edição e exclusão de produtos e fornecedores.
Relatórios:
Gera relatórios básicos de movimentação e estoque em formatos legíveis diretamente na interface.
Como Executar o Projeto
Requisitos:
Python 3.x
Node.js
Gerenciador de pacotes npm ou yarn
Passos para Inicialização:
Clone este repositório.
Instale as dependências do back-end:
bash
Copiar código
pip install -r requirements.txt  
Instale as dependências do front-end:
bash
Copiar código
cd frontend  
npm install  
Configure o arquivo .env com as credenciais do banco de dados.
Inicie o back-end:
bash
Copiar código
flask run  
Inicie o front-end:
bash
Copiar código
npm start  
Acesse o sistema no navegador através de http://localhost:3000.
