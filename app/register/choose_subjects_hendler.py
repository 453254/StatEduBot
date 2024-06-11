from aiogram import F, Router
from aiogram.types import CallbackQuery

import app.database.register_requests as rqr
from app.database.requests import get_active_subjects_for_user
from app.register.register_keyboard import register

subject_choose_router = Router()

# this func was created by Copilot
@subject_choose_router.callback_query(F.data.in_(['math', 'russian', 'informatics', 'physics', 'chemistry', 'biology', 'geography', 'history', 'social_science', 'literature', 'english', 'german', 'french', 'spanish']))
async def subject_handler(query: CallbackQuery):
    subject = query.data
    await rqr.add_user_subject(query.from_user.id, subject)
    await query.answer(f'Вы выбрали {subject.capitalize()} 📚\nЖелаю писать на 100 🍀🤞', show_alert=True)
    await query.message.edit_text(f'Список предметов, которые ты выбрал 📃:\n{await get_active_subjects_for_user(query.from_user.id)}', reply_markup=register)
