from uuid import UUID
from pydantic import BaseModel, EmailStr

class RiderCreate(BaseModel):
    name: str
    email: str
    phone_number: str

class RiderResponse(BaseModel):
    id: uuid.UUID
    name: str
    email: str
    phone_number: Optional[str]

    model_config = {
        "from_attributes": True
    }