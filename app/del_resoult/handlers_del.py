from asyncio import sleep
from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from datetime import datetime, timedelta
from aiogram.fsm.context import FSMContext

from app.del_resoult.states_del import ChooseDel
from app.database.requests_stats import check_user_subjects_resoults
import app.keyboards as kb
import app.del_resoult.keyboard_del as kbdl
import app.database.requests_del as rqdl
from app.utils import formating_subjects


del_router = Router()

@del_router.message(Command('deleteres'))
@del_router.message(F.text == '🗑️ Удалить результат')
async def del_resoult(message: Message, state: FSMContext):
    await state.clear()
    if await check_user_subjects_resoults(message.from_user.id) == True:
        await state.set_state(ChooseDel.choose_del)
        del_keyboard = await kbdl.generate_add_resoult_keyboard(message.from_user.id)
        await message.answer('📋Все занесенные результаты:', reply_markup=del_keyboard)
    else:
        await message.answer('Вы не добавили ни одного результата')


@del_router.callback_query(F.data.in_([str(i) for i in range(99)]))
async def deleate_resoult(query: CallbackQuery, state: FSMContext):
    if await state.get_state() == ChooseDel.choose_del:
        if await rqdl.del_resoult(query.data) == True:
            await query.answer('Удалено 🚮')
            del_keyboard = await kbdl.generate_add_resoult_keyboard(query.from_user.id)
            await query.message.edit_reply_markup(reply_markup=del_keyboard)
        else: 
            await query.answer('Ошибка 🤷')
    else:
        await state.clear()