from asyncio import sleep
from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from datetime import datetime, timedelta
from aiogram.fsm.context import FSMContext

from app.edit_resoult.states_resoult import RegisterSubjects
from app.database.requests_resoult import check_user_subjects
import app.keyboards as kb
import app.edit_resoult.keyboards_resoult as kbrs
import app.database.requests_resoult as rqrs
from app.utils import formating_subjects

router_resoult = Router()


@router_resoult.message(Command('resoult'))
@router_resoult.message(F.text == '➕ Добавить результат')
async def start_resoult(message: Message, state: FSMContext):
    await state.clear()
    if await check_user_subjects(message.from_user.id) == True:
        await state.set_state(RegisterSubjects.subject)
        add_resoult_keyboard = await kbrs.generate_add_resoult_keyboard(message.from_user.id)
        await message.answer("По какому предмету результат?", reply_markup=add_resoult_keyboard)
    else:
        await message.answer("Нет ниодного предмета 🫙")



@router_resoult.callback_query(RegisterSubjects.subject and F.data.in_(['math_add', 'russian_add', 'informatics_add', 'physics_add', 
                                            'chemistry_add', 'biology_add', 'geography_add', 'history_add', 'social_science_add', 
                                            'literature_add', 'english_add', 'german_add', 'french_add', 'spanish_add']))
async def choose_subject_for_add(query: CallbackQuery, state: FSMContext):
    if await state.get_state() == RegisterSubjects.subject:
        await query.answer(await formating_subjects(str(query.data)[:-4]))
        await query.message.answer('Какой балл?\n0 до 100')
        await state.update_data(subject=query.data)
        await state.set_state(RegisterSubjects.score)
    else:
        await state.clear()



@router_resoult.message(RegisterSubjects.score)
async def score(message: Message, state: FSMContext):
    if await state.get_state() == RegisterSubjects.score:
        if message.text.isdigit() and 0 <= int(message.text) <= 100:
            await state.set_state(RegisterSubjects.date)
            await state.update_data(score=message.text)
            await message.answer('Введи дату в формате гггг-мм-дд\n(оч важно именно так)', reply_markup=kbrs.date)
        else:
            await message.answer('Введите число от 0 до 100')
    else:
        await state.clear()


@router_resoult.callback_query(RegisterSubjects.date)
@router_resoult.callback_query(F.data.in_(['today', 'yesterday']))
async def choose_date(query: CallbackQuery, state: FSMContext):
    if await state.get_state() == RegisterSubjects.date:
        if query.data == 'today':
            await query.answer('Сегодня 🏙️')
            date = datetime.now().date()
        if query.data == 'yesterday':
            await query.answer('Вчера 🌆')
            date = datetime.now().date() - timedelta(days=1)
        await state.update_data(date=date)
        await state.set_state(RegisterSubjects.end)
        data = await state.get_data()
        subj = await formating_subjects(str(data['subject'])[:-4])

        await query.message.answer(f"Предмет: {subj}\nБалл: {data['score']}\nДата: {data['date']}", reply_markup=kb.main)
        await query.message.answer('Все верно?', reply_markup=kb.yes_no)
    else:
        await state.clear()


@router_resoult.message(RegisterSubjects.date)
async def date(message: Message, state: FSMContext):
    if await state.get_state() == RegisterSubjects.date:
        try:
            parsed_date = datetime.strptime(message.text, '%Y-%m-%d').date()
            await state.update_data(date=parsed_date)
            
            data = await state.get_data()

            subj = await formating_subjects(str(data['subject'])[:-4])

            await message.answer(f"Предмет: {subj}\nБалл: {data['score']}\nДата: {data['date']}", reply_markup=kb.main)
            await message.answer('Все верно?', reply_markup=kb.yes_no)
            await state.set_state(RegisterSubjects.end)
        except ValueError:
            await message.answer('Введите дату в формате гггг-мм-дд\n(очень важно именно так)')
    else:
        await state.clear()


@router_resoult.callback_query(RegisterSubjects.end)
async def check_resoult(query: CallbackQuery, state: FSMContext):
    if await state.get_state() == RegisterSubjects.end:
        await query.answer('Всё 📋')
        if query.data == 'yes':
            data = await state.get_data()

            await rqrs.add_user_resoult(query.from_user.id, str(data['subject'])[:-4], data['score'], data['date'])
            await query.message.edit_text('Сохранено 💾')
            await state.clear()
        if query.data == 'no':
            await query.message.edit_text('Отменено ❌')
            await state.clear()
    else:
        await state.clear()