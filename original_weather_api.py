import requests
import json


'''Our previous weather api call to retrieve the forecast for a region'''
def get_weather(lat, lon):
    weather = requests.get(f"https://api.weather.gov/points/{lat},{lon}")
    json_file = weather.json()
    isolated_forecast = json_file["properties"]["forecast"]
    forecast = requests.get(isolated_forecast).json()

    for section in forecast["properties"]["periods"]:
        day = section["name"]
        temp = section["temperature"]
        detail = section["detailedForecast"]
        print(day, "\n",  temp, "\n", detail)
        
get_weather(lat, lon)