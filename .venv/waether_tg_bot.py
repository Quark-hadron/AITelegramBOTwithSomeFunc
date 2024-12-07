import requests as rq
import datetime
import asyncio
from config import tg_token
from config import open_api_weather, news_api
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from Code_bot import get_weather
from curce import USD,EUR
from news import get_news
import g4f
from AI import generate

import keyboard as kb

bot = Bot(token=tg_token)
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer('Hello,Chose and click',reply_markup = kb.startWeather)

@dp.message(Command('Cost'))
async def get_cost(message: types.Message):
    await message.answer(f'Cost USD: {USD}$\n'
                         f'Cost EUR: {EUR}€')


@dp.message(Command('News'))
async  def get_news(message: types.Message):
    r = rq.get(f'https://newsapi.org/v2/everything?domains=techcrunch.com,thenextweb.com&apiKey={news_api}')
    data = r.json()

    publishedAt_1 = data['articles'][0]['publishedAt']
    title_1 = data['articles'][0]['title']
    author_1 = data['articles'][0]['author']
    content_1 = data['articles'][0]['content']
    description_1 = data['articles'][0]['description']
    url_1 = data['articles'][0]['url']

    await message.answer(f'{publishedAt_1}\n'
                         f'{title_1}\n'
                         f'{author_1}\n'
                         f'{content_1}\n'
                         f'{description_1}')
    await message.answer(f'{url_1}')


@dp.message(Command('Weather'))
async def cmd_start(message: types.Message):
    await message.answer('Enter please city')

@dp.message(F.text != 'Weather')
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

    try:
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
        if weather == 'Rain':
            await message.answer('It\'s worth taking an umbrella with you.')
        elif weather == 'Clouds':
            await message.answer('It\'s worth taking an umbrella with you.')
        elif weather == 'Snow':
            await message.answer('Better dress warmer')
        elif weather == 'Mist':
            await message.answer('Better wear reflectors')
        elif weather == 'Clear':
            await message.answer('cool weather')
        await message.answer('Good day')


    except:
        await message.answer('check please your command')

@dp.message(Command('AI'))
async def cmd_start(message: types.Message):
    await message.answer('Enter please:')

@dp.message(F.text != '/Weather')
async def ai(message: types.Message):
    res = await generate(message.text)  # res=
    # print(res.choices[0].message.content)
    await message.answer(res)


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
