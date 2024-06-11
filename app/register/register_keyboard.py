from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

yes_no = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='✅ Да', callback_data='yes')], 
    [InlineKeyboardButton(text='❌ Нет', callback_data='no')]
    ])

register = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='➗ Математика', callback_data='math'), InlineKeyboardButton(text='🇷🇺 Русский язык', callback_data='russian')],
    [InlineKeyboardButton(text='💽 Информатика', callback_data='informatics'), InlineKeyboardButton(text='⚙️ Физика', callback_data='physics')],
    [InlineKeyboardButton(text='🧪 Химия', callback_data='chemistry'), InlineKeyboardButton(text='🧬 Биология', callback_data='biology')],
    [InlineKeyboardButton(text='🗺️ География', callback_data='geography'), InlineKeyboardButton(text='🏛️ История', callback_data='history')],
    [InlineKeyboardButton(text='💭 Обществознание', callback_data='social_science'), InlineKeyboardButton(text='📚 Литература', callback_data='literature')],
    [InlineKeyboardButton(text='🇬🇧 Английский язык', callback_data='english'), InlineKeyboardButton(text='🇩🇪 Немецкий язык', callback_data='german')],
    [InlineKeyboardButton(text='🇫🇷 Французский язык', callback_data='french'), InlineKeyboardButton(text='🇪🇸 Испанский язык', callback_data='spanish')]
])

accept = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='💾 Сохранить и закончить выбор')],
    [KeyboardButton(text='🗑️ Очистить мой выбор')]
    ],  
    resize_keyboard=True, 
    input_field_placeholder='Выберите предметы, которые хотите отслеживать 👆')
