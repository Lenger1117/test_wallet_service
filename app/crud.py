from sqlalchemy.orm import Session
from . import models


def get_wallet_for_update(db: Session, wallet_id: str):
    """Поиск кошелька по ID."""
    return db.query(models.Wallet).filter(models.Wallet.id==wallet_id).with_for_update().first()