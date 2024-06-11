from sqlalchemy import update
from app.database.models import async_session
from app.database.models import Users_Subject
from sqlalchemy import select


async def check_user_registrasted(tg_id):
    async with async_session() as session:
        result = await session.execute(select(Users_Subject).where(Users_Subject.tg_id == tg_id))
        user = result.scalars().first()
        return 1 if user else 0


async def get_active_subjects_for_user(tg_id):
    async with async_session() as session:
        user_subjects = await session.execute(select(Users_Subject).where(Users_Subject.tg_id == tg_id))
        user_subjects = user_subjects.scalars().first()
        if not user_subjects:
            return 'Вы еще не выбрали предметы 😔\nВыберите их в меню ниже 👇'
        subjects = [
            "➗ Математика" if user_subjects.math else None,
            "🇷🇺 Русский язык" if user_subjects.russian else None,
            "💽 Информатика" if user_subjects.informatics else None,
            "⚙️ Физика" if user_subjects.physics else None,
            "🧪 Химия" if user_subjects.chemistry else None,
            "🧬 Биология" if user_subjects.biology else None,
            "🗺️ География" if user_subjects.geography else None,
            "🏛️ История" if user_subjects.history else None,
            "💭 Обществознание" if user_subjects.social else None,
            "📚 Литература" if user_subjects.literature else None,
            "🇬🇧 Английский язык" if user_subjects.english else None,
            "🇩🇪 Немецкий язык" if user_subjects.german else None,
            "🇫🇷 Французский язык" if user_subjects.french else None,
            "🇪🇸 Испанский язык" if user_subjects.spanish else None,
        ]
        return '\n'.join([subject for subject in subjects if subject])