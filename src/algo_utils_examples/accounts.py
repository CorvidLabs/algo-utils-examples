from algokit_utils import AlgorandClient, AlgoAmount, SigningAccount
from algosdk import mnemonic
from decimal import Decimal


def create_account(algorand: AlgorandClient, name: str, initial_algo: int = 0) -> SigningAccount:
    """
    Load a localnet/testnet/mainnet account from environment variables using mnemonic. 
    In the LocalNet, if no account is found on .env one will be created and funded using KMD.
    
    :param algorand: Algorand Client Instance.
    :param name: Local identifier of the account, ex: Joao, in the .env would be JOAO_MNEMONIC="25 WORDS MNEMONIC".
    :param initial_algo: Initial algo balance of localnet. On Testnet/Mainnet the initial balance is 0.
    :return: The object representing the account.
    """
    return algorand.account.from_environment(name, AlgoAmount.from_algo(initial_algo))


def get_balance(algorand: AlgorandClient, account: SigningAccount | str) -> Decimal:
    """
    Get the balance in algos of an account.
    :param algorand: Algorand Client Instance.
    :param account: The address of the account. (SigningAccount or str)
    :return: The balance in algo.
    """
    address = account.address if isinstance(account, SigningAccount) else account
    account_info = algorand.account.get_information(address)
    return account_info.amount.algo


def create_testnet_account(algorand: AlgorandClient) -> SigningAccount:
    """
    Create a new random account.
    :param algorand: Algorand Client Instance.
    :return: A SigningAccount object.
    """
    return algorand.account.random()


def get_mnemonic_from_private_key(private_key_base_64: str) -> str:
    """
    Get the mnemonic of an account from the private key.
    :param private_key_base_64: the private key in base 64 format. ex: joao.private_key
    :return: The mnemonic phrase for the private key.
    """
    return mnemonic.from_private_key(private_key_base_64)


def get_account_from_mnemonic(algorand: AlgorandClient, mnemonic_phrase: str) -> SigningAccount:
    """
    Get a SigningAccount object for an account.
    :param algorand: Algorand Client Instance.
    :param mnemonic_phrase: The mnemonic phrase.
    :return: A SigningAccount object recovered from the mnemonic phrase.
    """
    return algorand.account.from_mnemonic(mnemonic=mnemonic_phrase)

