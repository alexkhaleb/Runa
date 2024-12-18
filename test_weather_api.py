import requests
import pytest
import json
from datetime import datetime

# Configuration
API_KEY = "7445b8ec023e25f9b731e482b9fb5ee1"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Helper function to build API request
def build_url(params):
    params["appid"] = API_KEY
    return BASE_URL, params

# Test Cases
class TestCurrentWeatherAPI:
    
    # Test 1: Get weather by valid city name
    def test_weather_by_city_name(self):
        city_name = "Mexico City"
        url, params = build_url({"q": city_name})
        
        response = requests.get(url, params=params)
        
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        json_data = response.json()
        
        assert "weather" in json_data, "Weather key not found in response"
        assert json_data["name"] == city_name, f"City name mismatch: {json_data['name']}"
        assert "main" in json_data, "Main weather data missing"
    
    # Test 2: Get weather by valid geographic coordinates
    def test_weather_by_coordinates(self):
        latitude, longitude = 35.6895, 139.6917  # Coordinates for Tokyo
        url, params = build_url({"lat": latitude, "lon": longitude})
        
        response = requests.get(url, params=params)
        
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        json_data = response.json()
        
        assert "weather" in json_data, "Weather key not found in response"
        assert "coord" in json_data, "Coordinates data missing"
        assert pytest.approx(json_data["coord"]["lat"], 0.01) == latitude, "Latitude mismatch"
        assert pytest.approx(json_data["coord"]["lon"], 0.01) == longitude, "Longitude mismatch"
    
    # Test 3: Error handling for invalid input
    def test_weather_invalid_city_name(self):
        invalid_city_name = "InvalidCity123"
        url, params = build_url({"q": invalid_city_name})
        
        response = requests.get(url, params=params)
        
        assert response.status_code == 404, f"Expected 404, got {response.status_code}"
        json_data = response.json()
        
        assert "message" in json_data, "Error message missing in response"
        assert json_data["cod"] == "404", f"Expected error code 404, got {json_data['cod']}"
        assert json_data["message"] == "city not found", "Unexpected error message"

# Entry point for pytest execution
if __name__ == "__main__":
    pytest.main(["-v", "--tb=short", "--maxfail=1"])