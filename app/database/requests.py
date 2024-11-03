from sqlalchemy import update
from app.database.models import async_session
from app.database.models import Users_Subject
from sqlalchemy import select


async def check_user_registrasted(tg_id):
    async with async_session() as session:
        result = await session.execute(select(Users_Subject).where(Users_Subject.tg_id == tg_id))
        user = result.scalars().first()
        return 1 if user else 0