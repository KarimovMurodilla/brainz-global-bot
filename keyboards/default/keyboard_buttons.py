from aiogram import types


def show_role():
    menu = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn1 = types.KeyboardButton("Я талант")
    btn2 = types.KeyboardButton("Я компания/рекрутер")
    menu.add(btn1, btn2)

    return menu


def i_am_freelancer():
    menu = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn1 = types.KeyboardButton("Я рекрутер фрилансер")
    menu.add(btn1)

    return menu