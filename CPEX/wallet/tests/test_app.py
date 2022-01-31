import pytest
from wallet.model import Wallet, create_wallet, read_wallet, update_wallet, delete_wallet

OWNER = 14
AMOUNT = 0

@pytest.fixture
def wallet():
    return Wallet(
        owner_id=OWNER,
        amount=AMOUNT
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

def test_delete_wallet(wallet):
    wallet=create_wallet(wallet.owner_id, wallet.amount)
    result = delete_wallet(wallet.id)
    assert result

def test_read_wallet(wallet):
    wallet=create_wallet(wallet.owner_id, wallet.amount)
    wallet=read_wallet(wallet.id)
    assert (wallet.owner_id == OWNER and wallet.amount == AMOUNT)