from aiogram.types import ReplyKeyboardRemove, \
        ReplyKeyboardMarkup, \
        KeyboardButton

start_button = KeyboardButton('/cards')

menue_kb = ReplyKeyboardMarkup(resize_keyboard=True)
menue_kb.add(start_button)


