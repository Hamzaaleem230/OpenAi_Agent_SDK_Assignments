from my_agent.hotel_assistant import hotel_assistant
from agents import Runner, set_tracing_disabled

set_tracing_disabled(True)

def format_hotel_response(output):
    hotel_name = output.hotel_name
    location = output.location
    rooms = output.rooms
    available = "available for booking ✅" if output.available else "currently not available ❌"
    return f"{hotel_name} is located in {location}. It has {rooms} rooms and is {available}."

if __name__ == "__main__":
    user_input = input("👤 Enter your query: ")
    res = Runner.run_sync(starting_agent=hotel_assistant, input=user_input)

    final_answer = format_hotel_response(res.final_output)
    print("🤖 Bot:", final_answer)
