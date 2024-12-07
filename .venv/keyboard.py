from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton

startWeather = ReplyKeyboardMarkup(
    keyboard=[
        [
            #KeyboardButton(text='/IT'),
            KeyboardButton(text='/Weather'),
            KeyboardButton(text='/Cost'),
            KeyboardButton(text='/News'),
            KeyboardButton(text='/AI')
        ]
    ],
    resize_keyboard = True,
    one_time_keyboard=False,
    input_field_placeholder='Menu'
)