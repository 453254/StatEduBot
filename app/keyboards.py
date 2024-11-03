from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

yes_no = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='✅ Да', callback_data='yes')], 
    [InlineKeyboardButton(text='❌ Нет', callback_data='no')]
    ])

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='➕ Добавить результат'), KeyboardButton(text='🗑️ Удалить результат')],
    [KeyboardButton(text='📈 Показать мою статистику')],
    [KeyboardButton(text='📝 Управление списком предметов')],
    ],
    resize_keyboard=True,
    input_field_placeholder='Выберите пункт 👇')