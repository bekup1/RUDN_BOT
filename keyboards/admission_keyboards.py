from aiogram.client.default import DefaultBotProperties
from aiogram.filters import Command
from aiogram.types import (
    Message, CallbackQuery,
    InlineKeyboardButton, InlineKeyboardMarkup,
    WebAppInfo)
import logging
from logging_setting.logging import setup_logging
from aiogram.utils.keyboard import InlineKeyboardBuilder


def main_admission_keyboard():
    builder = InlineKeyboardBuilder()

    builder.add(
        InlineKeyboardButton(text="🏠 Общежитие", callback_data="dorm"),
        InlineKeyboardButton(text="📝 Документы", callback_data="admission_docs"),
        InlineKeyboardButton(text="🧮 Калькулятор баллов ЕГЭ", callback_data="calculator" ),
        InlineKeyboardButton(text="🔙 Назад", callback_data="back")
    )
    
    
    return builder.as_markup()