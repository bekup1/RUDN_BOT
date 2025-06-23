from aiogram.client.default import DefaultBotProperties
from aiogram.filters import Command
from aiogram.types import (
    Message, CallbackQuery,
    InlineKeyboardButton, InlineKeyboardMarkup,
    WebAppInfo)
import logging
from logging_setting.logging import setup_logging
from aiogram.utils.keyboard import InlineKeyboardBuilder






def main_my_rudn_keyboard():
    builder = InlineKeyboardBuilder()

    builder.add(
        InlineKeyboardButton(text="🎓 Моё Расписание", callback_data="my_shedule"),
        InlineKeyboardButton(text="📚 Мои Секции", callback_data="my_section"),
    #     InlineKeyboardButton(text="🏥 Мои Мероприятия", callback_data="ordinat"),
    #     InlineKeyboardButton(text="🏠 Мои Новости", callback_data="dorm"),
         InlineKeyboardButton(text="🔙 Назад", callback_data="main_menu")
     )
    
    builder.adjust(2,2,1)
    
    return builder.as_markup()

