from aiogram.types import Message 
from aiogram.filters import CommandStart
from aiogram import Router
from lexicon.lexicon_ru import LEXICON_RU
import logging
from logging_setting.logging import setup_logging
from keyboards.main_keyboard import main_menu_keyboard


router = Router()

@router.message(CommandStart())
async def process_start_command(message:Message):
    await message.answer(text=LEXICON_RU['/start'],reply_markup=main_menu_keyboard())
