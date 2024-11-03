from sqlalchemy import update
from app.database.models import async_session
from app.database.models import User_Resoult
from sqlalchemy import select
from app.utils import formating_subjects

async def take_all_resoults(tg_id: int):
    async with async_session() as session:
        async with session.begin():
            result = await session.execute(select(User_Resoult).where(User_Resoult.tg_id == tg_id))
            user_results = result.scalars().all()
            results_dict = {
                str(user_resoult.id): f"{str(await formating_subjects(user_resoult.subject))[:2]} {user_resoult.resoult} {str(user_resoult.date.strftime('%Y-%m-%d'))[5:]}"
                for user_resoult in user_results
            }
            return results_dict

async def del_resoult(id):
    async with async_session() as session:
        async with session.begin():
            # Находим запись по id
            stmt = select(User_Resoult).where(User_Resoult.id == id)
            result = await session.execute(stmt)
            user_result = result.scalars().first()
            if user_result:
                await session.delete(user_result)
                await session.commit()
                return True
            return False
