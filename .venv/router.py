import requests as rq
import datetime
import asyncio
from config import tg_token
from config import open_api_weather, news_api
from aiogram import Bot, Dispatcher, types, F,Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from Code_bot import get_weather



router = Router()

@router.message(F.text != 'Weather')
async def get_weather(message: types.Message):
    code_smile_weather = {
        'Clear': 'Clear \U00002600',
        'Clouds': 'Clouds \U00002601',
        'Rain': 'Rain \U00002614',
        'Drizzle': 'Drizzle \U00002614',
        'Thunderstorm': "Thunderstorm \U000026A1",
        'Snow': 'Snow \U0001F328',
        'Mist': 'Mist \U0001F32B'
    }

    #try:
    r = rq.get(f'https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_api_weather}&units=metric')
    data = r.json()
    city = data['name']
    temp = data['main']['temp']
    humidity = data['main']['humidity']
    temp_max = data['main']['temp_max']
    temp_min = data['main']['temp_min']
    speed = data['wind']['speed']
    gust = data['wind']['gust']
    smile_weather = data['weather'][0]['main']
    weather = data['weather'][0]['main']

    await message.reply(f'***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n'
            f'{city}\ntemp: {temp}°C\n'
            f'temp min: {temp_min}°C\n'
            f'temp max: {temp_max}°C\n'
            f'humidity: {humidity}%\n'
            f'speed: {speed}m/s\n'
            f'gust: {gust}m/s\n'
            f'today {code_smile_weather[smile_weather]}')

