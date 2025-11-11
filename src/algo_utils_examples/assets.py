from algokit_utils import AlgorandClient, AssetOptInParams, AssetCreateParams, AssetTransferParams
from typing import Optional


def create_asset(
        algorand: AlgorandClient,
        sender: str,
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

    create_asset_result = algorand.send.asset_create(
        AssetCreateParams(
            sender=sender,
            asset_name=name,
            unit_name=unit_name,
            total=total,
            decimals=decimals,
            default_frozen=frozen,
            manager=manager or sender,
            reserve=reserve or sender,
            freeze=freeze or sender,
            clawback=clawback or sender,
            url=url,
            note=note
        )
    )
    result = create_asset_result.asset_id
    print(
        f"\nAsset ID {result} create transaction confirmed with TxnID: {create_asset_result.tx_id}."
    )
    print(
        f"\nView it on Lora at https://lora.algokit.io/localnet/asset/{result}."
    )

    return result

def opt_in(algorand: AlgorandClient, account: str, asset_id: int):
    opt_in_result = algorand.send.asset_opt_in(
        AssetOptInParams(
            sender=account,
            asset_id=asset_id
        )
    )
    print(
        f"\nAsset opt-in transaction confirmed with TxnID: {opt_in_result.tx_id}. \nView it on Lora at https://lora.algokit.io/localnet/transaction/{opt_in_result.tx_id}."
    )

    return opt_in_result

def assets_transfer(algorand: AlgorandClient,
                    sender: str, 
                    receiver: str, 
                    asset_id: int, 
                    amount: int, 
                    note: bytes = b""):
    
    send_asset_result = algorand.send.asset_transfer(
        AssetTransferParams(
            sender=sender,
            receiver=receiver,
            asset_id=asset_id,
            amount=amount,
            note=note
        ) 
    )
    print(
        f"\nAsset transfer transaction confirmed with TxnID: {send_asset_result.tx_id}. \nView it on Lora at https://lora.algokit.io/localnet/transaction/{send_asset_result.tx_id}."
    )
    
    return send_asset_result