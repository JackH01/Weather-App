import requests


def cityToCoords(city):
    """
    Converts a city to lat and lon coords, using the open weather map 
    geo coder api.

    Params:
        - str: city

    Returns:
        - float: lat
        - float: lon
    """
    f = open(r"APIKey.txt", "r")
    API_key = f.read()
    limit = 1

    geoApiURL = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit={limit}&appid={API_key}"
    geoResponse = requests.get(geoApiURL)

    lat = geoResponse.json()[0]["lat"]
    lon = geoResponse.json()[0]["lon"]

    return (lat, lon)

def getWeatherFromCoords(lat, lon):
    """
    Gets the weather data from specified lat and lon coords, using the open
    weather map weather api.

    Params:
        - float: lat
        - float: lon

    Returns:
        - json: weatherResponse - weather data.
    """
    f = open(r"APIKey.txt", "r")
    API_key = f.read()

    weatherApiURL = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}"
    weatherResponse = requests.get(weatherApiURL)

    return weatherResponse.json()
