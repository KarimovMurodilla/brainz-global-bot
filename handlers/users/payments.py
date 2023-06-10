from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.inline import inline_buttons
from keyboards.default import keyboard_buttons

from loader import dp


@dp.message_handler(commands='payments', state='*')
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer(
        "Выберите удобный тариф:\n"
        "Base - 1 вакансия с картинкой. Охват более 5k\n"
        "Premium - до 8  вакансий и база кандидатов с дублированием\n"
        "Enterprise - Если у вашей компании более 20 вакансий в месяц мы предлагаем индивидуальную цену", 
    reply_markup=inline_buttons.payment())



# ---Payments---
@dp.callback_query_handler(text_contains='PAYMENT_ID_1', state='*')
async def payment_1000(c: types.CallbackQuery, state: FSMContext):
    PRICE = types.LabeledPrice(label="Test", amount=100000)

    await dp.bot.send_invoice(
        chat_id=c.from_user.id,
        title="Test titile",
        description = "Base - 1 вакансия с картинкой. Охват более 5k\n",
        provider_token="371317599:TEST:1686412892936",
        currency="UZS",
        prices=[PRICE],
        payload="test-payload"
    )


@dp.callback_query_handler(text_contains='PAYMENT_ID_2', state='*')
async def payment_5000(c: types.CallbackQuery, state: FSMContext):
    PRICE = types.LabeledPrice(label="Test", amount=500000)

    await dp.bot.send_invoice(
        chat_id=c.from_user.id,
        title="Test titile",
        description="Premium - до 8  вакансий и база кандидатов с дублированием\n",
        provider_token="371317599:TEST:1686412892936",
        currency="UZS",
        prices=[PRICE],
        payload="test-payload"
    )