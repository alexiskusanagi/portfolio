english version.
Integrative Project – Administrative Web System
This project was developed as part of the Vocational Course in Application Development (Senac, Brazil 2025). 
It is a complete web system, with real functionalities for registration, authentication, service management, and scheduling, 
aimed at administrative and institutional environments.

Features
Registration and management of clients, employees, and services

Employee login and logout with session control

Scheduling, modification, and cancellation of services via backoffice

Sales control and service status tracking

Navigation through specific areas (client, backoffice, recreation, nursery)

Interface with HTML, CSS, icons, and customized images

Database integration via PHP and SQL

Technologies Used
PHP for server-side logic

HTML/CSS for page structure and styling

JavaScript (light use) for basic interactions

SQL for data persistence

XAMPP as the local development environment

Git and GitHub for version control and collaboration

Project Structure
Código
portfolio/
├── areacliente/                  # Client-facing interface
├── css/, icons/, img/            # Styles and visual assets
├── utils/, ode/                  # Auxiliary folders
├── login_funcionario.php          # Employee authentication
├── logout_funcionario.php         # Session termination
├── cliente_lista.php              # Client listing
├── cliente_altera.php             # Client update
├── cadastra_cliente_backoffice.php# Client registration (backoffice)
├── funcionario_lista.php          # Employee listing
├── funcionario_cadastra.php       # Employee registration
├── funcionario_altera.php         # Employee update
├── servico_lista.php              # Service listing
├── servico_cadastra.php           # Service registration
├── servico_altera.php             # Service update
├── agendamento_altera_backoffice.php # Appointment update
├── agendamento_cancela_backoffice.php# Appointment cancellation
├── ver_agenda.php                 # Agenda visualization
├── vendas.php                     # Sales control
├── venda_status.php               # Sales status
├── bercarios.php, quartos_criancas.php # Nursery and children’s rooms
├── recreacao.php, salas_recreacao.php  # Recreation areas
├── backoffice_Kinder_Haus.php, estrutura_kinder_haus.php # Institutional structure
└── sobre.php, index.php           # Institutional pages
How to Run
Clone the repository:

bash
git clone https://github.com/alexiskusanagi/portfolio.git
Install XAMPP and move the portfolio folder to the htdocs directory.

Import the database (.sql file, if available).

Access via browser:

Código
http://localhost/portfolio/index.php
Author
Alexis Kusanagi Developer transitioning into the technology field, with vocational training and practical school experience in web projects. 
Fluent in English, with strong communication skills and a focus on continuous learning.

Contact
GitHub: alexiskusanagi

E-mail: alexiskusanagi

🇧🇷 Versão em Português
Projeto Integrador – Sistema Web Administrativo
Este projeto foi desenvolvido como parte do curso técnico de Desenvolvimento de Aplicativos (Senac, Brasil 2025). Trata-se de um sistema web completo, 
com funcionalidades reais de cadastro, autenticação, controle de serviços e agendamentos, voltado para ambientes administrativos e institucionais.

Funcionalidades
Cadastro e gerenciamento de clientes, funcionários e serviços

Login e logout de funcionários com controle de sessão

Agendamento, alteração e cancelamento de serviços via backoffice

Controle de vendas e acompanhamento de status

Navegação por áreas específicas (cliente, backoffice, recreação, berçário)

Interface com HTML, CSS, ícones e imagens customizadas

Integração com banco de dados via PHP e SQL

Tecnologias utilizadas
PHP para lógica de servidor

HTML/CSS para estrutura e estilo das páginas

JavaScript (uso leve) para interações básicas

SQL para persistência de dados

XAMPP como ambiente de desenvolvimento local

Git e GitHub para versionamento e colaboração

Estrutura do projeto
Código
portfolio/
├── areacliente/                  # Interface voltada ao cliente
├── css/, icons/, img/            # Estilos e recursos visuais
├── utils/, ode/                  # Pastas auxiliares
├── login_funcionario.php          # Autenticação de funcionários
├── logout_funcionario.php         # Encerramento de sessão
├── cliente_lista.php              # Listagem de clientes
├── cliente_altera.php             # Alteração de clientes
├── cadastra_cliente_backoffice.php# Cadastro de clientes (backoffice)
├── funcionario_lista.php          # Listagem de funcionários
├── funcionario_cadastra.php       # Cadastro de funcionários
├── funcionario_altera.php         # Alteração de funcionários
├── servico_lista.php              # Listagem de serviços
├── servico_cadastra.php           # Cadastro de serviços
├── servico_altera.php             # Alteração de serviços
├── agendamento_altera_backoffice.php # Alteração de agendamentos
├── agendamento_cancela_backoffice.php# Cancelamento de agendamentos
├── ver_agenda.php                 # Visualização da agenda
├── vendas.php                     # Controle de vendas
├── venda_status.php               # Status de vendas
├── bercarios.php, quartos_criancas.php # Berçários e quartos de crianças
├── recreacao.php, salas_recreacao.php  # Áreas de recreação
├── backoffice_Kinder_Haus.php, estrutura_kinder_haus.php # Estrutura institucional
└── sobre.php, index.php           # Páginas institucionais
Como executar
Clone o repositório:

bash
git clone https://github.com/alexiskusanagi/portfolio.git
Instale o XAMPP e mova a pasta portfolio para o diretório htdocs.

Importe o banco de dados (arquivo .sql, se disponível).

Acesse via navegador:

Código
http://localhost/portfolio/index.php
Autor
Alexis Kusanagi Desenvolvedor em transição para a área de tecnologia, com formação técnica e experiência prática em projetos web. Fluente em inglês, com forte comunicação e foco em aprendizado contínuo.

Contato
GitHub: alexiskusanagi

E-mail: alexiskusanagi
