from sqlalchemy import Column, Integer, String, Numeric
# Mudança aqui: deixando claro a origem do pacote
from app.infra.database import Base

class Conta(Base):
    __tablename__ = "contas"

    id = Column(Integer, primary_key=True, index=True)
    titular = Column(String, nullable=False)
    # Importante: Numeric(10,2) evita erros de arredondamento em centavos
    saldo = Column(Numeric(10, 2), default=0.00)
