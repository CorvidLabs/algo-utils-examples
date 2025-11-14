"""Tests for account creation and management."""
import pytest
from urllib.error import URLError
from dotenv import load_dotenv
from algokit_utils.config import config
from algokit_utils import AlgorandClient
from algo_utils_examples.accounts import create_account, get_balance


def test_create_account_and_verify():
    """Test that we can create an Algorand client and create an account."""
    # Loading environment variables
    load_dotenv()
    
    # Configure algokit utils
    config.configure(populate_app_call_resources=True)
    
    # Create Algorand Client on localnet
    algorand = AlgorandClient.default_localnet()
    
    # Create a new account with initial funding
    # In this case since we don't have the mnemonic in the .env, KMD will make the wallet for us
    try:
        account = create_account(algorand, "TEST_ACCOUNT", initial_algo=1000)
    except (URLError, ConnectionError, OSError) as e:
        # Skip test if LocalNet is not available
        pytest.skip(f"LocalNet is not available: {e}")
    
    # Verify the account was created
    assert account is not None, "Account should not be None"
    assert account.address is not None, "Account should have an address"
    assert len(account.address) > 0, "Account address should not be empty"
    
    # Verify the account has the expected initial balance
    balance = get_balance(algorand, account.address)
    assert balance >= 1000, f"Account should have at least 1000 ALGO, but has {balance}"
    
    # Verify the account has a private key
    assert account.private_key is not None, "Account should have a private key"
    assert len(account.private_key) > 0, "Account private key should not be empty"

