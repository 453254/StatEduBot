import os
import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from dotenv import load_dotenv

from app.choose_subjects_hendler import subject_choose_router
from app.handlers import router
from app.database.models import async_main

#TODO: 🗑️ Очистить мой выбор ломает всё и не работает + сделать чтобы когда нажимаешь на subjects (в списке register) внизу писало то, что ты уже выбрал


load_dotenv()
bot = Bot(token=os.getenv('TOKEN'))


async def main():
    await async_main()
    dp = Dispatcher()
    dp.include_router(router)
    dp.include_router(subject_choose_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        logging.basicConfig(level=logging.INFO)
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info('Бот остановлен!')
        exit(0)