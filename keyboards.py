from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
import descriptions as txt

guid_description = InlineKeyboardButton('Что такое метод карт?', callback_data='button1')
guide_how_question_form = InlineKeyboardButton('Правила формирования вопроса', callback_data='button2')
guide_interpritation = InlineKeyboardButton('Как интерпритировать?', callback_data='button3')
action_select_card = InlineKeyboardButton('Выбрать карту',callback_data='button4')

inline_kb = InlineKeyboardMarkup(row_width=2)
inline_kb.add(guid_description, guide_interpritation)
inline_kb.row(guide_how_question_form)
inline_kb.add(action_select_card)

select_card_kb = InlineKeyboardMarkup()
select_card_kb.add(action_select_card)

sex_kb = InlineKeyboardMarkup()
sex_kb.add(InlineKeyboardButton('М', callback_data='m_button'))
sex_kb.add(InlineKeyboardButton('Ж', callback_data='w_button'))

sphere_life_kb = InlineKeyboardMarkup()
sphere_life_kb.add(InlineKeyboardButton('Отношения', callback_data='отношения'))
sphere_life_kb.add(InlineKeyboardButton('Работа', callback_data='работа'))
sphere_life_kb.add(InlineKeyboardButton('Здоровье', callback_data='здоровье'))
sphere_life_kb.add(InlineKeyboardButton('О себе', callback_data='осебе'))
sphere_life_kb.add(InlineKeyboardButton('Послание', callback_data='послание'))


form_question_kb = InlineKeyboardMarkup()
form_question_kb.add(InlineKeyboardButton('Сформируйте вопрос', callback_data='вопрос'))

get_card_kb = InlineKeyboardMarkup()
get_card_kb.add(InlineKeyboardButton('Ваша карта', callback_data='вашакарта'))
