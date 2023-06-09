from aiogram.dispatcher.filters.state import State, StatesGroup


class ProfiEduDetails(StatesGroup):
	step1 = State()
	step2 = State()
	step3 = State()
	step4 = State()


class LyceumDetails(StatesGroup):
	step1 = State()
	step2 = State()
	step3 = State()