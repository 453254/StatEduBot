from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from datetime import datetime
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import app.keyboards as kb
import app.database.requests as rq

subject_choose_router = Router()

# dont look here (realy (I warned you))
#TODO: find to way, how to make it less ugly


@subject_choose_router.callback_query(F.data == 'math')
async def math_handler(query: CallbackQuery):
    await rq.add_user_subject(query.from_user.id, 'math')
    await query.answer('➗ Математика')

@subject_choose_router.callback_query(F.data == 'russian')
async def russian_handler(query: CallbackQuery):
    await rq.add_user_subject(query.from_user.id, 'russian')
    await query.answer('🇷🇺 Русский язык')

@subject_choose_router.callback_query(F.data == 'informatics')
async def informatics_handler(query: CallbackQuery):
    await rq.add_user_subject(query.from_user.id, 'informatics')
    await query.answer('💽 Информатика')

@subject_choose_router.callback_query(F.data == 'physics')
async def physics_handler(query: CallbackQuery):
    await rq.add_user_subject(query.from_user.id, 'physics')
    await query.answer('⚙️ Физика')

@subject_choose_router.callback_query(F.data == 'chemistry')
async def chemistry_handler(query: CallbackQuery):
    await rq.add_user_subject(query.from_user.id, 'chemistry')
    await query.answer('🧪 Химия')

@subject_choose_router.callback_query(F.data == 'biology')
async def biology_handler(query: CallbackQuery):
    await rq.add_user_subject(query.from_user.id, 'biology')
    await query.answer('🧬 Биология')

@subject_choose_router.callback_query(F.data == 'geography')
async def geography_handler(query: CallbackQuery):
    await rq.add_user_subject(query.from_user.id, 'geography')
    await query.answer('🗺️ География')

@subject_choose_router.callback_query(F.data == 'history')
async def history_handler(query: CallbackQuery):
    await rq.add_user_subject(query.from_user.id, 'history')
    await query.answer('🏛️ История')

@subject_choose_router.callback_query(F.data == 'social_science')
async def social_science_handler(query: CallbackQuery):
    await rq.add_user_subject(query.from_user.id, 'social_science')
    await query.answer('💭 Обществознание')

@subject_choose_router.callback_query(F.data == 'literature')
async def literature_handler(query: CallbackQuery):
    await rq.add_user_subject(query.from_user.id, 'literature')
    await query.answer('📚 Литература')

@subject_choose_router.callback_query(F.data == 'english')
async def english_handler(query: CallbackQuery):
    await rq.add_user_subject(query.from_user.id, 'english')
    await query.answer('🇬🇧 Английский язык')

@subject_choose_router.callback_query(F.data == 'german')
async def german_handler(query: CallbackQuery):
    await rq.add_user_subject(query.from_user.id, 'german')
    await query.answer('🇩🇪 Немецкий язык')

@subject_choose_router.callback_query(F.data == 'french')
async def french_handler(query: CallbackQuery):
    await rq.add_user_subject(query.from_user.id, 'french')
    await query.answer('🇫🇷 Французский язык')

@subject_choose_router.callback_query(F.data == 'spanish')
async def spanish_handler(query: CallbackQuery):
    await rq.add_user_subject(query.from_user.id, 'spanish')
    await query.answer('🇪🇸 Испанский язык')