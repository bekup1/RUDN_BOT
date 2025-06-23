from aiogram.client.default import DefaultBotProperties
from aiogram.filters import Command
from aiogram.types import (
    Message, CallbackQuery,
    InlineKeyboardButton, InlineKeyboardMarkup,
    WebAppInfo)
import logging
from logging_setting.logging import setup_logging
from aiogram.utils.keyboard import InlineKeyboardBuilder


def main_admission_keyboard():
    builder = InlineKeyboardBuilder()

    builder.add(
        InlineKeyboardButton(text="🎓 Бакалавриат", callback_data="bacalavr"),
        InlineKeyboardButton(text="📚 Магистратура", callback_data="magistr"),
        InlineKeyboardButton(text="🏥 Ординатура", callback_data="ordinat"),
        InlineKeyboardButton(text="🔬 Аспирантура", callback_data="aspirant"),
        InlineKeyboardButton(text="🏠 Общежитие", callback_data="dorm"),
        InlineKeyboardButton(text="🔙 Назад", callback_data="main_menu")
    )
    
    builder.adjust(2,2,1,1)
    
    return builder.as_markup()

def dorm_keyboard():
    builder = InlineKeyboardBuilder()

    inline_buttons: list[InlineKeyboardButton] = [
        InlineKeyboardButton(text=f'🏘 Общежитие {i + 1}', callback_data=f'dorm_{i+1}') for i in range(15) 
    ]

    builder.row(*inline_buttons,width=3)

    builder.row(
    InlineKeyboardButton(text="📄 Документы для заселения", callback_data="dorm_docs"),
    InlineKeyboardButton(text="🔄 Пошаговые действия для заселения", callback_data="dorm_steps_get"),
    InlineKeyboardButton(text="💳 Оплата общежития", callback_data="dorm_pay"),   
    InlineKeyboardButton(text="🔙 Назад", callback_data="admission"),
    width=1
    )

    return builder.as_markup()

def back_to_dorm_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔙 Назад", callback_data="dorm")]
    ])
    return keyboard

def bac_priem_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='💾 Сохранить фото', callback_data='save_bac_priem')
        ],
        [
            InlineKeyboardButton(text='🔙 Назад', callback_data='bacalavr')
        ]
    ])

def mag_sroki_priem_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='💾 Сохранить фото', callback_data='save_mag_sroki_priem')
        ],
        [
            InlineKeyboardButton(text='🔙 Назад', callback_data='magistr')
        ]
    ])

def bac_stipend_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='💾 Сохранить фото', callback_data='save_bac_stipend')
        ],
        [
            InlineKeyboardButton(text='🔙 Назад', callback_data='bacalavr')
        ]
    ])

def back_to_bacalavr():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔙 Назад", callback_data="bacalavr")]
    ])
    return keyboard
    
def back_to_mag():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔙 Назад", callback_data="magistr")]
    ])
    return keyboard

def back_to_asp():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔙 Назад", callback_data="aspirant")]
    ])
    return keyboard

def back_to_ord():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔙 Назад", callback_data="ordinat")]
    ])
    return keyboard

def bacavriat_keyboard():
    builder = InlineKeyboardBuilder()

    builder.row(
    InlineKeyboardButton(text="🧮 Калькулятор баллов ЕГЭ", callback_data="calculator"),
    InlineKeyboardButton(text="📅 Сроки приёма в бакалавриат и специалитет", callback_data="bac_priem"),   
    InlineKeyboardButton(text="📊 Проходные баллы прошлых лет", callback_data="bac_score_past"),
    InlineKeyboardButton(text="🏆 Индивидуальные достижения", callback_data="bac_individual"),
    InlineKeyboardButton(text="💰 Стипендиальная программа «Лига стипендий»", callback_data="bac_stipend"),
    InlineKeyboardButton(text="🔙 Назад", callback_data="admission"),
    width=1)
   
    return builder.as_markup()

def mag_admission_keyboard():
    builder = InlineKeyboardBuilder()

    builder.row(
    InlineKeyboardButton(text="🏛 Бюджет", callback_data="mag_budget"),
    InlineKeyboardButton(text="🎖 Грант", callback_data="mag_grant"),   
    InlineKeyboardButton(text="🎯 Целевое обучение", callback_data="mag_purpose_study"),
    InlineKeyboardButton(text="💵 Платное обучение", callback_data="mag_pay_study"),
    InlineKeyboardButton(text="🔙 Назад", callback_data="magistr"),
    width=1)
   
    return builder.as_markup()

def magistratura_keyboard():
    builder = InlineKeyboardBuilder()

    builder.row(
    InlineKeyboardButton(text="❓ Как поступить в магистратуру РУДН?", callback_data="mag_priem"),
    InlineKeyboardButton(text="📅 Сроки приёма в магистратуру", callback_data="mag_sroki"),   
    InlineKeyboardButton(text="🏆 Индивидуальные достижения", callback_data="mag_individ"),
    InlineKeyboardButton(text="💰 Стипендии для талантливых магистров", callback_data="mag_stipend"),
    InlineKeyboardButton(text="🔙 Назад", callback_data="admission"),
    width=1)

    return builder.as_markup()

def aspirantura_keyboard():
    builder = InlineKeyboardBuilder()

    builder.row(
    InlineKeyboardButton(text="📅 Сроки приёма в аспирантуру", callback_data="asp_sroki"),
    InlineKeyboardButton(text="🏆 Индивидуальные достижения", callback_data="asp_individual"),   
    InlineKeyboardButton(text="💰 Стипендии для аспирантов", callback_data="asp_stipend"),
    InlineKeyboardButton(text="🔙 Назад", callback_data="admission"),
    width=1)

    return builder.as_markup()

def ordinatura_keyboard():
    builder = InlineKeyboardBuilder()

    builder.row(
    InlineKeyboardButton(text="📅 Сроки приёма в ординатуру", callback_data="ord_priem"),
    InlineKeyboardButton(text="🏆 Индивидуальные достижения", callback_data="ord_individual"),
    InlineKeyboardButton(text="💰 Стипендия для ординаторов", callback_data="ord_stipend"),   
    InlineKeyboardButton(text="🔙 Назад", callback_data="admission"),
    width=1)

    return builder.as_markup()