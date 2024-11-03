from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import app.database.requests_resoult as rqrs


async def generate_add_resoult_keyboard(tg_id):
    subjects_buttons = await rqrs.get_user_subjects(tg_id)

    register_keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=value, callback_data=key+'_stat') for key, value in subjects_buttons.items()][i:i+2] for i in range(0, len(subjects_buttons), 2)
    ])
    return register_keyboard