import pytest
from algokit_utils import SigningAccount, SendSingleTransactionResult
from algokit_utils.algorand import AlgorandClient
from algokit_utils.models.amount import AlgoAmount
from algo_utils_examples.assets import create_asset, opt_in, opt_out, assets_transfer, get_asset_balance

@pytest.fixture
def algorand() -> AlgorandClient:
    """Get an AlgorandClient instance configured for LocalNet"""
    return AlgorandClient.default_localnet()


@pytest.fixture
def funded_account_01(algorand: AlgorandClient) -> SigningAccount:
    """Create and fund a test account with ALGOs"""
    new_account = algorand.account.random()
    dispenser = algorand.account.localnet_dispenser()
    algorand.account.ensure_funded(
        new_account,
        dispenser,
        min_spending_balance=AlgoAmount.from_algo(100),
        min_funding_increment=AlgoAmount.from_algo(1)
    )
    algorand.set_signer(sender=new_account.address, signer=new_account.signer)
    return new_account


@pytest.fixture
def funded_account_02(algorand: AlgorandClient) -> SigningAccount:
    """Create and fund a test account with ALGOs"""
    new_account = algorand.account.random()
    dispenser = algorand.account.localnet_dispenser()
    algorand.account.ensure_funded(
        new_account,
        dispenser,
        min_spending_balance=AlgoAmount.from_algo(100),
        min_funding_increment=AlgoAmount.from_algo(1)
    )
    algorand.set_signer(sender=new_account.address, signer=new_account.signer)
    return new_account

@pytest.fixture()
def asset_id(algorand: AlgorandClient, funded_account_01: SigningAccount) -> int:
    asset_id = create_asset(
        algorand,
        funded_account_01.address,
        "Buuh",
        "BH",
        1_000_000,
        1,
    )
    return asset_id

def test_create_asset(asset_id) -> None:
    assert isinstance(asset_id, int)
    assert asset_id > 0


def test_asset_transfer_workflow(
        algorand: AlgorandClient,
        funded_account_01: SigningAccount,
        funded_account_02: SigningAccount,
        asset_id: int
) -> None:

    #Opt-in
    opt_in_result = opt_in(algorand, funded_account_02.address, asset_id)
    assert opt_in_result.tx_id is not None

    #Transfer
    transfer_result = assets_transfer(
        algorand,
        funded_account_01.address,
        funded_account_02.address,
        asset_id,
        50
    )
    assert transfer_result.tx_id is not None

    #Checking balance
    balance = get_asset_balance(algorand, funded_account_02.address, asset_id)
    assert balance == 50

    
def test_asset_opt_out_workflow(
        algorand: AlgorandClient,
        funded_account_01: SigningAccount,
        funded_account_02: SigningAccount,
        asset_id: int
) -> None:

    #Opt-in
    opt_in_result = opt_in(algorand, funded_account_02.address, asset_id)
    assert opt_in_result.tx_id is not None
    
    #Opt-out
    opt_out_result = opt_out(
        algorand,
        funded_account_02.address,
        funded_account_01.address,
        asset_id
    )
    assert opt_out_result.tx_id is not None
    
