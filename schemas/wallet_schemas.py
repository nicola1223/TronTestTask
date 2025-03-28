"""Wallet pydantic schemas"""
from datetime import datetime

from pydantic import BaseModel


class WalletQueryResponse(BaseModel):
    """Model for a wallet query response"""
    id: int
    address: str
    created_at: datetime

    class Config:
        """Model configuration"""
        from_attributes = True


class WalletInfoResponse(BaseModel):
    """Model for a wallet information response"""
    address: str
    balance_trx: int
    bandwidth: int
    energy: int

    class Config:
        """Model configuration"""
        from_attributes = True


class AddressRequest(BaseModel):
    """Model for an address request"""
    address: str
