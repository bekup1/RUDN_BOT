from aiogram import handlers
from aiogram.types import Message
from aiogram import Router
from lexicon.lexicon_ru import LEXICON_RU

import logging

from logging_setting.logging import setup_logging

router = Router()

@router.message()
async def send_answer(message:Message):
    await message.answer(text=LEXICON_RU['other_answer'])
    logging.info('bot catch indefined message')

