from asyncio import sleep
from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext

import app.register.keyboard_register as kbr
import app.database.requests_register as rqr
import app.keyboards as kb
from app.register.states_register import RegisterSubjects


router_register = Router()


# /start
@router_register.message(CommandStart())
async def start(message: Message, state: FSMContext):
    await state.clear()
    user_exist = await rqr.check_user_started(message.from_user.id)
    if user_exist == 0:
        await rqr.guest(message.from_user.id)     # add user to guest db

    await message.answer(
        f'Привет {message.from_user.first_name}! 😊\n'
        'Я бот для отслеживания изменения баллов по пробникам ЕГЭ. 📚📈\n'
        'Если нужна подробная помощь, нажми 👉 /help\n\n'
        'Чтобы начать пользоваться ботом, добавь предметы, результаты которых будешь записывать. 📝📚'
        'Можешь добавить свои предеметы прямо сейчас🧐 или потом по кнопке "📝 Управление списком предметов".'
                        , reply_markup=kb.main)
        
    await sleep(1.5)  # delay 1.5 seconds
    await message.answer('Готов добавить предметы сейчас?', reply_markup=kb.yes_no)


# register
@router_register.message(F.text == '📝 Управление списком предметов')
@router_register.message(Command('register'))
async def register(message: Message, state: FSMContext):
    await state.clear()
    await message.answer('Хочешь обновить свой список предметов?', reply_markup=kb.yes_no)
    

@router_register.callback_query(F.data == 'yes')
async def yes(query: CallbackQuery, state: FSMContext):
    await state.clear()

    sent_message = await query.message.answer(f'Список предметов, которые ты выбрал 📃:\nПока здесь пусто', reply_markup=kbr.reister)
    message_id = sent_message.message_id
    await state.update_data(keyboard_id=message_id)
    await query.message.answer('Чтобы закончить выбор, нажми на кнопку "💾 Сохранить и закончить выбор"', reply_markup=kbr.accept)
    await query.answer('✅')
    await query.message.edit_text('✅ Да')
    await state.set_state(RegisterSubjects.subjects)      #register starting


@router_register.callback_query(F.data == 'no')
async def no(query: CallbackQuery, state: FSMContext):
    await state.clear()
    await query.answer('❌')
    await query.message.edit_text('❌ Нет')
    await query.message.answer('Ладно 👀', reply_markup=kb.main)


from main import bot
@router_register.message(F.text == '💾 Сохранить и закончить выбор')
async def save_and_end(message: Message, state: FSMContext):
    if await state.get_state() == RegisterSubjects.subjects:
        data = await state.get_data()
        message_id = int(data.get("keyboard_id"))
        await rqr.reset_all_subjects(message.from_user.id)

        try: 
            user_subjects = data["subjects"]
        except KeyError:
            user_subjects = []
        
        if len(user_subjects) == 0:
            await message.answer('Список предметов пуст! Добавьте хотя бы один предмет!')
            return

        await bot.edit_message_reply_markup(chat_id=int(message.chat.id), message_id=message_id, reply_markup=None)

        await message.answer('Выбранные предметы сохранены!', reply_markup=kb.main)
        await rqr.add_user_subjects(message.from_user.id, user_subjects)
        await state.clear()      #register ending


@router_register.message(F.text == '🗑️ Очистить мой выбор')
async def clear(message: Message, state: FSMContext):
    if await state.get_state() == RegisterSubjects.subjects:
        await state.update_data(subjects=[])
        
        await message.reply('Список предметов очищен!\n'
                            'Можете продолжать')
    else:
        await state.clear()