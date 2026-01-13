from fastapi import FastAPI
from app.controller.address_controller import router
from app.database.base import Base
from app.database.session import engine
from app.core.logging import setup_logging

setup_logging()
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Address Book API")
app.include_router(router, prefix="/addresses", tags=["Addresses"])
