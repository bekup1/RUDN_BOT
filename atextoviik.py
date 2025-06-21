import logging
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import Command
from aiogram.types import (
    Message, CallbackQuery,
    InlineKeyboardButton, InlineKeyboardMarkup,
    WebAppInfo
)
from aiogram.utils.keyboard import InlineKeyboardBuilder
import asyncio

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Токен бота
BOT_TOKEN = "7395547960:AAGSpAKgd-9XWsXX42BTRCpJil5nR8YM2Tk"

# Инициализация бота и диспетчера
bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher()

# Клавиатура главного меню
def main_menu_keyboard():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="🎓 Факультеты", callback_data="faculties"),
        InlineKeyboardButton(text="📅 Расписание", callback_data="schedule")
    )
    builder.row(
        InlineKeyboardButton(text="📝 Поступление", callback_data="admission"),
        InlineKeyboardButton(text="🏛 Контакты", callback_data="contacts")
    )
    builder.row(
        InlineKeyboardButton(text="🌐 Официальный сайт", web_app=WebAppInfo(url="https://www.rudn.ru/")),
        InlineKeyboardButton(text="❓ Помощь", callback_data="help")
    )
    return builder.as_markup()

# Клавиатура факультетов
def faculties_keyboard():
    builder = InlineKeyboardBuilder()
    faculties = [
        "Инженерный факультет",
        "Факультет физико-математических наук",
        "Филологический факультет",
        "Экономический факультет",
        "Юридический факультет",
        "Медицинский институт"
    ]
    for faculty in faculties:
        builder.add(InlineKeyboardButton(text=faculty, callback_data=f"faculty_{faculty}"))
    builder.adjust(1)
    builder.row(InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_main"))
    return builder.as_markup()

# Клавиатура расписания
def schedule_keyboard():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="Сегодня", callback_data="schedule_today"),
        InlineKeyboardButton(text="Завтра", callback_data="schedule_tomorrow"),
        InlineKeyboardButton(text="Неделя", callback_data="schedule_week")
    )
    builder.row(InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_main"))
    return builder.as_markup()

# Клавиатура поступления
def admission_keyboard():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="Бакалавриат", callback_data="admission_bachelor"),
        InlineKeyboardButton(text="Магистратура", callback_data="admission_master")
    )
    builder.row(
        InlineKeyboardButton(text="Аспирантура", callback_data="admission_phd"),
        InlineKeyboardButton(text="Документы", callback_data="admission_docs")
    )
    builder.row(InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_main"))
    return builder.as_markup()

# Обработчик команды /start
@dp.message(Command("start"))
async def cmd_start(message: Message):
    welcome_text = (
        "👋 Добро пожаловать в официальный бот РУДН!\n\n"
        "Здесь вы можете быстро получить доступ к основной информации университета. "
        "Выберите нужный раздел:"
    )
    await message.answer(welcome_text, reply_markup=main_menu_keyboard())

# Обработчик команды /help
@dp.message(Command("help"))
async def cmd_help(message: Message):
    help_text = (
        "ℹ️ Справка по использованию бота:\n\n"
        "Используйте кнопки меню для навигации по разделам.\n"
        "Основные разделы:\n"
        "- 🎓 Факультеты - информация о факультетах\n"
        "- 📅 Расписание - расписание занятий\n"
        "- 📝 Поступление - информация для абитуриентов\n"
        "- 🏛 Контакты - контактная информация\n\n"
        "Для возврата в главное меню используйте кнопку 'Назад'."
    )
    await message.answer(help_text)

# Обработчик инлайн кнопок
@dp.callback_query(lambda c: c.data == "back_to_main")
async def back_to_main(callback: CallbackQuery):
    await callback.message.edit_text(
        "Выберите нужный раздел:",
        reply_markup=main_menu_keyboard()
    )
    await callback.answer()

@dp.callback_query(lambda c: c.data == "faculties")
async def show_faculties(callback: CallbackQuery):
    await callback.message.edit_text(
        "🎓 Выберите факультет:",
        reply_markup=faculties_keyboard()
    )
    await callback.answer()

@dp.callback_query(lambda c: c.data.startswith("faculty_"))
async def show_faculty_info(callback: CallbackQuery):
    faculty_name = callback.data.split("_", 1)[1]
    await callback.message.edit_text(
        f"Информация о факультете: {faculty_name}\n\n"
        "Подробнее: https://www.rudn.ru/",
        reply_markup=faculties_keyboard()
    )
    await callback.answer()

@dp.callback_query(lambda c: c.data == "schedule")
async def show_schedule_options(callback: CallbackQuery):
    await callback.message.edit_text(
        "📅 Выберите период для расписания:",
        reply_markup=schedule_keyboard()
    )
    await callback.answer()

@dp.callback_query(lambda c: c.data.startswith("schedule_"))
async def show_schedule(callback: CallbackQuery):
    period = callback.data.split("_", 1)[1]
    periods = {
        "today": "сегодня",
        "tomorrow": "завтра",
        "week": "на неделю"
    }
    await callback.message.edit_text(
        f"Расписание занятий {periods.get(period, '')}:\n\n"
        "Здесь будет информация о расписании...\n"
        "Полное расписание: https://www.rudn.ru/schedule",
        reply_markup=schedule_keyboard()
    )
    await callback.answer()

@dp.callback_query(lambda c: c.data == "admission")
async def show_admission_options(callback: CallbackQuery):
    await callback.message.edit_text(
        "📝 Информация для абитуриентов:",
        reply_markup=admission_keyboard()
    )
    await callback.answer()

@dp.callback_query(lambda c: c.data.startswith("admission_"))
async def show_admission_info(callback: CallbackQuery):
    admission_type = callback.data.split("_", 1)[1]
    types_info = {
        "bachelor": "Бакалавриат",
        "master": "Магистратура",
        "phd": "Аспирантура",
        "docs": "Необходимые документы"
    }
    await callback.message.edit_text(
        f"Информация о поступлении ({types_info.get(admission_type, '')}):\n\n"
        "Подробнее: https://www.rudn.ru/admission",
        reply_markup=admission_keyboard()
    )
    await callback.answer()

@dp.callback_query(lambda c: c.data == "contacts")
async def show_contacts(callback: CallbackQuery):
    contacts_text = (
        "🏛 Контактная информация РУДН:\n\n"
        "📞 Телефон: +7 (495) 787-38-03\n"
        "📧 Email: info@rudn.ru\n"
        "📍 Адрес: 117198, Москва, ул. Миклухо-Маклая, 6\n\n"
        "🌐 Сайт: https://www.rudn.ru/\n"
        "🚇 Ближайшее метро: Юго-Западная"
    )
    await callback.message.edit_text(
        contacts_text,
        reply_markup=main_menu_keyboard()
    )
    await callback.answer()

@dp.callback_query(lambda c: c.data == "help")
async def show_help(callback: CallbackQuery):
    await cmd_help(callback.message)
    await callback.answer()

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())