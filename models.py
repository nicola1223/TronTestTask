"""Module for creating database models"""

from datetime import datetime
from typing import List

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, relationship

from database import Base


class WalletQuery(Base):
    """
    Wallet queries table model
    """
    __tablename__ = 'wallet_queries'
    id: Mapped[int] = Column(Integer, primary_key=True)
    address: Mapped[str] = Column(
        String, ForeignKey('wallets.address'), nullable=False
    )
    created_at: Mapped[datetime] = Column(
        DateTime, default=datetime.now(), nullable=False
    )
    wallet: Mapped['Wallet'] = relationship(
        back_populates='wallet_queries'

    )

    def __repr__(self) -> str:
        return f'<WalletQuery {self.address}: {self.created_at}>'


class Wallet(Base):
    """
    Wallets table model
    """
    __tablename__ = 'wallets'
    id: Mapped[int] = Column(Integer, primary_key=True)
    address: Mapped[str] = Column(String, nullable=False)
    bandwidth: Mapped[int] = Column(Integer, nullable=False)
    energy: Mapped[int] = Column(Integer, nullable=False)
    wallet_queries: Mapped[List["WalletQuery"]] = relationship(
        back_populates='wallet',
        cascade='all, delete-orphan'
    )

    def __repr__(self) -> str:
        return f'<Wallet {self.address}: '\
               f'Bandwidth: {self.bandwidth} Energy: {self.energy} '\
               f'Queries: {self.wallet_queries}>'
