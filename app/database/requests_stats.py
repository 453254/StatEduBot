from app.database.models import async_session
from app.database.models import User_Resoult
from sqlalchemy import select

async def check_user_subjects_resoults(tg_id):
    async with async_session() as session:
        result = await session.execute(select(User_Resoult).where(User_Resoult.tg_id == tg_id))
        user = result.scalars().first()
        return True if user else False


async def get_resoults_data(tg_id):
    async with async_session() as session:
        async with session.begin():
            result = await session.execute(select(User_Resoult).where(User_Resoult.tg_id == tg_id))
            user_results = result.scalars().all()
            results_list = [
                {
                    'resoult': int(user_resoult.resoult),
                    'subject': str(user_resoult.subject),
                    'date': str(user_resoult.date.strftime('%Y-%m-%d'))
                }
                for user_resoult in user_results
            ]
            return results_list
