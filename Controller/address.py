from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from database.session import get_db
from model.address import Address
from schema.schemas import AddressCreate, AddressResponse
from service import address_service
from core import logging

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
@router.put("/update/{address_id}", response_model=AddressResponse)
def update_address(address_id: int, data: AddressCreate, db: Session = Depends(get_db)):
    updated = address_service.update_existing_address(db, address_id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="Address not found")
    return updated

@router.delete("/delete_address/{address_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_address(address_id: int, db: Session = Depends(get_db)):
    if not address_service.delete_existing_address(db, address_id):
        raise HTTPException(status_code=404, detail="Address not found")
    return None

