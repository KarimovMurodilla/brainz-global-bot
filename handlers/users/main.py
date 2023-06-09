from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.inline import inline_buttons
from keyboards.default import keyboard_buttons

from loader import dp, db


# ---Start---
@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message, state: FSMContext):
    await state.finish()
    user = message.from_user
    user_in_db = await db.get_user(user.id)

    if not user_in_db:
        await db.reg_user(user.id, user.username, user.first_name)

    await message.answer("Assalomu aleykum!")