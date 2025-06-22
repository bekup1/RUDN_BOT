import aiogram
import asyncio
from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from logging_setting.logging import setup_logging
from aiogram.enums import ParseMode
from config_data.config import Config , load_config
from handlers import other_handlers, user_handlers
import logging
from keyboards.menu_keyboards import set_main_menu

setup_logging()




# Функция конфигурирования и запуска бота
async def main():
    config: Config = load_config()
    logging.info('config successfully config')

        # Инициализируем бот и диспетчер
    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher()

    await set_main_menu(bot)


    dp.include_router(user_handlers.router)
    logging.info('bot catched some command from his arsenal and router imported and worked')
    dp.include_router(other_handlers.router)
    logging.debug('hadlers stopped work')
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    logging.info('start polling')



asyncio.run(main())



    





