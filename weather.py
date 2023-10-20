from dotenv import load_dotenv
from pprint import pprint
import requests
import os


load_dotenv()

def get_current_weather(city = 'Melbourne, Australia'):
    request_url = f"http://api.openweathermap.org/data/2.5/weather?appid={os.getenv('API_KEY')}&q={city}&units=imperial"

    weather_data = requests.get(request_url).json()

    return weather_data


if __name__ == '__main__':
    print('\n Getting the Current Weather Status in your city \n')
    city = input('\n What city are you in? \n')

# check for empty strings or string with spaces
    if not bool(city.strip()):
        city = 'Sydney'

    weather_data = get_current_weather(city)
    print('\n')
    pprint(weather_data)
        

