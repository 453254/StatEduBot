import os
import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from dotenv import load_dotenv

from app.register.add_subjects_register import subject_choose_router
from app.register.hendlers_register import router_register
from app.edit_resoult.handlers_resoult import router_resoult
from app.stats.handlers_stats import stats_router
from app.handlers import router
from app.database.models import async_main
from app.del_resoult.handlers_del import del_router

load_dotenv()
bot = Bot(token=os.getenv('TOKEN'))




async def main():
    await async_main()

    dp = Dispatcher()
    dp.include_routers(router_resoult, router, router_register, subject_choose_router, del_router, stats_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        logging.basicConfig(level=logging.INFO)
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info('Бот остановлен!')