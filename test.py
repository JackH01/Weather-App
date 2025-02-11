"""
A test script to try out the API calls, using: the weather api and geocoder api from https://openweathermap.org/api.
"""
import requests

f = open("APIKey.txt", "r")
API_key = f.read()


# Using Geocoder API to turn city name into lat/lon coords.
city = "London"
limit = 1

geoApiURL = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit={limit}&appid={API_key}"
geoResponse = requests.get(geoApiURL)

lat = geoResponse.json()[0]["lat"]
lon = geoResponse.json()[0]["lon"]

# Using Weather API to get the current weather from lat/lon coords.
weatherApiURL = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}"
weatherResponse = requests.get(weatherApiURL)

print(weatherResponse.json())