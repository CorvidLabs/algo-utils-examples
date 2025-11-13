from algokit_utils import AlgorandClient, AlgoAmount, PaymentParams, SendAtomicTransactionComposerResults, SendSingleTransactionResult
from algokit_utils.models import SigningAccount


def payment(
        algorand: AlgorandClient, 
        sender: SigningAccount | str, 
        receiver: SigningAccount | str, 
        algo: float,
        note: bytes = b""
) -> SendSingleTransactionResult:
    """
    Send a payment transaction.
    :param algorand: Algorand Client Instance.
    :param sender: The sender address. SigningAccount or address string.
    :param receiver: The receiver address. SigningAccount or address string.
    :param algo: The amount of algo. Automatically converted to microAlgos.
    :param note: An optional note.
    :return: An object with the result of the transaction.
    """
    sender_address = sender.address if isinstance(sender, SigningAccount) else sender
    receiver_address = receiver.address if isinstance(receiver, SigningAccount) else receiver
    micro_algo = int(algo * 1_000_000)
    transaction = algorand.send.payment(
        PaymentParams(
            sender=sender_address,
            receiver=receiver_address,
            amount=AlgoAmount.from_micro_algo(micro_algo),
            note=note
        )
    )
    return transaction


def group_transaction(
        algorand: AlgorandClient, 
        payment_params: list[PaymentParams]
) -> SendAtomicTransactionComposerResults:
    """
    Execute an atomic group transaction on the blockchain. They all succeed or fail together.
    :param algorand: Algorand Instance client.
    :param payment_params: The list of parameters of each transaction.
    :return: The result of the transaction.
    """
    group_tx_result = algorand.send.new_group()
    for params in payment_params:
        group_tx_result.add_payment(params)
    result = group_tx_result.send()
    return result

