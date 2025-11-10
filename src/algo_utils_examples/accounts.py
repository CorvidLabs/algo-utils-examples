from algokit_utils import AlgorandClient, AlgoAmount


# Create one localnet account. Note: This function won't work to create a new
# account on testnet/mainnet
def create_account(algorand: AlgorandClient, name: str, balance_algo: float):
    return algorand.account.from_environment(name, AlgoAmount(algo=balance_algo))


# Get the balance of an account in Algos.
def get_balance(algorand: AlgorandClient, address: str):
    account_info = algorand.account.get_information(address)
    return account_info.amount.algo


def create_testnet_account(algorand: AlgorandClient):
    account = algorand.account.random()
    print(f"Account address: {account.address}")
    print(f"SAVE THIS MNEMONIC SECURELY - You'll need it to recover this account!")
    print(f"Account mnemonic: {account.private_key}")
    print(f"Fund this account at: https://bank.testnet.algorand.network/")
    
    return account