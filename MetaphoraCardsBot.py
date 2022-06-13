import os

import logging
from typing import Text
from aiogram.dispatcher.storage import FSMContext

from aiogram.types import message, reply_keyboard
from aiogram.types import callback_query
from aiogram.types.callback_query import CallbackQuery

import menu as mn
import descriptions as txt
import keyboards as kb


from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)

API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.callback_query_handler(lambda c: c.data == 'button1')
async def process_callback_button(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, txt.method_description)


@dp.callback_query_handler(lambda c: c.data == 'button2')
async def process_button2(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,txt.how_to_form_question_description)

@dp.callback_query_handler(lambda c: c.data == 'button3')
async def process_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, txt.how_to_interpitated_card_description)

@dp.callback_query_handler(lambda c: c.data == 'button4')
async def process_button4(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'card panel')

@dp.message_handler(commands=['start','help'])
async def send_welcome(message: types.Message):

    await message.reply(txt.greeting, reply_markup=kb.inline_kb)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
