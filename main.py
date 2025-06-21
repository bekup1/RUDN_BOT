import aiogram
import asyncio
from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from logging_setting.logging import setup_logging
from aiogram.enums import ParseMode
from config_data.config import Config , load_config
from handlers import other_handlers, user_handlers
import logging

setup_logging()

config: Config = load_config()
logging.info('config successfully config')

    # Инициализируем бот и диспетчер
bot = Bot(token=config.tg_bot.token)
dp = Dispatcher()

dp.include_router(user_handlers.router)
logging.info('bot catched some command from his arsenal and router imported and worked')
dp.include_router(other_handlers.router)
logging.debug('hadlers stopped work')




if __name__ == '__main__':
    dp.run_polling(bot)
    logging.debug('start_polling')
else:
    logging.error('code doesnt start and file not such a main')
    






