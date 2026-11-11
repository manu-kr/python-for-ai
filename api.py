import re

import requests

# We need coordinates to get weather data
latitude = 48.85   # Paris latitude
longitude = 2.35   # Paris longitude

# Build the API URL with our parameters
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

# Make the request
response = requests.get(url)
data = response.json()

print(data)

temperature = data['current']['temperature_2m']
print(f"Temperature in Paris: {temperature}°C")

def getWeatherData(latitude, longitude):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"
    response = requests.get(url)
    g_url = f"https://google.com"
    response1 = requests.get(g_url)
    data1 = response1.text
    print(data1)

    data = response.json()
    return data['current']['temperature_2m']

paris_temperature = getWeatherData(48.85, 2.35)
london_temperature = getWeatherData(51.51, -0.13)
bangalore_temperature = getWeatherData(12.97, 77.59)
tokyo_temperature = getWeatherData(35.68, 139.76)

print(f"Temperature in Paris: {paris_temperature}°C")
print(f"Temperature in London: {london_temperature}°C")
print(f"Temperature in Bangalore: {bangalore_temperature}°C")
print(f"Temperature in Tokyo: {tokyo_temperature}°C")