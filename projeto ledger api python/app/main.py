from fastapi import FastAPI
from app.infra.database import engine, Base

# Importa o roteador criado na pasta api
from app.api.v1 import router as api_router

# Cria as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Mantemos apenas o Health Check na raiz por segurança
@app.get("/")
async def home():
    return {"mensagem": "Ledger API Online", "status": "Conectado ao Postgres"}

# O comando mágico que injeta todas as rotas financeiras para dentro do FastAPI
app.include_router(api_router)
