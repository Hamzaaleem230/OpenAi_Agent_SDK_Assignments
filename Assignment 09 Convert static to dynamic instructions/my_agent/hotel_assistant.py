from agents import Agent
from my_config.gemini_config import GEMINI_MODEL
from data_schema.hotel_info_output import HotelInfoOutput


hotels = {
    "Pearl Continental": {"location": "Karachi", "rooms": 120, "available": True},
    "Serena Hotel": {"location": "Islamabad", "rooms": 150, "available": False},
    "Avari Towers": {"location": "Lahore", "rooms": 200, "available": True}
}

hotel_assistant = Agent(
    name="🏨 Hotel Assistant",
    instructions=f"""
    You are a hotel information assistant.
    You can provide details (location, rooms, availability) about multiple hotels.
    
    Hotels data:
    {hotels}

    - Identify which hotel user is asking about.
    - Return details only for that hotel.
    - Always include reasoning.
    """,
    model=GEMINI_MODEL,
    output_type=HotelInfoOutput
)
