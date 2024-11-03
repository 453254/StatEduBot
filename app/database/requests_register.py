from sqlalchemy import update
from app.database.models import async_session
from app.database.models import Users_Subject, Guest
from sqlalchemy import select


# func for add guests, who clicked on /start
async def guest(tg_id):
    async with async_session() as session:
        guest = Guest(tg_id=tg_id)
        session.add(guest)
        await session.commit()
# func to check if user was guest yet
async def check_user_started(tg_id):
    async with async_session() as session:
        result = await session.execute(select(Guest).where(Guest.tg_id == tg_id))
        user = result.scalars().first()
        return 1 if user else 0


# func to check if user was in subject db yet
async def user_in_subjects(tg_id):
    async with async_session() as session:
        result = await session.execute(select(Users_Subject).where(Users_Subject.tg_id == tg_id))
        user = result.scalars().first()
        return 1 if user else 0

async def reset_all_subjects(tg_id):    # func for reseting all user subjects
    async with async_session() as session:
        user = await session.execute(select(Users_Subject).where(Users_Subject.tg_id == tg_id))
        user = user.scalars().first()
        if not user:
            user = Users_Subject(tg_id=tg_id)
            session.add(user)
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

async def add_user_subjects(tg_id, subjects):
    async with async_session() as session:
        user = await session.execute(select(Users_Subject).where(Users_Subject.tg_id == tg_id))
        user = user.scalars().first()
        if not user:
            user = Users_Subject(tg_id=tg_id)
            session.add(user)
        for subject in subjects:
            setattr(user, subject, True)
        await session.commit()