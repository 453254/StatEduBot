import os
import datetime
from asyncio import sleep
from aiogram import F, Router
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

import app.database.requests_stats as rqst
import app.stats.keyboard_stats as kbst
from app.stats.states_stats import ShowStat
from app.utils import formating_subjects
from app.stats.create_graph.generator_graph import graph_generator


stats_router = Router()

@stats_router.message(Command('showstats'))
@stats_router.message(F.text == '📈 Показать мою статистику')
async def shoose_subject_for_show(message: Message, state: FSMContext):
    await state.clear()
    if await rqst.check_user_subjects_resoults(message.from_user.id) == True:
        keyboard_add_resoult = await kbst.generate_add_resoult_keyboard(message.from_user.id)
        await message.answer('По какому предмету статистика?', reply_markup=keyboard_add_resoult)
        await state.set_state(ShowStat.choose_subj)
    else:
        await message.answer('Вы не добавили ни одного результата')

@stats_router.callback_query(ShowStat.choose_subj)
@stats_router.callback_query(F.data.in_(['math_stat', 'russian_stat', 'informatics_stat', 'physics_stat', 
                                            'chemistry_stat', 'biology_stat', 'geography_stat', 'history_stat', 'social_science_stat', 
                                            'literature_stat', 'english_stat', 'german_stat', 'french_stat', 'spanish_stat']))
async def show_subject_stat(query: CallbackQuery, state: FSMContext):
    if await state.get_state() == ShowStat.choose_subj:
        await query.answer(await formating_subjects(str(query.data)[:-5]))

        resoults_data = await rqst.get_resoults_data(query.from_user.id)
        average = await graph_generator(resoults_data, str(query.data)[:-5], query.from_user.id)

        path = f'plot_{datetime.date.today()}_{query.from_user.id}.png'

        await query.message.answer_photo(photo=FSInputFile(path=path), caption=f"Средний результат: ~{average} 😎")

        os.remove(f'plot_{datetime.date.today()}_{query.from_user.id}.png')