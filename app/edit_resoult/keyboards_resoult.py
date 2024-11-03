from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

import app.database.requests_resoult as rqrs


async def generate_add_resoult_keyboard(user):
    subjects_buttons = await rqrs.get_user_subjects(user)

    register_keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=value, callback_data=key+'_add') for key, value in subjects_buttons.items()][i:i+2] for i in range(0, len(subjects_buttons), 2)
    ])
    return register_keyboard

date = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сегодня', callback_data='today'),
     InlineKeyboardButton(text='Вчера', callback_data='yesterday')],
])