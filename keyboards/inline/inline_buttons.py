from aiogram import types


def select_lang():
    menu = types.InlineKeyboardMarkup(row_width=2)
    menu.add()

    return menu