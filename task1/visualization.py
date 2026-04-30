import matplotlib.pyplot as plt
# above package is used to design graphs

def plot_dashboard(cities, temps, humidity, pressure, wind_speed_list, cloudiness_list):
    # creating a 2x3 grid for neat layout
    fig, axs = plt.subplots(2, 3, figsize=(15, 8))

    # graph for temperature
    axs[0, 0].bar(cities, temps, color="orange")
    axs[0, 0].set_title("Temperature (°C)")

    # graph for humidity
    axs[0, 1].bar(cities, humidity, color="blue")
    axs[0, 1].set_title("Humidity (%)")

    # graph for pressure
    axs[0, 2].bar(cities, pressure, color="green")
    axs[0, 2].set_title("Pressure (hPa)")

    # graph for wind speed
    axs[1, 0].bar(cities, wind_speed_list, color="purple")
    axs[1, 0].set_title("Wind Speed (m/s)")

    # graph for cloudiness
    axs[1, 1].bar(cities, cloudiness_list, color="gray")
    axs[1, 1].set_title("Cloudiness (%)")

    # empty last box to avoid clutter
    axs[1, 2].axis("off")

    plt.suptitle("Weather Dashboard Across Cities", fontsize=16)
    plt.tight_layout()
    plt.savefig("weather_dashboard.png")
    plt.show()