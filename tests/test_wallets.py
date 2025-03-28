"""Tests for application"""
from datetime import datetime

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker

from core.database import Base
from dependencies import get_db
from main import app
from models.models import Wallet, WalletQuery

SQLALCHEMY_DATABASE_URL = 'sqlite:///./test_db.sqlite3'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
)

TestingSessionLocal = sessionmaker(engine)


def override_get_db():
    """Override get_db"""
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


@pytest.fixture
def test_db():
    """Provide a test database session"""
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


def test_queries(test_db):
    """Unit test for queries"""
    with TestingSessionLocal() as db:
        wallet = Wallet(
            address='test_address',
            balance_trx=100,
            bandwidth=50,
            energy=20
        )
        query = WalletQuery(
            address='test_address',
            created_at=datetime.now()
        )

        db.add(wallet)
        db.add(query)
        db.commit()

        saved_wallet_query = select(Wallet).limit(1)
        saved_query_query = select(WalletQuery).limit(1)

        saved_wallet = db.execute(saved_wallet_query).scalar()
        saved_query = db.execute(saved_query_query).scalar()

        assert saved_wallet.address == 'test_address'
        assert saved_query.address == 'test_address'
        assert saved_wallet.wallet_queries[0].id == saved_query.id
