from aiogram import types


def payment():
    menu = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text="Base - 1000 рублей", callback_data="PAYMENT_ID_1")
    btn2 = types.InlineKeyboardButton(text="Premium - 5000 рублей", callback_data="PAYMENT_ID_2")
    btn3 = types.InlineKeyboardButton(text="Enterprise - Лично", callback_data='enterprise')

    menu.add(btn1, btn2, btn3)

    return menu