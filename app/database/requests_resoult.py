from app.database.models import async_session
from app.database.models import Users_Subject, User_Resoult
from sqlalchemy import select

async def check_user_subjects(tg_id):
    async with async_session() as session:
        user_subjects = await session.execute(select(Users_Subject).where(Users_Subject.tg_id == tg_id))
        user_subjects = user_subjects.scalars().first()
        if user_subjects:
            return True
        return False

async def get_user_subjects(tg_id):
    async with async_session() as session:
        user_subjects = await session.execute(select(Users_Subject).where(Users_Subject.tg_id == tg_id))
        user_subjects = user_subjects.scalars().first()
        subjects_translation = {
        'math': '➗ Математика',
        'russian': '🇷🇺 Русский язык',
        'informatics': '💽 Информатика',
        'physics': '⚙️ Физика',
        'chemistry': '🧪 Химия',
        'biology': '🧬 Биология',
        'geography': '🗺️ География',
        'history': '🏛️ История',
        'social_science': '💭 Обществознание',
        'literature': '📚 Литература',
        'english': '🇬🇧 Английский язык',
        'german': '🇩🇪 Немецкий язык',
        'french': '🇫🇷 Французский язык',
        'spanish': '🇪🇸 Испанский язык'
        }

        # dont ask what the f*** is it
    true_subjects_dict = {key: subjects_translation[key] for key, value in user_subjects.__dict__.items() 
                              if value is True and key in subjects_translation}


    return true_subjects_dict


async def add_user_resoult(tg_id, subject, resoult, date):
    async with async_session() as session:
        user_resoult = User_Resoult(tg_id=tg_id, subject=subject, resoult=resoult, date=date)
        session.add(user_resoult)
        await session.commit()