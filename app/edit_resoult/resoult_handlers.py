from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from datetime import datetime


import app.keyboards as kb
import app.database.requests as rq
import app.edit_resoult.resoult_keyboards as ekb

router_resoult = Router()


@router_resoult.message(F.text == '➕ Добавить результат')
async def add_resoult(message: Message):
    await message.answer('Выберите предмет', reply_markup=None)#ekb.subjects)