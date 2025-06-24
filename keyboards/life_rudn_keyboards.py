from aiogram.client.default import DefaultBotProperties
from aiogram.filters import Command
from aiogram.types import (
    Message, CallbackQuery,
    InlineKeyboardButton, InlineKeyboardMarkup,
    WebAppInfo)

import logging
from logging_setting.logging import setup_logging
from aiogram.utils.keyboard import InlineKeyboardBuilder


def main_life_rudn_keyboard():
    builder = InlineKeyboardBuilder()

    builder.add(
        InlineKeyboardButton(text="🆕 Новости", callback_data='news_rudn'),
        InlineKeyboardButton(text="🏠 Общежития", callback_data="dorm"),
        InlineKeyboardButton(text="🏅 Спортиная жизнь", callback_data='sport_life'),
        InlineKeyboardButton(text="🗓 Мероприятия", callback_data="events"),
        InlineKeyboardButton(text="🤝 Профсоюзная организцация ", callback_data='profsouz'),
        InlineKeyboardButton(text="🪪 МФЦ", callback_data='mfc_rudn'),
        InlineKeyboardButton(text="💬 Форум студентов", url='https://t.me/RUDNCAMPUS'),
        InlineKeyboardButton(text="📚 КДЦ РУДН", web_app=WebAppInfo(url='https://clinic.rudn.ru/')),
        InlineKeyboardButton(text="🔙 Назад", callback_data="main_menu")
    )



    builder.adjust(2, 2, 2, 2, 1)

    return builder.as_markup()



def back_to_life_rudn_keyboard():
    builder = InlineKeyboardBuilder()

    builder.add(
        InlineKeyboardButton(text="🔙 Назад", callback_data="campus_life")
    )

    return builder.as_markup()

