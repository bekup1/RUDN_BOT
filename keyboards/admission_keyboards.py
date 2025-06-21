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
    
    builder.adjust(1,1,1,1)
    
    return builder.as_markup()

def dorm_keyboard():
    builder = InlineKeyboardBuilder()

    inline_buttons: list[InlineKeyboardButton] = [
        InlineKeyboardButton(text=f'Общежитие_{i + 1}', callback_data=f'dorm_{i+1}') for i in range(15) 
    ]

    builder.row(*inline_buttons,width=3)

    builder.row(
    InlineKeyboardButton(text="📁 Докуемнты для заселения", callback_data="dorm_docs"),
    InlineKeyboardButton(text="🔙 Назад", callback_data="back")
    )

    return builder.as_markup()
