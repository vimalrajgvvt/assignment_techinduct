from pydantic import BaseModel, Field

class AddressCreate(BaseModel):
    name: str = Field(..., min_length=1)
    street: str = Field(..., min_length=1)
    city: str = Field(..., min_length=1)
    latitude: float = Field(..., ge=-90, le=90)
    longitude: float = Field(..., ge=-180, le=180)

class AddressResponse(AddressCreate):
    id: int

    class Config:
        from_attributes = True
