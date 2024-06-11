from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from datetime import datetime


import app.keyboards as kb
import app.database.requests as rq

router = Router()


# /start
@router.message(CommandStart())
async def start(message: Message):
    user_exist = await rq.check_user_exists(message.from_user.id)
    if user_exist == 1:
        await message.reply('Ты уже нажимал на эту кнопку!', reply_markup=kb.main)
    else:
        await rq.add_user(message.from_user.id)     # creating user blank subjects list
        await message.reply('Привет! Я бот для отслеживания успеваемости.'
                            'Чтобы начать, выбери предметы, которые хочешь трекать', 
                            reply_markup=kb.register)
        await message.answer('Чтобы закончить выбор, нажми на кнопку "💾 Сохранить и закончить выбор"', reply_markup=kb.register)


# register
@router.message(Command('register'))
async def register(message: Message):
    user_exist = await rq.check_user_exists(message.from_user.id)
    if user_exist == 1:
        await message.answer('Хочешь изменить свои предметы?', reply_markup=kb.yes_no)
    else:
        await rq.add_user(message.from_user.id)     # creating user blank subjects list
        await message.answer('Уверен?', reply_markup=kb.yes_no)


@router.callback_query(F.data == 'yes')
async def yes(query: CallbackQuery):
    await query.message.answer('Выбери предметы, которые хочешь трекать', reply_markup=kb.accept)
    await query.message.answer('Чтобы закончить выбор, нажми на кнопку "💾 Сохранить и закончить выбор"', reply_markup=kb.register)
    await rq.reset_all_subjects(query.from_user.id)
    await query.answer('✅')
    await query.message.edit_text('✅ Да')


@router.callback_query(F.data == 'no')
async def no(query: CallbackQuery):
    await query.answer('❌')
    await query.message.edit_text('❌ Нет')
    await query.message.answer('Продолжим...', reply_markup=kb.main)


@router.message(F.text == '💾 Сохранить и закончить выбор')
async def save_and_end(message: Message):
    await message.answer('Выбранные предметы сохранены!', reply_markup=kb.main)


@router.message(F.text == '🗑️ Очистить мой выбор')
async def clear(message: Message):
    await rq.reset_all_subjects(message.from_user.id)
    await message.reply('Выбор очищен', reply_markup=kb.register)


# =====================================================================================================

# /help
@router.message(Command('help'))
async def help(message: Message):
    await message.answer('Помощь')

# /menu
@router.message(Command('menu'))
async def menu(message: Message):
    await message.answer('Меню 👇', reply_markup=kb.main)
