from sqlalchemy import update
from app.database.models import async_session
from app.database.models import Users_Subject, Guest
from sqlalchemy import select


# func for add guests, who clicked on /start
async def guest(tg_id, date):
    async with async_session() as session:
        guest = await session.execute(select(Guest).where(Guest.tg_id == tg_id))
        guest = guest.scalars().first()
        if guest:
            first_time = False
        else:
            first_time = True
        guest = Guest(tg_id=tg_id, date=date, first_time=first_time)
        session.add(guest)
        await session.commit()


async def check_user_started(tg_id):
    async with async_session() as session:
        result = await session.execute(select(Guest).where(Guest.tg_id == tg_id))
        user = result.scalars().first()
        return 1 if user else 0


# idk how to create, edit and delete subjects in one func, so I'll just leave it like this 3 funcs
async def add_user(tg_id):    # func for adding user subject to db at firts time
    async with async_session() as session:
        user_id = Users_Subject(tg_id=tg_id)
        session.add(user_id)
        await session.commit()


async def reset_all_subjects(tg_id):    # func for reseting all user subjects
    async with async_session() as session:
        user = await session.execute(select(Users_Subject).where(Users_Subject.tg_id == tg_id))
        user = user.scalars().first()
        setattr(user, 'math', False)
        setattr(user, 'russian', False)
        setattr(user, 'informatics', False)
        setattr(user, 'physics', False)
        setattr(user, 'chemistry', False)
        setattr(user, 'biology', False)
        setattr(user, 'geography', False)
        setattr(user, 'history', False)
        setattr(user, 'social', False)
        setattr(user, 'literature', False)
        setattr(user, 'english', False)
        setattr(user, 'german', False)
        setattr(user, 'french', False)
        setattr(user, 'spanish', False)
        await session.commit()

async def add_user_subject(tg_id, subject):    # func for adding user subject to db
    async with async_session() as session:
        user = await session.execute(select(Users_Subject).where(Users_Subject.tg_id == tg_id))
        user = user.scalars().first()
        setattr(user, subject, True)
        await session.commit()


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