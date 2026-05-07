from dotenv import load_dotenv

import requests
import os   
from pprint import pprint
load_dotenv()

def get_current_weather(city="Dehradun"):
    api_key = os.getenv("API_KEY")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: {response.status_code}")
        return None


if __name__ == "__main__":
    print("Welcome to the Weather App!")
    city = input("Enter the city name: ")
    weather_data = get_current_weather(city)
    if weather_data:
        pprint(weather_data)
