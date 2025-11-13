from pydantic import BaseModel, UUID4, Field, ConfigDict
from  typing import Literal


class OperationRequest(BaseModel):
    operation_type: Literal["DEPOSIT", "WITHDRAW"] = Field(
        description="Тип операции: пополнение или снятие."
    )
    amount: float = Field(gt=0, description="Сумма операции. Должна быть положительной.")


class WalletResponse(BaseModel):
    id: UUID4 = Field(description="Уникальный идентификатор кошелька.")
    balance: float = Field(description="Баланс кошелька.")

    model_config = ConfigDict(from_attributes=True)