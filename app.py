from fastapi import FastAPI # type: ignore
from database.base import Base
from database.session import engine
from Controller import address

Base.metadata.create_all(bind=engine) # Create DB tables on startup

app = FastAPI(title="Address Book API", description="API for address")

app.include_router(address.router, prefix="/address") # route the controller to address the api

if __name__ == "__main__":
    uvicorn.run("app.app", host="0.0.0.0", port=5002, reload=True)
    # uvicorn app:app --host 0.0.0.0 --port 5002 --reload //command to run the project



