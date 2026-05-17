from fastapi import APIRouter, HTTPException, Depends
from decimal import Decimal
from sqlalchemy.orm import Session

# Importamos a conexão e os modelos apontando os caminhos corretos
from app.infra.database import get_db
from app.infra import models

# Criamos o roteador que vai "guardar" as rotas temporariamente
router = APIRouter()

@router.get("/simular-saldo")
async def saldo():
    return {"conta": "12345-6", "saldo": Decimal("1500.50")}

@router.post("/contas/")
async def criar_conta(titular: str, saldo_inicial: Decimal, db: Session = Depends(get_db)):
    nova_conta = models.Conta(titular=titular, saldo=saldo_inicial)
    db.add(nova_conta)
    db.commit()
    db.refresh(nova_conta)
    return nova_conta

@router.get("/saldo/{conta_id}")
async def buscar_saldo(conta_id: int, db: Session = Depends(get_db)):
    conta = db.query(models.Conta).filter(models.Conta.id == conta_id).first()
    if not conta:
        raise HTTPException(status_code=404, detail="Conta não encontrada no Ledger")
    return {
        "id": conta.id,
        "titular": conta.titular,
        "saldo": conta.saldo,
        "mensagem": f"Saudações, {conta.titular}"
    }
