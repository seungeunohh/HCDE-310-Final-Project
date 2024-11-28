from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# for the city's weather
open_weather_key = "42e0db3eff3e8f26179d7cc0dd37c6b0"
# for attractions/places
foursquare_api_key = "fsq3TuKTngxKhRoh8dDkl7DucVlWniJo2OBoy53M1VKgeT4="
# for local events/festivals
eventbrite_api_key = "4BNWXHEXU74C5LA2KH"
# for dining & food spots data
yelp_api_key = ("4gxqsxIgu-yLpq3FyyOdpCpUNySuh39fH8BlT4Shm7UIrvji1SAbVb5GO3mf5gZbf3RKP0KSiUwrXAMz3xLcaSr1N-uDDX52hS2h1ip"
                "f9csZk-VnB0LcpK6q3sNHZ3Yx")
# 4gxqsxIgu-yLpq3FyyOdpCpUNySuh39fH8BlT4Shm7UIrvji1SAbVb5GO3mf5gZbf3RKP0KSiUwrXAMz3xLcaSr1N-uDDX52hS2h1ipf9csZk-VnB0LcpK6q3sNHZ3Yx


def get_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_key}&units=metric"
    response = request.get(url)
    if response.status_code == 200:
        data = response.json()
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        return f"{weather_description}, {temperature} C"
    else:
        return "Weather data unavailable"

def get_dining_data(city):
    url = f'https://api.yelp.com/v3/businesses/search'


def get_attractions_data(city):
    url = 'https://api.foursquare.com/v3/places/search'


def get_events_data(city, month):
    url = f'https://www.eventbriteapi.com/v3/events/search/'
