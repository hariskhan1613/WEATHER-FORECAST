import requests

def get_weather_data(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": location,
        "appid": api_key,
        "units": "metric"  # Use metric units for temperature
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    return data

def display_weather(data):
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    description = data['weather'][0]['description']

    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")
    print(f"Description: {description}")

def main():
    api_key = "bd5e378503939ddaee76f12ad7a97608"
    location = input("Enter city name or zip code: ")

    weather_data = get_weather_data(api_key, location)

    if weather_data['cod'] == 200:
        display_weather(weather_data)
    else:
        print("Weather data not available.")

if __name__ == "__main__":
    main()
