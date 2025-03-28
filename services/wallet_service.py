"""Tron wallet manipulations"""
from tronpy import Tron

from utils.typing import WalletInfo


def get_wallet(address: str, network: str = 'nile') -> WalletInfo:
    """Get wallet information by address

    :param network: Which network to connect, one of
    ``"mainnet"``, ``"shasta"``, ``"nile"``, or ``"tronex"``
    """
    client = Tron(network=network)
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
