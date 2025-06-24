from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram import Router, F
from lexicon.lexicon_ru import LEXICON_RU, LEXICON_COMMANDS, LEXICON_RU_ADMISSION
import logging
from logging_setting.logging import setup_logging
from keyboards.main_keyboard import main_menu_keyboard
from keyboards.study_keyboard import main_study_keyboard
from aiogram.types import FSInputFile
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram import Router, F
from lexicon.lexicon_ru import LEXICON_RU, LEXICON_COMMANDS, LEXICON_RU_ADMISSION
import logging
from logging_setting.logging import setup_logging
from keyboards.main_keyboard import main_menu_keyboard 

from keyboards.setting_keyboard import back_to_my_rudn_keyboard
from database_my.database import user_db 

from keyboards.my_rudn_keyboards import main_my_rudn_keyboard 
from aiogram.types import FSInputFile
from keyboards.life_rudn_keyboards import main_life_rudn_keyboard


router = Router()

@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'], reply_markup=main_menu_keyboard())
    if message.from_user.id not in user_db:
        user_db[message.from_user.id] = {
            'section': 'unknown',
            'institut': 'unknown',
            'program': 'unknown',
            'group': 'unknown'
                    }

@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'], reply_markup=main_menu_keyboard())
    


@router.callback_query(F.data == 'education')
async def process_dorm_docs(callback: CallbackQuery):
    await callback.message.edit_text(
        text=LEXICON_RU['education'],
        reply_markup=main_study_keyboard()
    )
    await callback.answer()

@router.callback_query(F.data == 'my_rudn')
async def process_my_rudn(callback: CallbackQuery):
    await callback.message.edit_text(
        text=LEXICON_RU['my_rudn'] + f"\n\nВаши текущие данные:\n"
        f"Секция: {user_db[callback.from_user.id]['section']}\n"
        f"Институт: {user_db[callback.from_user.id]['institut']}\n"
        f"Программа: {user_db[callback.from_user.id]['program']}\n"
        f"Группа: {user_db[callback.from_user.id]['group']}\n\n\
            чтобы изменить данные, нажмите на /setting"
            
        ,
        reply_markup=main_my_rudn_keyboard()
    )
    await callback.answer()

@router.callback_query(F.data == 'my_shedule')
async def process_my_shedule(callback: CallbackQuery):
    await callback.message.edit_text(
        text='когда разработчик выучит базы данных, то тут будет ваше расписание на основе вашей учебной группы',
        reply_markup=back_to_my_rudn_keyboard()
    )
    await callback.answer()

@router.callback_query(F.data == 'my_section')
async def process_my_section(callback: CallbackQuery):
    await callback.message.edit_text(
        text='когда разработчик выучит базы данных, то тут будет ваша секция на основе вашей секции и учебной группы',
        reply_markup=back_to_my_rudn_keyboard()
    )
    await callback.answer()


@router.callback_query(F.data == 'navigation')
async def process_navigation(callback: CallbackQuery):
    await callback.message.edit_text(
        text=LEXICON_RU['navigation'],
        reply_markup=main_menu_keyboard()
    )
    await callback.answer()