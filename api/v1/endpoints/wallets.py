"""Wallets routers"""
from datetime import datetime
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from dependencies import get_db
from models.models import Wallet, WalletQuery
from schemas.wallet_schemas import (AddressRequest, WalletInfoResponse,
                                    WalletQueryResponse)
from services.wallet_service import get_wallet

router = APIRouter(prefix='/wallet', tags=['Wallets'])


@router.post("/", response_model=WalletInfoResponse)
async def wallet_info(request: AddressRequest, db: Session = Depends(get_db)):
    """Get wallet information by address"""
    try:
        current_wallet_info = get_wallet(request.address)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e

    timestamp = datetime.now()
    query = select(Wallet).filter(
        Wallet.address == request.address
    ).limit(1)
    wallet_exists = db.execute(query).scalar() is not None
    if not wallet_exists:
        db_wallet = Wallet(
            address=request.address,
            balance_trx=current_wallet_info['balance_trx'],
            bandwidth=current_wallet_info['bandwidth'],
            energy=current_wallet_info['energy']
        )
        db.add(db_wallet)
    db_query = WalletQuery(address=request.address, created_at=timestamp)
    db.add(db_query)
    db.commit()
    db.refresh(db_query)
    if not wallet_exists:
        db.refresh(db_wallet)
    return current_wallet_info


@router.get('/queries', response_model=List[WalletQueryResponse])
async def list_queries(
    skip: int = 0, limit: int = 10, db: Session = Depends(get_db)
):
    """Get a list of queries"""
    queries = db.query(
        WalletQuery
    ).order_by(
        WalletQuery.created_at.desc()
    ).offset(
        skip
    ).limit(
        limit
    ).all()
    return queries
