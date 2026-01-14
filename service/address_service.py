from sqlalchemy.orm import Session
from model.address import Address
from schema.schemas import AddressCreate
from utils.geo import calculate_haversine_distance
from core.logging import logger

BANGALORE_LAT = 12.9738 # Bangalore Center (MG Road)
BANGALORE_LON = 77.6119 # Bangalore Center (MG Road)

def create_new_address(db: Session, address_data: AddressCreate):
    logger.info(f"Adding new address: {address_data.name}")
    new_address = Address(**address_data.model_dump())
    db.add(new_address)
    db.commit()
    db.refresh(new_address)
    return new_address


def get_addresses_within_radius(db: Session, radius_km: float):
    # 1. Fetch all addresses from DB
    all_addresses = db.query(Address).all()
    
    nearby_addresses = []
    
    for addr in all_addresses:
        # 2. Calculate distance between Bangalore and the stored address
        dist = calculate_haversine_distance(
            BANGALORE_LAT, BANGALORE_LON, 
            addr.latitude, addr.longitude
        )
        
        # 3. If within 5km radius
        if dist <= radius_km:
            nearby_addresses.append(addr)
            
    return nearby_addresses