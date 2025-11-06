from algokit_utils import AlgorandClient, AlgoAmount

# Create one localnet account. Note: This function won't work to create a new
# account on testnet/mainnet
def create_account(algorand: AlgorandClient, name: str, balance_algo: float):
    return algorand.account.from_environment(name, AlgoAmount(algo=balance_algo))