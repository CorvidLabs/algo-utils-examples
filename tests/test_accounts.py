"""Tests for account creation and management."""
import pytest
from algokit_utils import AlgorandClient
from algo_utils_examples.accounts import create_account, get_balance


def test_create_account_and_verify():
    """Test that we can create an Algorand client and create an account."""
    # Create Algorand Client on localnet
    algorand = AlgorandClient.default_localnet()
    
    # Create a new account with initial funding
    account = create_account(algorand, "TEST_ACCOUNT", initial_algo=1000)
    
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

