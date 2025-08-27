from pydantic import BaseModel

class HotelInfoOutput(BaseModel):
    hotel_name: str
    location: str
    rooms: int
    available: bool
    reasoning: str
