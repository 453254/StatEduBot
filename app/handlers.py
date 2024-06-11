from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from datetime import datetime


import app.keyboards as kb
import app.database.requests as rq

router = Router()


# /help
@router.message(Command('help'))
async def help(message: Message):
    await message.answer('Помощь')

# /menu
@router.message(Command('menu'))
async def menu(message: Message):
    await message.answer('Меню 👇', reply_markup=kb.main)
