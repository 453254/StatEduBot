from aiogram.fsm.state import StatesGroup, State

class RegisterSubjects(StatesGroup):
    subject = State()
    score = State()
    date = State()
    end = State()