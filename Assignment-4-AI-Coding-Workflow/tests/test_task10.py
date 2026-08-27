import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from tasks.task10.unassisted import format_weather_summary as weather_unassisted
from tasks.task10.assisted import format_weather_summary as weather_assisted

SAMPLE_API = {
    "name": "Hyderabad",
    "main": {
        "temp": 303.15, # 30.0 C, 86.0 F
        "humidity": 65
    },
    "weather": [{"description": "scattered clouds"}]
}

@pytest.mark.parametrize("weather_fn", [weather_unassisted, weather_assisted])
def test_weather_formatter(weather_fn):
    res = weather_fn(SAMPLE_API)
    assert res["city"] == "Hyderabad"
    assert res["temp_celsius"] == 30.0
    assert res["temp_fahrenheit"] == 86.0
    assert res["humidity"] == 65
    assert "Hyderabad" in res["summary"]
    assert "30.0°C" in res["summary"]
