from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import pandas as pd
import requests
import os as os


def get_weather_data(latitude, longitude):
    today = datetime.now()
    week_ago = today - timedelta(days=7)

    start_date = week_ago.strftime("%Y-%m-%d")
    end_date = today.strftime("%Y-%m-%d")

    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}&longitude={longitude}"
        f"&start_date={start_date}&end_date={end_date}"
        "&daily=temperature_2m_max,temperature_2m_min"
    )

    response = requests.get(url)
    data = response.json()

    daily_data = data["daily"]

    df = pd.DataFrame({
        "date": daily_data["time"],
        "max_temp": daily_data["temperature_2m_max"],
        "min_temp": daily_data["temperature_2m_min"],
    })

    df["date"] = pd.to_datetime(df["date"])

    return df


def plot_weather_data(df, city_name):
    plt.figure(figsize=(10, 6))
    plt.plot(df["date"], df["max_temp"], marker="o", label="Max Temp")
    plt.plot(df["date"], df["min_temp"], marker="o", label="Min Temp")

    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.title(f"{city_name} Weather - Past 7 Days")
    plt.legend()

    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig(f"{city_name.lower()}_weather_chart.png")
    plt.show()



df = get_weather_data(11.410000, 76.699997)  # Ooty
print(df)
plot_weather_data(df, "Ooty")
# Create data folder if it doesn't exist
if not os.path.exists('data'):
    os.makedirs('data')

# Save to CSV
df.to_csv('data/ooty_weather.csv', index=False)
print("Data saved to data/ooty_weather.csv")