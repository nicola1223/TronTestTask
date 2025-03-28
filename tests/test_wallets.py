"""Tests for application"""
from datetime import datetime
from unittest.mock import patch

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


@pytest.fixture(autouse=True)
def test_db():
    """Provide a test database session"""
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)
    engine.dispose()


def test_queries():
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


def test_wallet_endpoint():
    """Test wallet endpoint"""
    mock_response = {
        'address': 'test_address',
        'balance_trx': 100,
        'bandwidth': 50,
        'energy': 20
    }

    with patch('api.v1.endpoints.wallets.get_wallet') as mock_service:
        mock_service.return_value = mock_response

        response = client.post(
            "v1/wallet/",
            json={'address': 'test_address'}
        )

        mock_service.assert_called_once_with('test_address')

        assert response.status_code == 200
        assert response.json() == mock_response

        with TestingSessionLocal() as db:
            wallet_query = select(Wallet).limit(1)
            query_query = select(WalletQuery).limit(1)

            wallet = db.execute(wallet_query).scalar()
            query = db.execute(query_query).scalar()

            assert wallet.address == 'test_address'
            assert query.address == 'test_address'
            assert wallet.balance_trx == 100

        response = client.get('v1/wallet/queries?skip=0&limit=1')
        assert response.status_code == 200
        assert len(response.json()) == 1
        assert response.json()[0]['address'] == 'test_address'
