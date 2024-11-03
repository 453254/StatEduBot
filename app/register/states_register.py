from aiogram.fsm.state import StatesGroup, State

class RegisterSubjects(StatesGroup):
    keyboard_id = State()
    subjects = State()