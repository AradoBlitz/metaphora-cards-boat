from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
import descriptions as txt

guid_description = InlineKeyboardButton('Что такое метод карт?', callback_data='button1')
guide_how_question_form = InlineKeyboardButton('Правила формирования вопроса', callback_data='button2')
guide_interpritation = InlineKeyboardButton('Как интерпритировать?', callback_data='button3')
action_get_card = InlineKeyboardButton('Выбрать карту',callback_data='button4')

inline_kb = InlineKeyboardMarkup().add(guid_description, guide_how_question_form,
        guide_interpritation, action_get_card)
