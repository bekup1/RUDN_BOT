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

    builder.add(
        InlineKeyboardButton(text="💎 Мой РУДН", callback_data="my_rudn"),
        InlineKeyboardButton(text="🎓 Обучение", callback_data="education"),
        InlineKeyboardButton(text="📝 Поступление", callback_data="admission"),
        InlineKeyboardButton(text="❤️ Жизнь в РУДН", callback_data="campus_life"),
        InlineKeyboardButton(text="🌐 Официальный сайт", web_app=WebAppInfo(url="https://www.rudn.ru/")),
        InlineKeyboardButton(text="❓ Помощь", callback_data="help")
    )
    
    builder.adjust(2, 2, 1, 1)  
    
    return builder.as_markup()

