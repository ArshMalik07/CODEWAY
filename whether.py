import requests

def get_weather_data(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    params = {
        'q': location,
        'appid': api_key,
        'units': 'metric',
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  
        return response.json()
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.RequestException as err:
        print(f"Request Error: {err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return None

def display_weather(weather_data):
    if weather_data:
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        description = weather_data['weather'][0]['description']

        print(f"\nCurrent Weather:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
        print(f"Description: {description}")
    else:
        print("Unable to display weather data.")

def main():
    api_key = '78feb2eb2cc52b8b741e77f37e34ff0f'  

    user_input = input("Enter the name of a city or a zip code: ")
    weather_data = get_weather_data(api_key, user_input)

    display_weather(weather_data)

if __name__ == "__main__":
    main()
