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
from keyboards.life_rudn_keyboards import main_life_rudn_keyboard, back_to_life_rudn_keyboard





router = Router()

setup_logging()




@router.callback_query(F.data == 'campus_life')
async def process_campus_life(callback: CallbackQuery):
    await callback.message.edit_text(
        text='''LEXICON_RU['campus_life']''',
        reply_markup=main_life_rudn_keyboard()
    )
    await callback.answer()

        # InlineKeyboardButton(text="🆕 Новости", callback_data='news_rudn'),
        # InlineKeyboardButton(text="🏠 Общежития", callback_data="dorm"),
        # InlineKeyboardButton(text="🏅 Спортиная жизнь", callback_data='sport_life'),
        # InlineKeyboardButton(text="🗓 Мероприятия", callback_data="events"),
        # InlineKeyboardButton(text="🤝 Профсоюзная организцация ", callback_data='profsouz'),
        # InlineKeyboardButton(text="🪪 МФЦ", callback_data='mfc_rudn'),
        # InlineKeyboardButton(text="💬 Форум студентов", url='https://t.me/RUDNCAMPUS'),
        # InlineKeyboardButton(text="📚 КДЦ РУДН", web_app=WebAppInfo(url='https://clinic.rudn.ru/')),
        # InlineKeyboardButton(text="🔙 Назад", callback_data="main_menu")

@router.callback_query(F.data == 'news_rudn')
async def process_news_rudn(callback: CallbackQuery):
    await callback.message.edit_text(
        text='''LEXICON_RU['news_rudn']''',
        reply_markup=back_to_life_rudn_keyboard()
    )
    await callback.answer()


@router.callback_query(F.data == 'sport_life')
async def process_sport_life(callback: CallbackQuery):
    await callback.message.edit_text(
        text='''LEXICON_RU['sport_life']''',
        reply_markup=back_to_life_rudn_keyboard()
    )
    await callback.answer()

@router.callback_query(F.data == 'events')
async def process_events(callback: CallbackQuery):
    await callback.message.edit_text(
        text='''LEXICON_RU['events']''',
        reply_markup=back_to_life_rudn_keyboard()
    )
    await callback.answer()


@router.callback_query(F.data == 'profsouz')
async def process_profsouz(callback: CallbackQuery):
    await callback.message.edit_text(
        text='''LEXICON_RU['profsouz']''',
        reply_markup=back_to_life_rudn_keyboard()
    )
    await callback.answer()

@router.callback_query(F.data == 'mfc_rudn')
async def process_mfc_rudn(callback: CallbackQuery):
    await callback.message.edit_text(
        text='''LEXICON_RU['mfc_rudn']''',
        reply_markup=back_to_life_rudn_keyboard()
    )
    await callback.answer()

