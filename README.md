🏥 SafeCare

Cuidado que traz conforto e confiança

O SafeCare é um sistema web desenvolvido para auxiliar cuidadores de idosos ou pessoas dependentes na organização do cuidado diário, permitindo o registro de tarefas, acompanhamento de atividades e compartilhamento de informações básicas com familiares autorizados.

O sistema busca reduzir esquecimentos, retrabalho e sobrecarga do cuidador, além de melhorar a comunicação entre todos os envolvidos no cuidado do paciente.

🚀 Tecnologias Utilizadas

Front-end: HTML5, CSS3

Back-end: Python 3 (Flask)

Banco de Dados: MySQL

Controle de Versão: Git e GitHub

Editor recomendado: VS Code

👥 Público-alvo

Cuidador principal: responsável pelo cadastro de pacientes, tarefas e acompanhamento da rotina.

Familiares: usuários autorizados a visualizar informações básicas do cuidado, sem permissão de edição.

📂 Estrutura do Projeto
SafeCare/
│
├── app.py
├── database.py
├── config.py
├── requirements.txt
│
├── static/
│   └── css/
│       └── style.css
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── cadastro.html
│   └── home.html
│
├── .gitignore
└── README.md

🗄️ Banco de Dados

O sistema utiliza o banco MySQL, com as seguintes tabelas principais:

usuario

paciente

tarefa

notificacao

O banco utilizado é:

sistema_cuidados


📌 Recomenda-se utilizar um usuário próprio do sistema, e não o root.

▶️ Como Executar o Projeto
1️⃣ Clonar o repositório
git clone https://github.com/0000823497-cmd/SafeCare.git
cd SafeCare

2️⃣ Instalar dependências
pip install flask mysql-connector-python

3️⃣ Configurar conexão com o banco

No arquivo database.py, ajuste as credenciais:

host="localhost"
user="safecare_user"
password="safecare123"
database="sistema_cuidados"

4️⃣ Executar o sistema
python app.py


Acesse no navegador:

http://127.0.0.1:5000

🧭 Navegação do Sistema

Index (Site institucional): apresentação do projeto, com botões “Entrar” e “Cadastrar”.

Login: acesso do usuário ao sistema.

Cadastro: criação de conta como cuidador ou familiar.

Home: painel principal com menu das funcionalidades (em evolução).

📌 Organização por Sprints
Sprint 1 (concluída)

Estrutura inicial do projeto

Criação do banco de dados

Site institucional

Telas de login e cadastro

Conexão Flask + MySQL

Tratamento básico de erros e mensagens

Sprint 2 (em andamento)

Navegação completa entre páginas

Cadastro funcional com login

Home page com layout final

Menu com funcionalidades futuras

👨‍👩‍👧‍👦 Equipe

Time 7

Artur Lopes de Oliveira

Eduardo Amorim Cerqueira

Natalia Teixeira Silva

Rogerio Maia Lana Moreira
O SafeCare está em desenvolvimento contínuo e segue boas práticas de organização de código, separação de responsabilidades e integração entre front-end e back-end, servindo como base sólida para expansão futura.
