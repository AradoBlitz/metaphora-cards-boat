import os, random

import logging
from typing import Text
from aiogram.dispatcher.filters import state

from aiogram.types import message, reply_keyboard
from aiogram.types import callback_query
from aiogram.types.callback_query import CallbackQuery
from aiogram.types import InputFile
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup 
 
import files as cards
import menu as mn
import descriptions as txt
import keyboards as kb
import reply_keyboards as reply_kb


from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)

API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")
PROXY_URL = 'http://proxy.server:3128'

bot = Bot(token=API_TOKEN, proxy=PROXY_URL)

dp = Dispatcher(bot, storage=MemoryStorage())

class Form(StatesGroup):
    sex = State()
    sphereLife = State()
    question = State()

@dp.callback_query_handler(lambda c: c.data == 'вашакарта', state = Form.sphereLife)
async def process_get_card_button(callback_query: types.CallbackQuery, state: FSMContext):
    
    await bot.answer_callback_query(callback_query.id)
    print("return card")
    async with state.proxy() as data:
        await bot.send_photo(callback_query.from_user.id, photo=InputFile(cards.selectCard(str(list(data.values())[0]), str(list(data.values())[1]))))   
    await state.finish()

    print(str(list(data.values())))


@dp.callback_query_handler(lambda c: c.data == 'health' 
        or c.data == 'message-card'
        or c.data == 'me'
        or c.data == 'relationships'
        or c.data == 'work-career'
        or c.data == 'what-to-do', state = Form.sex)
async def process_sphere_life(callback_query: types.CallbackQuery, state: FSMContext):
    await state.update_data(sphere_life = callback_query.data)
    
    async with state.proxy() as data:
        data["sphere_life"] = callback_query.data
    await Form.sphereLife.set()
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,
            'Сформулируйте вопрос', reply_markup=kb.get_card_kb)

@dp.callback_query_handler(lambda c: c.data == 'man'
        or c.data == 'woman', state = None)
async def process_sex_button(callback_query: types.CallbackQuery, state: FSMContext):
  
    async with state.proxy() as data:
        data["sex"] = callback_query.data
    await Form.next()
    await bot.answer_callback_query(callback_query.id);
    await bot.send_message(callback_query.from_user.id,
            'Из какой области ваш вопрос?',
            reply_markup= kb.sphere_life_kb);
    

@dp.callback_query_handler(lambda c: c.data == 'button1')
async def process_callback_button(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,
            txt.method_description,
            reply_markup=kb.select_card_kb)


@dp.callback_query_handler(lambda c: c.data == 'button2')
async def process_button2(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,
            txt.how_to_form_question_description,
            reply_markup = kb.select_card_kb)

@dp.callback_query_handler(lambda c: c.data == 'button3')
async def process_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,
            txt.how_to_interpitated_card_description,
            reply_markup=kb.select_card_kb)

@dp.callback_query_handler(lambda c: c.data == 'button4')
async def process_button4(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 
            'Ваш пол?', 
            reply_markup=kb.sex_kb)

@dp.message_handler(commands=['cards'])
async def send_cards(message: types.Message):
    await message.reply(txt.greeting, reply_markup=kb.inline_kb)

@dp.message_handler(commands=['start','help'])
async def sen_welcome(message: types.Message):
    await message.reply(txt.greeting, reply_markup=reply_kb.menue_kb)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
