from algokit_utils import AlgorandClient, AlgoAmount, PaymentParams
from algokit_utils.models import SigningAccount

def payment(algorand: AlgorandClient, sender: SigningAccount, receiver: SigningAccount, amount: float, note: bytes = b""):
    tx = algorand.send.payment(
        PaymentParams(
            sender=sender.address,
            receiver=receiver.address,
            amount=AlgoAmount.from_algo(amount),
            note=note
        )
    )
    print(
        f"\nPay transaction confirmed with TxID: {tx.tx_id}"
        f"\n View the transaction on Lora at https://lora.algokit.io/localnet/transaction/{tx.tx_id}."
    )
    return tx


def group_transaction(algorand: AlgorandClient, payment_params: list[PaymentParams]):
    group_tx_result = algorand.send.new_group()

    for params in payment_params:
        group_tx_result.add_payment(params)

    result = group_tx_result.send()

    print(
        f"\nAtomic group transaction confirmed!"
        f"\nNumber of transaction: {len(payment_params)}"
        f"\nTransaction IDs: {result.tx_ids}"
        f"\nView first transaction on lora at https://lora.algokit.io/localnet/transaction/{result.tx_ids[0]}"
    )
    return result