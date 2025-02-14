from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from django.http import HttpResponseRedirect

from .forms import CityForm
from .api_calls import cityToCoords, getWeatherFromCoords

def home(request):
  errorMessage = None
  # If this is a POST request, process the form data
  if request.method == "POST":
      # Create a form instance and populate it with data from the request:
      form = CityForm(request.POST)
      # Check whether it's valid:
      if form.is_valid():
          # Process validated form - get weather data from city.
          # NOTE: if there is no direct match to the city entered, the API returns the nearest match.
          city = form.cleaned_data["city"]
          lat, lon = cityToCoords(city)
          weatherData = getWeatherFromCoords(lat, lon)
          displayWeather = True

          # In case the API is down / we run out of API calls.
          if weatherData == None:
            errorMessage = "There is an issue with the open weather map api, please try again later."
            displayWeather = False

  # if a GET (or any other method) create a blank form
  else:
      form = CityForm()
      city = ""
      displayWeather = False
      weatherData = None

  # If there was a POST request, and the API has returned some data, the form and data will be displayed.
  if displayWeather:
    context = {
      "form": form,
      "city": city,
      "actual_city": weatherData["name"],
      "city_names_match": (city == weatherData["name"]),
      "country": weatherData["sys"]["country"],
      "lat": weatherData["coord"]["lat"],
      "lon": weatherData["coord"]["lon"],
      "main_weather": weatherData["weather"][0]["main"],
      "description": weatherData["weather"][0]["description"],
      "temp": weatherData["main"]["temp"],
      "feels_like": weatherData["main"]["feels_like"],
      "pressure": weatherData["main"]["pressure"],
      "humidity": weatherData["main"]["humidity"],
      "displayWeather": displayWeather,
      "errorMessage": errorMessage,
    }

  # Otherwise just display an emptt form.
  else:
    context = {
    "form": form,
    "city": city,
    "displayWeather": displayWeather,
    "errorMessage": errorMessage,
  }

  return render(request, "homepage.html", context)
