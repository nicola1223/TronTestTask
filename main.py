"""Main file of microservice"""
from fastapi import FastAPI

from api.v1.routers import router as v1_router
from core.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(v1_router)


@app.get('/')
async def root():
    """API root endpoint"""
    return {'message': 'Welcome to the Wallet API!'}
