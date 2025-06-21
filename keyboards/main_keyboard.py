from aiogram.client.default import DefaultBotProperties
from aiogram.filters import Command
from aiogram.types import (
    Message, CallbackQuery,
    InlineKeyboardButton, InlineKeyboardMarkup,
    WebAppInfo)

import logging
from logging_setting.logging import setup_logging
from aiogram.utils.keyboard import InlineKeyboardBuilder



def main_menu_keyboard():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="🎓 Факультеты", callback_data="faculties"),
        InlineKeyboardButton(text="📅 Расписание", callback_data="schedule")
    )
    builder.row(
        InlineKeyboardButton(text="📝 Поступление", callback_data="admission"),
        InlineKeyboardButton(text="🏛 Контакты", callback_data="contacts")
    )
    builder.row(
        InlineKeyboardButton(text="🌐 Официальный сайт", web_app=WebAppInfo(url="https://www.rudn.ru/")),
        InlineKeyboardButton(text="❓ Помощь", callback_data="help")
    )
    return builder.as_markup()

