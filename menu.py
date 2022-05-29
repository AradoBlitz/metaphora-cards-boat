from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardMarkup, \
        InlineKeyboardButton, KeyboardButton



what_is_card_method_btn = KeyboardButton("Что такое метод карт?")
how_to_form_question_btn = KeyboardButton("Правила формулирования вопроса")
how_interpitated_card_btn = KeyboardButton("Как интерпритирвать?")
get_card_btn = KeyboardButton("Выбрать карту")

greet_kb = ReplyKeyboardMarkup(resize_keyboard=True)
greet_kb.add(what_is_card_method_btn)
greet_kb.add(how_to_form_question_btn)
greet_kb.add(how_interpitated_card_btn)
greet_kb.add(get_card_btn)
