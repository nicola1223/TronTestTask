"""Typing for application"""
from typing import TypedDict


class WalletInfo(TypedDict):
    """
    Wallet information
    """
    address = str
    balance_trx: int
    bandwidth: int
    energy: int
