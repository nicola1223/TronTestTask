"""Wallet pydantic schemas"""
from datetime import datetime

from pydantic import BaseModel, ConfigDict


class WalletQueryResponse(BaseModel):
    """Model for a wallet query response"""
    id: int
    address: str
    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )


class WalletInfoResponse(BaseModel):
    """Model for a wallet information response"""
    address: str
    balance_trx: int
    bandwidth: int
    energy: int

    model_config = ConfigDict(
        from_attributes=True
    )


class AddressRequest(BaseModel):
    """Model for an address request"""
    address: str
