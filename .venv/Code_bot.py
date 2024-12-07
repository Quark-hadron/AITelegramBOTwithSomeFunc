import requests as rq
import datetime
from pprint import pprint
from config import open_api_weather as token

def get_weather(city,token):

    code_smile_weather = {
        'Clear': 'Clear \U00002600',
        'Clouds': 'Clouds \U00002601',
        'Rain': 'Rain \U00002614',
        'Drizzle': 'Drizzle \U00002614',
        'Thunderstorm': "Thunderstorm \U000026A1",
        'Snow': 'Snow \U0001F328',
        'Mist': 'Mist \U0001F32B'
    }

    try:
        r = rq.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}&units=metric')
        data = r.json()
        pprint(data)
        city = data['name']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        temp_max = data['main']['temp_max']
        temp_min = data['main']['temp_min']
        speed = data['wind']['speed']
        gust = data['wind']['gust']

        smile_weather = data['weather'][0]['main']

        print(f'***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n'
              f'{city}\ntemp: {temp}°C\n'
              f'temp min: {temp_min}°C\n'
              f'temp max: {temp_max}°C\n'
              f'humidity: {humidity}%\n'
              f'speed: {speed}m/s\n'
              f'gust: {gust}m/s\n'
              f'today {code_smile_weather[smile_weather]}')

    except Exception as ex:
        print(ex)
        print('Chake please name lat or lon')


def main():
    city = input('Enter city:' )
    get_weather(city,token)

if __name__ == '__main__':
    main()