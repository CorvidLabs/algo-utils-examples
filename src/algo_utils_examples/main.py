from dotenv import load_dotenv
from algokit_utils.config import config
import logging
from algokit_utils import AlgorandClient, PaymentParams, AlgoAmount
from .accounts import create_account, get_balance
from .transaction import payment, group_transaction

logger = logging.getLogger(__name__)

def main():

    # Loading environment variables
    load_dotenv()

    # Configure Logging
    logging.basicConfig(
        level=logging.DEBUG, format="%(asctime)s %(levelname)-10s: %(message)s"
    )

    # Configure algokit utils
    config.configure(populate_app_call_resources= True)

    # Create Algorand Client on localnet.
    algorand = AlgorandClient.default_localnet()

    # Using the create account function to make two accounts on localnet.
    joao = create_account(algorand, "JOAO", 5000)
    print(
        f"\njoao account {joao.address}"
        f"View it on lora at https://lora.algokit.io/localnet/transaction/{joao.address}"
    )
    jose = create_account(algorand, "JOSE", 10000)
    print(
        f"jose account {jose.address}"
        f"View it on lora at https://lora.algokit.io/localnet/transaction/{jose.address}"
    )

    # Making a test payment from jose to joao of 25 algos.
    tx = payment(algorand, jose, joao, 25, "Test transaction")

    # Setting parameters for an atomic group transaction (2 payments)
    params = [
        PaymentParams(
            sender=joao.address,
            receiver=jose.address,
            amount=AlgoAmount.from_algo(50),
            note=b"Test atomic  tx",
        ),
        PaymentParams(
            sender=jose.address,
            receiver=joao.address,
            amount=AlgoAmount.from_algo(75),
            note=b"Test atomic tx b"
        )
    ]

    # Executing the atomic group transaction (all succeed or all fail together)
    result = group_transaction(algorand, params)
    
    # Check the balance on the accounts
    joao_balance = get_balance(algorand,joao.address)
    jose_balance = get_balance(algorand, jose.address)
    print(
        f"\nJoão account balance: {joao_balance}"
        f"\nJosé account balance: {jose_balance}"
    )
    
if __name__ == "__main__":
    main()
