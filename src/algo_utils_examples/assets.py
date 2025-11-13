from algokit_utils import (AlgorandClient, AssetOptInParams, AssetOptOutParams, AssetCreateParams, AssetTransferParams,
                           SigningAccount, SendSingleTransactionResult)
from typing import Optional


def create_asset(
        algorand: AlgorandClient,
        sender: SigningAccount | str,
        name: str,
        unit_name: str,
        total: int,
        decimals: int = 0,
        frozen: bool = False,
        manager: Optional[str] = None,
        reserve: Optional[str] = None,
        freeze: Optional[str] = None,
        clawback: Optional[str] = None,
        url: str = "",
        note: bytes = b""
) -> int:
    """
    Create an asset on the blockchain.
    :param algorand: Algorand Instance Client.
    :param sender: The creator address. (SigningAccount or string)
    :param name: Full name of the asset. Ex: Blue Sun Coins
    :param unit_name: Shorter name of the asset. Ex: BSC
    :param total: Total supply of the asset. Ex: 1_000_000_000_000 - 1 Trillion supply.
    :param decimals: Number of decimals the asset has. Ex: 1_000_000_000_000 asset with 2 decimals shows to the user: 10_000_000_000.00
    :param frozen: True or false value to determine if the asset can be freely moved. Ex: a user can send or not the asset.
    :param manager: The address that can set the reserve, freeze, clawback address. If none defaults to sender.
    :param reserve: The address that holds the uncirculated supply. If none defaults to sender.
    :param freeze: The address that can freeze the asset in any account. If none defaults to sender.
    :param clawback: The address that can clawback the asset from any account. If none defaults to sender.
    :param url: The metadata URL of the asset.
    :param note: A metadata message in the creation of the asset. Optional.
    :return: The asset ID.
    """
    sender_address = sender.address if isinstance(sender, SigningAccount) else sender
    create_asset_result = algorand.send.asset_create(
        AssetCreateParams(
            sender=sender_address,
            asset_name=name,
            unit_name=unit_name,
            total=total,
            decimals=decimals,
            default_frozen=frozen,
            manager=manager or sender_address,
            reserve=reserve or sender_address,
            freeze=freeze or sender_address,
            clawback=clawback or sender_address,
            url=url,
            note=note
        )
    )
    result = create_asset_result.asset_id
    return result


def opt_in(
        algorand: AlgorandClient, 
        account: SigningAccount | str, 
        asset_id: int
) -> SendSingleTransactionResult:
    """
    Send an opt-in transaction request.
    :param algorand: Algorand Client Instance.
    :param account: The address that wants to opt-in. (SigningAccount or string)
    :param asset_id: The id of the asset to opt in to.
    :return: The result of the transaction.
    """
    account_address = account.address if isinstance(account, SigningAccount) else account
    opt_in_result = algorand.send.asset_opt_in(
        AssetOptInParams(
            sender=account_address,
            asset_id=asset_id
        )
    )
    return opt_in_result


def opt_out(
        algorand: AlgorandClient,
        account: SigningAccount | str,
        creator: SigningAccount | str,
        asset_id: int
) -> SendSingleTransactionResult:
    """
    Send an opt-out transaction request removing the asset from the account. (balance must be zero)
    :param algorand: Algorand Client Instance.
    :param account: The address that wants to opt out. (SigningAccount or string)
    :param creator: The address of the account that created the asset. (SigningAccount or string)
    :param asset_id: The id of the asset.
    :return: The result of the transaction.
    """
    account_address = account.address if isinstance(account, SigningAccount) else account
    creator_address = creator.address if isinstance(creator, SigningAccount) else creator
    opt_out_result = algorand.send.asset_opt_out(
        AssetOptOutParams(
            sender=account_address,
            creator=creator_address,
            asset_id=asset_id
        )
    )
    return opt_out_result


def assets_transfer(
        algorand: AlgorandClient,
        sender: SigningAccount | str,
        receiver: SigningAccount | str,
        asset_id: int, 
        amount: int, 
        note: bytes = b""
) -> SendSingleTransactionResult:
    """
    Send an asset transfer transaction request.
    :param algorand: Algorand Instance Client.
    :param sender: Address of who is sending the asset. (SigningAccount or string)
    :param receiver: Address of who is receiving the asset. (SigningAccount or string)
    :param asset_id: ID of the asset to transfer.
    :param amount: Quantity to transfer in base units. (considering decimals).
    :param note: Optional metadata note.
    :return: The result of the transaction.
    """
    sender_address = sender.address if isinstance(sender, SigningAccount) else sender
    receiver_address = receiver.address if isinstance(receiver, SigningAccount) else receiver
    send_asset_result = algorand.send.asset_transfer(
        AssetTransferParams(
            sender=sender_address,
            receiver=receiver_address,
            asset_id=asset_id,
            amount=amount,
            note=note
        ) 
    )
    return send_asset_result


def get_asset_balance(algorand: AlgorandClient, account: SigningAccount | str, asset_id: int) -> int:
    """
    Get the balance of an asset.
    :param algorand: Algorand Instance Client.
    :param account: The address of the account that has the asset. (SigningAccount or string)
    :param asset_id: The ID of the asset being checked.
    :return: The number of assets the account has with that ID. Returns 0 if the account did not opt in.
    """
    account_address = account.address if isinstance(account, SigningAccount) else account
    account_info = algorand.account.get_information(account_address)
    for asset in account_info.assets:
        if asset['asset-id'] == asset_id:
            return asset['amount']
    return 0

