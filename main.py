

config: Config = load_config()
logging.info('config successfully config')

    # Инициализируем бот и диспетчер
bot = Bot(token=config.tg_bot.token)
dp = Dispatcher()

амввма
мавмвам
вам
ва
мав
м
вам
авм
ва
мав
ма
в


if __name__ == '__main__':
    dp.run_polling(bot)
    logging.debug('start_polling')
else:
    logging.error('code doesnt start and file not such a main')
    






