from aiogram.client.default import DefaultBotProperties
from aiogram.filters import Command
from aiogram.types import (
    Message, CallbackQuery,
    InlineKeyboardButton, InlineKeyboardMarkup,
    WebAppInfo)
import logging
from logging_setting.logging import setup_logging
from aiogram.utils.keyboard import InlineKeyboardBuilder


def main_study_keyboard():
    builder = InlineKeyboardBuilder()

    builder.add(
        InlineKeyboardButton(text="📚 ТУИС", web_app=WebAppInfo(url='https://esystem.rudn.ru/')),
        InlineKeyboardButton(text="📖 Библиотека",web_app=WebAppInfo(url='https://mega.rudn.ru/MegaPro/Web' )),
        InlineKeyboardButton(text="🗓 Расписание занятий", callback_data="study_schedule"),
        InlineKeyboardButton(text="💬 Форум студентов", url='https://t.me/RUDNCAMPUS'),
        InlineKeyboardButton(text="🔙 Назад", callback_data="main_menu")
    )

    builder.adjust(2, 2, 1)   

    return builder.as_markup()