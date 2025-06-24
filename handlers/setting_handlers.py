from aiogram.filters.callback_data import CallbackData
from typing import Any

from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram import Router, F
from lexicon.lexicon_ru import LEXICON_RU, LEXICON_COMMANDS, LEXICON_RU_ADMISSION
import logging
from logging_setting.logging import setup_logging
from keyboards.main_keyboard import main_menu_keyboard
from keyboards.setting_keyboard import (setting_section_keyboard , setting_institut_keyboard, setting_faculty_humanitarian_keyboard, 
                setting_faculty_foreign_languages_keyboard, back_to_my_rudn_keyboard,setting_faculty_math_computer_science_keyboard, setting_group_keyboard, setting_faculty_physics_technology_keyboard , User_setting_CallbackFactory)
from aiogram.types import FSInputFile
from database_my.database import user_db
from aiogram import handlers
from aiogram.types import Message
from aiogram import Router
from lexicon.lexicon_ru import LEXICON_RU

import logging

from logging_setting.logging import setup_logging



router = Router()

setup_logging()

identification: Any 


@router.message(Command(commands='setting'))
async def process_help_command(message: Message):

    await message.answer(text=f'выберите вашу секцию', reply_markup=setting_section_keyboard())
    
    if message.from_user.id  in user_db:

        user_db[message.from_user.id]['section'] = 'unknown'
        user_db[message.from_user.id]['institut'] = 'unknown'
        user_db[message.from_user.id]['faculty'] = 'unknown'
        user_db[message.from_user.id]['group'] = 'unknown'    



@router.callback_query(User_setting_CallbackFactory.filter(F.section != None))
async def process_section_press(callback: CallbackQuery,
                                 callback_data: User_setting_CallbackFactory):
    user_db[callback.from_user.id]['section'] = callback_data.section  

    await callback.message.edit_text(text="выберите ваш институт", reply_markup=setting_institut_keyboard())
    await callback.answer()






@router.callback_query(User_setting_CallbackFactory.filter(F.institut != None))
async def process_faculty_press(callback: CallbackQuery,
                                 callback_data: User_setting_CallbackFactory):
    user_db[callback.from_user.id]['institut'] = callback_data.institut  

    if callback_data.institut == 'humanitarian':
        await callback.message.edit_text(text="выберите ваш факультет", reply_markup=setting_faculty_humanitarian_keyboard())
    elif callback_data.institut == 'foreign_languages':
        await callback.message.edit_text(text="выберите ваш факультет", reply_markup=setting_faculty_foreign_languages_keyboard())
    elif callback_data.institut == 'math_computer_science':
        await callback.message.edit_text(text="выберите ваш факультет", reply_markup=setting_faculty_math_computer_science_keyboard())
    elif callback_data.institut == 'physics_technology':
        await callback.message.edit_text(text="выберите ваш факультет", reply_markup=setting_faculty_physics_technology_keyboard())
    
    await callback.answer()


@router.callback_query(User_setting_CallbackFactory.filter(F.faculty != None))
async def process_group_press(callback: CallbackQuery,
                                 callback_data: User_setting_CallbackFactory):
    user_db[callback.from_user.id]['program'] = callback_data.faculty  

    await callback.message.edit_text(text="выберите вашу группу", reply_markup=setting_group_keyboard())

    await callback.answer()

@router.callback_query(User_setting_CallbackFactory.filter(F.group != None))
async def process_group_press(callback: CallbackQuery,
                                 callback_data: User_setting_CallbackFactory):
    user_db[callback.from_user.id]['group'] = callback_data.group  

    await callback.message.edit_text(text="Вы успешно сохранили настройки. Ваши параметры:\n\n"
        f"Секция: {user_db[callback.from_user.id]['section']}\n"
        f"Институт: {user_db[callback.from_user.id]['institut']}\n"
        f"Программа: {user_db[callback.from_user.id]['program']}\n"
        f"Группа: {user_db[callback.from_user.id]['group']}\n\n\
            чтобы изменить данные, нажмите на /setting", reply_markup=back_to_my_rudn_keyboard())

    await callback.answer()

@router.callback_query(F.data == 'back_to_my_rudn')
async def process_back_to_my_rudn(callback: CallbackQuery):
    await callback.message.edit_text(text=LEXICON_RU['/my_rudn'] , reply_markup=main_menu_keyboard())
    await callback.answer()

