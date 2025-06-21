from aiogram.types import Message , CallbackQuery
from aiogram.filters import CommandStart 
from aiogram import Router, F
from lexicon.lexicon_ru import LEXICON_RU
import logging
from logging_setting.logging import setup_logging
from keyboards.main_keyboard import main_menu_keyboard
from keyboards.admission_keyboards import main_admission_keyboard


router = Router()

@router.message(CommandStart())
async def process_start_command(message:Message):
    await message.answer(text=LEXICON_RU['/start'],reply_markup=main_menu_keyboard())

@router.callback_query(F.data == 'admission')
async def process_button_2_press(callback: CallbackQuery):
    await callback.message.edit_text(
        text='Это раздел поступления, что вас интересует?',
        reply_markup= main_admission_keyboard()
    )

