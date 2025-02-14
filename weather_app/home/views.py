from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from django.http import HttpResponseRedirect

from .forms import CityForm
from .api_calls import cityToCoords, getWeatherFromCoords

def home(request):
  errorMessage = None
  # if this is a POST request we need to process the form data
  if request.method == "POST":
      # create a form instance and populate it with data from the request:
      form = CityForm(request.POST)
      # check whether it's valid:
      if form.is_valid():
          # process the data in form.cleaned_data as required
          # ...
          
          # TODO process data, see if need to process weather data.
          city = form.cleaned_data["city"]
          lat, lon = cityToCoords(city)
          weatherData = getWeatherFromCoords(lat, lon)
          displayWeather = True

          if weatherData == None:
            errorMessage = "There is an issue with the open weather map api, please try again later."
            displayWeather = False

          #return render(request, "homepage.html", {"form": form})

  # if a GET (or any other method) we'll create a blank form
  else:
      form = CityForm()
      city = ""
      displayWeather = False
      weatherData = None
      print("aaaaaaaaaaaaaaaa")

  print(weatherData)

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

  else:
    context = {
    "form": form,
    "city": city,
    "displayWeather": displayWeather,
    "errorMessage": errorMessage,
  }

  return render(request, "homepage.html", context)
