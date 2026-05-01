Financial Ledger API
Descrição do Projeto
Desenvolvimento de uma API de alto desempenho para gestão de livro razão (ledger) financeiro, projetada com foco em integridade de dados e arquitetura escalável. O projeto evoluiu de uma simulação em memória para um sistema com persistência real, capaz de processar e armazenar transações bancárias de forma permanente.
Tecnologias e Decisões de Engenharia
O projeto utiliza Python 3.x e FastAPI com suporte nativo a operações assíncronas (Asyncio) para garantir baixa latência. A infraestrutura é sustentada pelo PostgreSQL 15, gerenciado via Docker Compose para assegurar a reprodutibilidade do ambiente. A comunicação entre o código e o banco de dados é feita através do SQLAlchemy (ORM), utilizando a função get_db com o comando yield para uma gestão eficiente de conexões. Para garantir a precisão monetária, essencial em Fintechs, a biblioteca Decimal foi implementada tanto no código quanto no banco de dados (tipo Numeric), eliminando erros de arredondamento. A execução é realizada via servidor Uvicorn com tipagem estrita para maior manutenibilidade.
Funcionalidades Implementadas
O sistema conta com documentação automatizada via Swagger UI para validação de contratos de API. As funcionalidades incluem a criação dinâmica de contas reais, onde cada titular recebe um identificador único e um saldo inicial persistente no disco. Foi mantido um endpoint de consulta de saldos simulados para testes rápidos de contrato, além de um endpoint otimizado para recuperação de estados financeiros reais por identificador de conta. O monitoramento de disponibilidade é garantido por um endpoint de Health Check que verifica o status operacional do serviço.
Guia de Instalação e Execução
Clonagem do Repositório:

git clone https://github.com/alexiskusanagi/portfolio.git
cd ledger-api


Configuração da Infraestrutura (Docker):

docker-compose up -d


Configuração do Ambiente Virtual:

python -m venv .venv
# Ativação no Windows:
.venv\Scripts\activate


Instalação de Dependências:

pip install "fastapi[all]" sqlalchemy psycopg2-binary


Inicialização do Servidor:

uvicorn main:app --reload


Acesso à Interface de Testes:
Acesse http://127.0.0.1:8000/docs para interagir com os endpoints documentados