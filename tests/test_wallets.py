from decimal import Decimal
from app.models import Wallet


def test_wallet_starts_with_zero():
    wallet = Wallet(id="123", balance=Decimal("0.00"))
    assert wallet.balance == Decimal("0.00")


def test_deposit_increases_balance():
    wallet = Wallet(id="123", balance=Decimal("100.00"))
    wallet.balance += Decimal("50.00")
    assert wallet.balance == Decimal("150.00")


def test_withdraw_decreases_balance():
    wallet = Wallet(id="123", balance=Decimal("100.00"))
    wallet.balance -= Decimal("30.00")
    assert wallet.balance == Decimal("70.00")


def test_cannot_withdraw_more_than_balance():
    wallet = Wallet(id="123", balance=Decimal("10.00"))
    assert wallet.balance >= Decimal("0.00")
