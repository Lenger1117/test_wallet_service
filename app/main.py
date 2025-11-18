from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from decimal import Decimal
from app.database import SessionLocal
from app.models import Wallet
from app.schemas import OperationRequest, WalletResponse


app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/api/v1/wallets/{wallet_id}", response_model=WalletResponse)
def get_wallet(wallet_id: str, db: Session = Depends(get_db)):
    wallet = db.query(Wallet).filter(Wallet.id == wallet_id).first()
    if not wallet:
        wallet = Wallet(id=wallet_id)
        db.add(wallet)
        db.commit()
        db.refresh(wallet)
    return wallet


@app.post("/api/v1/wallets/{wallet_id}/operation",
          response_model=WalletResponse)
def operate_wallet(
    wallet_id: str,
    operation: OperationRequest,
    db: Session = Depends(get_db)
):
    wallet = db.query(Wallet).filter(Wallet.id == wallet_id).with_for_update().first()
    if not wallet:
        raise HTTPException(status_code=404, detail="Кошелек не найден.")

    amount = Decimal(str(operation.amount))
    if operation.operation_type == "WITHDRAW":
        if wallet.balance < amount:
            raise HTTPException(
                status_code=400,
                detail="Недостаточно средств."
                )
        wallet.balance -= amount
    else:
        wallet.balance += amount

    db.commit()
    db.refresh(wallet)
    return wallet
