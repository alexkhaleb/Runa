import requests
import pytest
import json
from datetime import datetime

# Configuration
API_KEY = "7445b8ec023e25f9b731e482b9fb5ee1"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Helper Function
def build_url(params):
    params["appid"] = API_KEY
    return BASE_URL, params

# Test Class
class TestWeatherAPI:
    def test_weather_by_city_name(self):
        url, params = build_url({"q": "London"})
        response = requests.get(url, params=params)
        assert response.status_code == 200
        assert "weather" in response.json()

    def test_weather_by_coordinates(self):
        url, params = build_url({"lat": 35.6895, "lon": 139.6917})
        response = requests.get(url, params=params)
        assert response.status_code == 200
        assert "coord" in response.json()

    def test_invalid_city_name(self):
        url, params = build_url({"q": "InvalidCity123"})
        response = requests.get(url, params=params)
        assert response.status_code == 404
        assert response.json()["message"] == "city not found"