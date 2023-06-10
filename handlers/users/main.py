from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.inline import inline_buttons
from keyboards.default import keyboard_buttons

from loader import dp, db, gs
from states.bundle import TalentSteps, RecruiterSteps


# ---Start---
@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message, state: FSMContext):
    await state.finish()
    user = message.from_user
    user_in_db = await db.get_user(user.id)

    if not user_in_db:
        await db.reg_user(user.id, user.username, user.first_name)

    await message.answer("Выберите свою роль", reply_markup=keyboard_buttons.show_role())


# ---Talent---

@dp.message_handler(text="Я талант", state='*')
async def talent_section(message: types.Message):
    await message.answer("Введите ваше имя и фамилию", reply_markup=types.ReplyKeyboardRemove())
    await TalentSteps.step1.set()


@dp.message_handler(state=TalentSteps.step1)
async def process_talent_reg(message: types.Message, state: FSMContext):
    await message.answer(f"Отлично! {message.text}. Можете настраивать бота по своему усмотрению.")
    await db.reg_talent(message.from_user.id, message.text)

    users = await db.get_all_users()
    line = len(users) + 1
    gs.update_columns(line, message.from_user.username, message.text, "Талант")

    await state.finish()


# ---Recruiter---

@dp.message_handler(text="Я компания/рекрутер", state='*')
async def talent_section(message: types.Message):
    await message.answer("Введите ваше имя и фамилию", reply_markup=types.ReplyKeyboardRemove())
    await RecruiterSteps.step1.set()


@dp.message_handler(state=RecruiterSteps.step1)
async def process_talent_reg(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['fullname'] = message.text

    await message.answer(f"Введите название вашей компании в которую будете искать таланты. Если вы рекрутер фрилансер и ищите таланты для по заказу нажмите кнопку ниже",
        reply_markup=keyboard_buttons.i_am_freelancer()
    )
    await RecruiterSteps.next()


@dp.message_handler(state=RecruiterSteps.step2)
async def process_talent_reg(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        fullname = data['fullname']
        company = message.text

    await message.answer(f"Отлично! {fullname}. Можете настраивать бота по своему усмотрению.", reply_markup=types.ReplyKeyboardRemove())
    await db.reg_recruiter(message.from_user.id, fullname, company)

    users = await db.get_all_users()
    line = len(users) + 1
    gs.update_columns(line, message.from_user.username, fullname, "Рекрутер", company)

    await state.finish()