from dotenv import load_dotenv
from algokit_utils.config import config
import logging
import os
from algokit_utils import AlgorandClient, PaymentParams, AlgoAmount
from .accounts import create_account, get_balance, get_mnemonic_from_private_key, get_account_from_mnemonic
from .transaction import payment, group_transaction
from .assets import create_asset, opt_in, assets_transfer, opt_out, get_asset_balance

logger = logging.getLogger(__name__)


def main():
    # Loading environment variables
    load_dotenv()

    # Configure Logging
    logging.basicConfig(
        level=logging.DEBUG, format="%(asctime)s %(levelname)-10s: %(message)s"
    )

    # Configure algokit utils
    config.configure(populate_app_call_resources=True)

    # Create Algorand Client on localnet.
    algorand = AlgorandClient.default_localnet()

    # Testing the account creation.
    # In this case since I have the mnemonic phrases in the .env I did not set any  AlgoAmount
    # And instead of creating its loading the accounts I previously made.
    # In Sara and Lira cases, I don't have the mnemonics in the .ENV so KMD will make the wallets for me.
    joao = create_account(algorand, "JOAO")
    jose = create_account(algorand, "JOSE")
    sara = create_account(algorand, "SARA", 1000)
    lira = create_account(algorand, "LIRA", 5000)

    print(f"\nJoão account address: {joao.address}")
    print(f"\nJosé account address: {jose.address}")
    print(f"\nSara account address: {sara.address}")
    print(f"\nLira account address: {lira.address}")
    print(f"View João account on lora at: https://lora.algokit.io/localnet/account/{joao.address}")
    print(f"View José account on lora at: https://lora.algokit.io/localnet/account/{jose.address}")
    print(f"View Sara account on lora at: https://lora.algokit.io/localnet/account/{sara.address}")
    print(f"View Lira account on lora at: https://lora.algokit.io/localnet/account/{lira.address}")

    # Time to get the mnemonics of the two new accounts.
    sara_mnemonic = get_mnemonic_from_private_key(sara.private_key)
    lira_mnemonic = get_mnemonic_from_private_key(lira.private_key)

    print("\nNEVER SHARE THESE PHRASES! Save them in the .env or somewhere safer if you want to reuse the accounts.")
    print(f"\nSara mnemonic phrase: {sara_mnemonic}")
    print(f"\nLira mnemonic phrase: {lira_mnemonic}")

    # Getting the account address using the mnemonic. This is more for demonstration purposes, you usually will get the address loading
    # the account and then using account.address
    jose_address = get_account_from_mnemonic(algorand, os.getenv("JOSE_MNEMONIC"))

    # Don't forget to use .address, or you will expose the private key and with that someone can get the mnemonic phrase leading
    # to control of the account
    print(f"\nJosé address from the mnemonic phrase: {jose_address.address}")

    #Getting the balance off all accounts before the transactions.
    joao_balance = get_balance(algorand, joao.address)
    jose_balance = get_balance(algorand, jose.address)
    sara_balance = get_balance(algorand, sara.address)
    lira_balance = get_balance(algorand, lira.address)

    print(f"João account balance: {joao_balance}")
    print(f"José account balance: {jose_balance}")
    print(f"Sara account balance: {sara_balance}")
    print(f"Lira account balance: {lira_balance}")

    # Transaction tests.
    payment_01 = payment(algorand, sara, lira, 2, b"First payment test")
    payment_02 = payment(algorand, jose, joao, 0.5, b"Second payment test")
    payment_03 = payment(algorand, lira.address, jose.address, 3, b"Third payment test")
    payment_04 = payment(algorand, sara.address, joao.address, 0.7, b"Last payment test")

    print(f"\nSee all payments results below")
    print(f"First payment from Sara to Lira: https://lora.algokit.io/localnet/transaction/{payment_01.tx_id}")
    print(f"Second payment from José to João: https://lora.algokit.io/localnet/transaction/{payment_02.tx_id}")
    print(f"Third payment from Lira to José: https://lora.algokit.io/localnet/transaction/{payment_03.tx_id}")
    print(f"Last payment from Sara to João: https://lora.algokit.io/localnet/transaction/{payment_04.tx_id}")
    print(f"\n")

    # Getting the balance off all accounts after the transactions to see the differences.
    joao_balance = get_balance(algorand, joao)
    jose_balance = get_balance(algorand, jose)
    sara_balance = get_balance(algorand, sara)
    lira_balance = get_balance(algorand, lira)

    print(f"João account balance: {joao_balance}")
    print(f"José account balance: {jose_balance}")
    print(f"Sara account balance: {sara_balance}")
    print(f"Lira account balance: {lira_balance}")
    print(f"\n")

    # Let's create some assets now.
    jose_asset = create_asset(
        algorand,
        jose,
        "Buh",
        "BH",
        1_000_000,
        2,
    )

    sara_asset = create_asset(
        algorand,
        sara.address,
        "Bah",
        "BA",
        1_000_000_000,
        1,
        False,
        sara.address,
        sara.address,
        sara.address,
        sara.address,
    )

    print(f"José asset ID {jose_asset}")
    print(f"Sara asset ID {sara_asset}")
    print(f"View it at https://lora.algokit.io/localnet/asset/{jose_asset}")
    print(f"View it at https://lora.algokit.io/localnet/asset/{sara_asset}")
    print(f"\n")

    # Now let's do some asset transactions starting with opt in into the assets we created.

    lira_opt_in_sara_asset = opt_in(algorand, lira.address, sara_asset)
    lira_opt_in_jose_asset = opt_in(algorand, lira.address, jose_asset)
    joao_opt_in_jose_asset = opt_in(algorand, joao.address, jose_asset)
    joao_opt_in_sara_asset = opt_in(algorand, joao.address, sara_asset)

    print(f"Lira opt in results confirmed with txIDs: {lira_opt_in_sara_asset.tx_id} and {lira_opt_in_jose_asset.tx_id}")
    print(f"João opt in results confirmed with txIDs: {joao_opt_in_jose_asset.tx_id} and {joao_opt_in_sara_asset.tx_id}")
    print(f"\nView them at:"
          f"\nhttps://lora.algokit.io/localnet/transaction/{lira_opt_in_sara_asset.tx_id}"
          f"\nhttps://lora.algokit.io/localnet/transaction/{lira_opt_in_jose_asset.tx_id}"
          f"\nhttps://lora.algokit.io/localnet/transaction/{joao_opt_in_jose_asset.tx_id}"
          f"\nhttps://lora.algokit.io/localnet/transaction/{joao_opt_in_sara_asset.tx_id}")
    print(f"\n")
    
    # Now some asset transfer
    jose_asset_transfer_01 = assets_transfer(algorand, jose.address, joao.address, jose_asset,10_00, b"First ASA transfer")
    jose_asset_transfer_02 = assets_transfer(algorand, jose.address, lira.address, jose_asset, 100_00)
    sara_asset_transfer_01 = assets_transfer(algorand, sara.address, lira.address, sara_asset, 10000_0, b"TY!")
    sara_asset_transfer_02 = assets_transfer(algorand, sara.address, joao.address, sara_asset, 50000_0, b"TY!")
    
    print(f"José first asset transfer confirmed with txID: {jose_asset_transfer_01.tx_id}")
    print(f"José second asset transfer confirmed with txID: {jose_asset_transfer_02.tx_id}")
    print(f"Sara first asset transfer confirmed with txID: {sara_asset_transfer_01.tx_id}")
    print(f"Sara second asset transfer confirmed with txID: {sara_asset_transfer_02.tx_id}")
    print(f"\nView them at:"
          f"\nhttps://lora.algokit.io/localnet/transaction/{jose_asset_transfer_01.tx_id}"
          f"\nhttps://lora.algokit.io/localnet/transaction/{jose_asset_transfer_02.tx_id}"
          f"\nhttps://lora.algokit.io/localnet/transaction/{sara_asset_transfer_01.tx_id}"
          f"\nhttps://lora.algokit.io/localnet/transaction/{sara_asset_transfer_02.tx_id}")
    print(f"\n")

    #Now lets get the asset balance of the accounts.
    joao_asset_balance_sara_asset = get_asset_balance(algorand, joao.address, sara_asset)
    joao_asset_balance_jose_asset = get_asset_balance(algorand, joao.address, jose_asset)
    lira_asset_balance_sara_asset = get_asset_balance(algorand, lira.address, sara_asset)
    lira_asset_balance_jose_asset = get_asset_balance(algorand, lira.address, jose_asset)
    print(f"Joao has {joao_asset_balance_sara_asset} of Sarah asset.")
    print(f"Joao has {joao_asset_balance_jose_asset} of José asset.")
    print(f"Lira has {lira_asset_balance_sara_asset} of Sarah asset.")
    print(f"Lira has {lira_asset_balance_jose_asset} of José asset.")
    print(f"\n")

    # Let's opt out Lira of one asset. To do that we need to ensure Lira has zero amount of that asset.
    # Let's send back Sarah asset.
    lira_asset_transfer = assets_transfer(algorand, lira.address, sara.address, sara_asset, lira_asset_balance_sara_asset)
    lira_opt_out_sara_asset = opt_out(algorand, lira.address, sara.address, sara_asset)
    print(f"Lira transfer all of Sara assets back to her: {lira_asset_transfer.tx_id}")
    print(f"Lira opt out txID: {lira_opt_out_sara_asset.tx_id}")
    print(f"View it at https://lora.algokit.io/localnet/transaction/{lira_opt_out_sara_asset.tx_id}")
    print(f"\n")

    #Now some payment atomic transaction. Note: Atomic Transaction is way more powerful than what showed here!
    payment_params= [
        PaymentParams(
            sender=lira.address,
            receiver=sara.address,
            amount=AlgoAmount.from_algo(100)
        ),
        PaymentParams(
            sender=sara.address,
            receiver=jose.address,
            amount=AlgoAmount.from_algo(50)
        )
    ]
    atomic_transaction = group_transaction(algorand, payment_params)
    print(f"Atomic transaction confirmed with group txID: {atomic_transaction.group_id}")
    print(f"View the first transaction at  https://lora.algokit.io/localnet/transaction/{atomic_transaction.tx_ids[0]}")


if __name__ == "__main__":
    main()

