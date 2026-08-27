"""
task10: Weather API Parser (AI-Assisted implementation)
Parses nested JSON payload and converts temperatures.
"""

def format_weather_summary(api_response: dict) -> dict:
    if not api_response or "main" not in api_response:
        raise ValueError("Invalid weather payload.")
        
    city = api_response.get("name", "Unknown Location")
    k = float(api_response["main"].get("temp", 273.15))
    c = round(k - 273.15, 1)
    f = round((c * 9/5) + 32, 1)
    
    humidity = api_response["main"].get("humidity", 0)
    desc = api_response.get("weather", [{}])[0].get("description", "clear sky").capitalize()
    
    return {
        "city": city,
        "temp_celsius": c,
        "temp_fahrenheit": f,
        "humidity": humidity,
        "condition": desc,
        "summary": f"Weather in {city}: {desc}, {c}°C ({f}°F), Humidity: {humidity}%."
    }
