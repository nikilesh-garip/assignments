"""
task10: Weather API Parser (Unassisted implementation)
Parses nested JSON payload and converts temperatures.
"""

def format_weather_summary(api_response: dict) -> dict:
    if not api_response or "main" not in api_response:
        raise ValueError("Invalid weather payload.")
        
    city = api_response.get("name", "Unknown Location")
    temp_kelvin = api_response["main"].get("temp", 273.15)
    temp_c = round(temp_kelvin - 273.15, 1)
    temp_f = round((temp_c * 9/5) + 32, 1)
    
    humidity = api_response["main"].get("humidity", 0)
    weather_list = api_response.get("weather", [{}])
    condition = weather_list[0].get("description", "clear sky").capitalize()
    
    summary_text = f"Weather in {city}: {condition}, {temp_c}°C ({temp_f}°F), Humidity: {humidity}%."
    
    return {
        "city": city,
        "temp_celsius": temp_c,
        "temp_fahrenheit": temp_f,
        "humidity": humidity,
        "condition": condition,
        "summary": summary_text
    }
