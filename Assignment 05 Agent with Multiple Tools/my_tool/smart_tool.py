from agents import function_tool


@function_tool
def add(n1, n2):
    print("plus tool fire ----->")
    return f"Your answer is {n1 + n2}"


@function_tool
def subtract(n1, n2):
    print("subtract tool fire ----->")
    return f"Your answer is {n1 - n2}"


@function_tool
def multiply(n1, n2):
    print("multiply tool fire ----->")
    return f"Your answer is {n1 * n2}"


@function_tool
def divide(n1, n2):
    print("divide tool fire ----->")
    return f"Your answer is {n1 / n2}"


@function_tool
def get_weather(city):
    print("weather tool fire ----->")
    
    if city == "Karachi":
        return f"The weather in {city} is 28°C"
    
    if city == "Lahore":
        return f"The weather in {city} is 32°C"
    
    if city == "Islamabad":
        return f"The weather in {city} is 30°C"
    
    else:
        return f"Sorry, I don't know the weather in {city}"
    
