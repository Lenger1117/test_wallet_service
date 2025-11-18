from sqlalchemy import Numeric
from sqlalchemy.orm import Mapped, mapped_column
from decimal import Decimal
from .database import Base
from uuid import UUID, uuid4

class Wallet(Base):
    __tablename__ = "wallets"
    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    balance: Mapped[Decimal] = mapped_column(Numeric(20, 2), nullable=False, default=Decimal("0.00"))