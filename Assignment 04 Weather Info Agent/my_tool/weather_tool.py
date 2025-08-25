from agents import function_tool


@function_tool
def get_weather(city):
    print("weather tool fire ------->")
    
    if city == "Karachi":
        return f"The weather in {city} is 28°C."
    
    if city == "Lahore":
        return f"The weather in {city} is 30°C."
    
    if city == "Quetta":
        return f"The weather in {city} is 24°C."
    
    else:
        return f"Sorry, I don't know the weather in {city}." 