import requests
# fetching the data from openweathermap
def fetch_weather_data(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)

    # if everything is correct
    if response.status_code == 200:
        data = response.json()
        return {
            "Temperature": data["main"]["temp"],
            "Humidity": data["main"]["humidity"],
            "Pressure": data["main"]["pressure"],
            "Wind Speed": data["wind"]["speed"],
            "Cloudiness": data["clouds"]["all"]   # added cloudiness
        }
    # if wrong else statement will display
    else:
        print(f"Error fetching data for {city} - Status {response.status_code}")
        return None