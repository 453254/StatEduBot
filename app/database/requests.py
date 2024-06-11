from sqlalchemy import update
from app.database.models import async_session
from app.database.models import Users_Subject
from sqlalchemy import select


async def check_user_exists(tg_id):
    async with async_session() as session:
        result = await session.execute(select(Users_Subject).where(Users_Subject.tg_id == tg_id))
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


