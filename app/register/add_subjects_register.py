from aiogram import F, Router
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from app.register.keyboard_register import reister
from app.register.states_register import RegisterSubjects

subject_choose_router = Router()


@subject_choose_router.callback_query(RegisterSubjects.subjects and F.data.in_(['math', 'russian', 'informatics', 'physics', 'chemistry', 'biology', 
                                                  'geography', 'history', 'social_science', 'literature', 'english', 
                                                  'german', 'french', 'spanish']))
async def subject_handler(query: CallbackQuery, state: FSMContext):
    if await state.get_state() == RegisterSubjects.subjects:
        subject = query.data    # get subject from callback data
        user_data = await state.get_data()  # get user data from state
        subjects = user_data.get('subjects', [])     # get subjects list from user data
        
        # collecting datas data for write it down in the database
        if subject not in subjects:
            subjects.append(subject)
            await state.update_data(subjects=subjects)

        subject_names = {
            "math": "➗ Математика",
            "russian": "🇷🇺 Русский язык",
            "informatics": "💽 Информатика",
            "physics": "⚙️ Физика",
            "chemistry": "🧪 Химия",
            "biology": "🧬 Биология",
            "geography": "🗺️ География",
            "history": "🏛️ История",
            "social_science": "💭 Обществознание",
            "literature": "📚 Литература",
            "english": "🇬🇧 Английский язык",
            "german": "🇩🇪 Немецкий язык",
            "french": "🇫🇷 Французский язык",
            "spanish": "🇪🇸 Испанский язык"}
        subjects_list_formatted = [subject_names[subject] for subject in subjects if subject in subject_names]
        subjects_string_formatted = '\n'.join(subjects_list_formatted)

        try:
            await query.message.edit_text(f"Предметы, которые ты выбрал 📃:\n{subjects_string_formatted}",
                                        reply_markup=reister)
            await query.answer(f'Вы выбрали предмет {subjects_list_formatted[-1]}\nЖелаю писать на 100 🍀🤞', show_alert=True)
        except Exception:   #TelegramBadRequest
            await query.answer(f'Предмет {subjects_list_formatted[-1]} уже выбран 😉\nЧтобы закончить жми "💾 Сохранить и закончить выбор"', show_alert=True)

        # Check if subject is already in the list, if not, add it
    else:
        await state.clear()