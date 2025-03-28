"""V1 routers"""
from fastapi import APIRouter

from .endpoints import wallets

router = APIRouter(prefix='/v1')

router.include_router(wallets.router)
