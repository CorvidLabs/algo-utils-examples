"""Tests for account creation and management."""
import pytest
from urllib.error import URLError
from dotenv import load_dotenv
from algokit_utils.config import config
from algokit_utils import AlgorandClient
from algo_utils_examples.accounts import create_account, get_balance
from algo_utils_examples.transaction import payment
import uuid


def test_create_account_and_payment_transaction():
    """Test that we can create an Algorand client and create an account."""
    
    # Given
    
    # Loading environment variables
    load_dotenv()

    # Configure algokit utils
    config.configure(populate_app_call_resources=True)

    # Create Algorand Client on localnet
    algorand = AlgorandClient.default_localnet()

    # Create a new account with initial funding
    # In this case since we don't have the mnemonic in the .env, KMD will make the wallet for us
    try:
        account01 = create_account(algorand, str(uuid.uuid4()), initial_algo=5)
        account02 = create_account(algorand, str(uuid.uuid4()), initial_algo=3)
    except (URLError, ConnectionError, OSError) as e:
        # Skip test if LocalNet is not available
        pytest.skip(f"LocalNet is not available: {e}")

    # When
    
    # Testing simple transactions
    transaction_01 = payment(algorand, account01.address, account02.address,2)
    account02_balance = get_balance(algorand, account02.address)
    
    # Then
    assert account02_balance == 5, "The balance should be 5"
    
    
   
    
    
