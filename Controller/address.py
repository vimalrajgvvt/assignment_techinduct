from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from database.session import get_db
from schema.schemas import AddressCreate, AddressResponse
from service import address_service

router = APIRouter()

@router.post("/create", response_model=AddressResponse, status_code=status.HTTP_201_CREATED)
def create_address(address: AddressCreate, db: Session = Depends(get_db)):
    return address_service.create_new_address(db, address)

@router.get("/nearby", response_model=List[AddressResponse])
def get_nearby_bangalore_addresses(radius: float = 5.0, db: Session = Depends(get_db)):
    """
    Returns addresses within 'radius' km of Bangalore center.
    Default is 5km.
    """
    return address_service.get_addresses_within_radius(db, radius)
