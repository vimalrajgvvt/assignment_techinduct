from fastapi import FastAPI
from database.base import Base
from database.session import engine
from Controller import address

# Create DB tables on startup
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Address Book API",
    description="Minimal API for address management with coordinate filtering"
)

app.include_router(address.router, prefix="/address")

# Standard entry point for running the script directly
if __name__ == "__main__":
    # Note: Using "app.app" matches your directory structure
    uvicorn.run("app.app", host="0.0.0.0", port=5002, reload=True)

