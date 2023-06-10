from aiogram.dispatcher.filters.state import State, StatesGroup


class TalentSteps(StatesGroup):
	step1 = State()


class RecruiterSteps(StatesGroup):
	step1 = State()
	step2 = State()
	step3 = State()