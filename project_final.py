from flask import Flask, render_template, request
import requests

app = Flask(__name__)

open_weather_key = "42e0db3eff3e8f26179d7cc0dd37c6b0"
yelp_api_key = "4gxqsxIgu-yLpq3FyyOdpCpUNySuh39fH8BlT4Shm7UIrvji1SAbVb5GO3mf5gZbf3RKP0KSiUwrXAMz3xLcaSr1N-uDDX52hS2h1ipf9csZk-VnB0LcpK6q3sNHZ3Yx"


def get_weather_data(city):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_key}&units=imperial"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            weather_description = data['weather'][0]['description']
            temperature = data['main']['temp']
            return f"{weather_description.capitalize()}, {temperature} °F"
        else:
            return "Weather data unavailable, please check the city name."
    except requests.exceptions.RequestException as e:
        return f"Error retrieving weather data: {str(e)}"


def get_restaurants_data(city):
    try:
        url = f'https://api.yelp.com/v3/businesses/search?location={city}&categories=restaurants,cafes,food&sort_by=rating&limit=10'
        headers = {'Authorization': f"Bearer {yelp_api_key}"}
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            restaurants = []
            for business in data['businesses']:
                restaurants.append({
                    "name": business['name'],
                    "rating": business['rating'],
                    "address": ", ".join(business['location']['display_address']),
                    "image_url": business['image_url'],
                })
            return restaurants
        else:
            return []
    except requests.exceptions.RequestException as e:
        return f"Error retrieving restaurant data: {str(e)}"


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        city = request.form['city']
        weather = get_weather_data(city)
        restaurants = get_restaurants_data(city)
        return render_template('results.html', weather=weather, restaurants=restaurants, city=city)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)