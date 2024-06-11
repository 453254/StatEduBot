from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from datetime import datetime


import app.register.register_keyboard as kbr
import app.database.register_requests as rqr    # idk why it marked yellow, its work
from app.keyboards import main
from app.database.requests import check_user_registrasted

router_register = Router()


# /start
@router_register.message(CommandStart())
async def start(message: Message):
    user_exist = await rqr.check_user_started(message.from_user.id)
    if user_exist == 1:
        await message.reply('Ты уже нажимал на эту кнопку!', reply_markup=main)
    else:
        await rqr.guest(message.from_user.id, datetime.now())     # creating guest
        await rqr.add_user(message.from_user.id)     # creating user blank subjects list
        await message.reply(f'Привет <b>{message.from_user.first_name}</b>! Я бот для отслеживания успеваемости.\n'
                            'Если нужна подробная помощь 👉 /help\n\n'
                            'Готов добавить предметы сейчас?', reply_markup=kbr.yes_no)


# register
@router_register.message(Command('register'))
async def register(message: Message):
    user_exist = await check_user_registrasted(message.from_user.id)
    if user_exist == 1:
        await message.answer('Хочешь добавить/удалить свои предметы?', reply_markup=kbr.yes_no)
    else:
        await rqr.add_user(message.from_user.id)     # creating user blank subjects list
        await message.answer('Уверен?', reply_markup=kbr.yes_no)


@router_register.callback_query(F.data == 'yes')
async def yes(query: CallbackQuery):
    await query.message.answer(f'Список предметов, которые ты выбрал 📃:\n{await rqr.get_active_subjects_for_user(query.from_user.id)}'
                               , reply_markup=kbr.register)
    await query.message.answer('Чтобы закончить выбор, нажми на кнопку "💾 Сохранить и закончить выбор"', reply_markup=kbr.accept)
    await query.answer('✅')
    await query.message.edit_text('✅ Да')

@router_register.callback_query(F.data == 'no')
async def no(query: CallbackQuery):
    await query.answer('❌')
    await query.message.edit_text('❌ Нет')
    await query.message.answer('Продолжим...', reply_markup=main)


@router_register.message(F.text == '💾 Сохранить и закончить выбор')
async def save_and_end(message: Message):
    await message.answer('Выбранные предметы сохранены!', reply_markup=main)


@router_register.message(F.text == '🗑️ Очистить мой выбор')
async def clear(message: Message):
    await rqr.reset_all_subjects(message.from_user.id)
    await message.reply('Выбор предметов очищен\n(Список может не обновиться сразу, но он очищен)')