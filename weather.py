import requests

def get_weather(api_key, location, unit='metric'):
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'q': location, 'units': unit, 'appid': api_key}

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        weather_data = response.json()

        return weather_data

    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")

def display_weather(weather_data, unit):
    temperature = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']
    conditions = weather_data['weather'][0]['description']

    if unit == 'metric':
        unit_symbol = '°C'
    else:
        unit_symbol = '°F'
        temperature = (temperature * 9/5) + 32

    print(f"\nCurrent Weather in {weather_data['name']}, {weather_data['sys']['country']}:")
    print(f"Temperature: {temperature:.2f} {unit_symbol}")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")
    print(f"Conditions: {conditions.capitalize()}")

if __name__ == "__main__":
    api_key = 'b5a0a50ad325b7623fcf9b5293fd506a'
    location = input("Enter the city or location: ")
    unit = input("Choose temperature unit (Celsius or Fahrenheit): ").lower()

    if unit not in ['celsius', 'fahrenheit']:
        print("Invalid temperature unit. Using Celsius by default.")
        unit = 'celsius'

    weather_data = get_weather(api_key, location, unit)
    
    if weather_data:
        display_weather(weather_data, unit)
