from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import ADMINS
from loader import dp, db, gs
from states.bundle import TalentSteps, RecruiterSteps


# ---Start---
@dp.message_handler(chat_id=ADMINS, commands='activity', state='*')
async def bot_start(message: types.Message, state: FSMContext):
    url = gs.get_url()
    await message.answer(url)