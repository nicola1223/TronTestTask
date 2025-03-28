"""Tron wallet manipulations"""
from tronpy import Tron
from utils.typing import WalletInfo


async def get_wallet(address: str) -> WalletInfo:
    """Get wallet information by address"""
    client = Tron(network='nile')
    if not client.is_address(address):
        raise ValueError("Invalid address format")
    balance_trx = client.get_account_balance(address)
    bandwidth = client.get_bandwidth(address)
    resource = client.get_account_resource(address)
    energy = resource.get('EnergyLimit', 0) - resource.get('EnergyUsed', 0)
    return {
        'address': address,
        'balance_trx': int(balance_trx),
        'bandwidth': bandwidth,
        'energy': energy,
    }
