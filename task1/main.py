from fetching_the_data import fetch_weather_data # fetching from fetching_the_data.py to use openweathermap
from visualization import plot_dashboard     # to plot graphs in dashboard

API_KEY = "d612d9971cffc3daa942fce12dcd3940"  # your api key generated from openweathermap

cities = ["Hyderabad", "Mumbai", "Delhi", "Chennai", "Pune"]  # for any random cities of your wish

valid_cities = []  # for valid cities

# the parameters we need to take for each city
temps = []
humidity = []
pressure = []
wind_speed_list = []
cloudiness_list = []

# displaying the data
for city in cities:
    data = fetch_weather_data(city, API_KEY)
    if data:
        valid_cities.append(city)
        temps.append(data["Temperature"])
        humidity.append(data["Humidity"])
        pressure.append(data["Pressure"])
        wind_speed_list.append(data["Wind Speed"])
        cloudiness_list.append(data["Cloudiness"])

# for true
if valid_cities:
    plot_dashboard(
        valid_cities,
        temps,
        humidity,
        pressure,
        wind_speed_list,
        cloudiness_list
    )
# for false
else:
    print("No valid data fetched. Check your API key.")