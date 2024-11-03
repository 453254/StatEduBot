from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

import app.database.requests_del as rqdl


async def generate_add_resoult_keyboard(user):
    subjects_buttons = await rqdl.take_all_resoults(user)
    in_one_line = 3

    register_keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=value, callback_data=key) for key, value in subjects_buttons.items()]
        [i:i+in_one_line] for i in range(0, len(subjects_buttons), in_one_line)
    ])
    return register_keyboard