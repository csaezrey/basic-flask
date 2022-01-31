import pytest
from wallet.model import Wallet, create_wallet, read_wallet, update_wallet, delete_wallet

@pytest.fixture
def wallet():
    return Wallet(
        owner_id=14,
        amount=0
    )

@pytest.mark.parametrize(
    "owner_id,amount",
    [
        (1,1000),
        (2,2000)
    ]
)
def test_create_wallet(owner_id, amount):
    wallet = create_wallet(owner_id, amount)
    assert wallet.id is not None


def test_update_wallet(wallet):
    wallet=create_wallet(wallet.owner_id, wallet.amount)
    update_wallet(wallet.id,3000)
    assert wallet.amount == 3000