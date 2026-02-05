🩺 SafeCare

O SafeCare é uma aplicação web desenvolvida com o objetivo de auxiliar no gerenciamento de cuidados, permitindo o controle de usuários, pacientes, tarefas e notificações.
O sistema é voltado para cuidadores e familiares, oferecendo uma base organizada para acompanhamento de atividades e informações importantes relacionadas ao cuidado.

O projeto está sendo desenvolvido de forma incremental, seguindo a metodologia Scrum, com entregas organizadas por Sprints.

🚀 Tecnologias Utilizadas
Front-end

HTML5

CSS3

JavaScript (Vanilla)

Back-end

Python 3

Flask

Banco de Dados

MySQL 8.0

MySQL Workbench

Integração

MySQL Connector para Python

📋 Pré-requisitos

Antes de executar o projeto, é necessário ter instalado:

Python 3.x (com a opção Add Python to PATH habilitada)

MySQL Server

MySQL Workbench

Git

VS Code (editor recomendado)

📁 Estrutura do Projeto
TIME7/
│
├── models/
│   ├── autorizacao.py
│   ├── notificacao.py
│   ├── paciente.py
│   ├── tarefa.py
│   └── usuario.py
│
├── routes/
│   ├── auth.py
│   ├── notificacoes.py
│   ├── pacientes.py
│   └── tarefas.py
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── cadastro.html
│   ├── home.html
│   ├── pacientes.html
│   ├── tarefas.html
│   └── notificacoes.html
│
├── app.py
├── config.py
├── database.py
├── requirements.txt
├── README.md
└── .gitignore

🗄️ Banco de Dados

O sistema utiliza o banco de dados sistema_cuidados, com as seguintes tabelas principais:

usuario – controle de usuários e autenticação

paciente – cadastro de pacientes vinculados a cuidadores

tarefa – gerenciamento de tarefas e cuidados

notificacao – envio e controle de notificações

As tabelas estão relacionadas por chaves estrangeiras, garantindo integridade referencial.

🔧 Configuração do Banco de Dados

Abra o MySQL Workbench

Crie o banco de dados sistema_cuidados

Execute o script SQL fornecido pelo projeto (dump do banco)

Verifique se o serviço MySQL está ativo

No arquivo database.py, ajuste as credenciais se necessário:

host="localhost"
user="root"
password="root"
database="sistema_cuidados"

▶️ Como Executar o Projeto

Clone o repositório:

git clone <url-do-repositorio>


Acesse a pasta do projeto:

cd TIME7


Instale as dependências:

pip install flask mysql-connector-python


Execute a aplicação:

python app.py


Acesse no navegador:

http://127.0.0.1:5000

📌 Funcionalidades Implementadas (Sprint 1 e 2)
✔ Sprint 1

Estrutura inicial do projeto

Configuração do Flask

Conexão com banco de dados MySQL

Criação das tabelas

Site institucional simples

Tela de login

Tela de cadastro

✔ Sprint 2

Redirecionamento do site institucional:

“Entrar” → Login

“Cadastrar” → Cadastro

Cadastro de usuários funcional

Login de usuários funcional

Validação de credenciais

Tratamento de erros de autenticação

Fluxo completo: cadastro → login → home

Home page com layout base

Menu principal com as funcionalidades previstas do sistema (sem implementação funcional)

🔜 Próximos Passos (Sprints Futuras)

Implementação do CRUD de pacientes

Implementação do CRUD de tarefas

Sistema de notificações

Controle de sessão de usuário

Melhoria no design da interface

Segurança (hash de senhas e proteção de rotas)

👥 Equipe

TIME 7

Artur Lopes de Oliveira

Eduardo Amorim Cerqueira

Natalia Teixeira Silva

Rogerio Maia Lana Moreira

📄 Observações Finais

O SafeCare está em desenvolvimento contínuo e segue boas práticas de organização de código, separação de responsabilidades e integração entre front-end e back-end, servindo como base sólida para expansão futura.
