from aiogram.filters.callback_data import CallbackData
from typing import Optional
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton


class User_setting_CallbackFactory(CallbackData, prefix='user'):
    section: Optional[str] = None
    institut: Optional[str] = None
    faculty: Optional[str] = None
    group: Optional[str] = None


def setting_section_keyboard():
    builder = InlineKeyboardBuilder()

    builder.add(
        InlineKeyboardButton(text="Бокс", callback_data=User_setting_CallbackFactory(section="boxing").pack()),
        InlineKeyboardButton(text="Футбол", callback_data=User_setting_CallbackFactory(section="football").pack()),
        InlineKeyboardButton(text="Баскетбол", callback_data=User_setting_CallbackFactory(section="basketball").pack()),
        InlineKeyboardButton(text="Волейбол", callback_data=User_setting_CallbackFactory(section="volleyball").pack()),
        InlineKeyboardButton(text="Танцы", callback_data=User_setting_CallbackFactory(section="dancing").pack()),
        InlineKeyboardButton(text="Бадминтон", callback_data=User_setting_CallbackFactory(section="badminton").pack()),
        InlineKeyboardButton(text="Назад", callback_data="main_menu")
    )

    builder.adjust(2, 2, 2, 1)
    return builder.as_markup()


def setting_institut_keyboard():
    builder = InlineKeyboardBuilder()

    builder.add(
        InlineKeyboardButton(
            text="Институт гуманитарных наук",
            callback_data=User_setting_CallbackFactory(institut="humanitarian").pack()
        ),
        InlineKeyboardButton(
            text="Институт иностранных языков",
            callback_data=User_setting_CallbackFactory(institut="foreign_languages").pack()
        ),
        InlineKeyboardButton(
            text="Институт математики и компьютерных наук",
            callback_data=User_setting_CallbackFactory(institut="math_computer_science").pack()
        ),
        InlineKeyboardButton(
            text="Институт физики и технологий",
            callback_data=User_setting_CallbackFactory(institut="physics_technology").pack()
        ),
        InlineKeyboardButton(text="Назад", callback_data="main_menu")
    )

    builder.adjust(1, 1, 1, 1)
    return builder.as_markup()


def setting_faculty_humanitarian_keyboard():
    builder = InlineKeyboardBuilder()

    builder.add(
        InlineKeyboardButton(
            text="Факультет истории",
            callback_data=User_setting_CallbackFactory(faculty="history").pack()
        ),
        InlineKeyboardButton(
            text="Факультет философии",
            callback_data=User_setting_CallbackFactory(faculty="philosophy").pack()
        ),
        InlineKeyboardButton(
            text="Факультет социологии",
            callback_data=User_setting_CallbackFactory(faculty="sociology").pack()
        ),
        InlineKeyboardButton(
            text="Назад",
            callback_data=User_setting_CallbackFactory(institut="humanitarian").pack()
        )
    )

    builder.adjust(1, 1, 1)
    return builder.as_markup()


def setting_faculty_foreign_languages_keyboard():
    builder = InlineKeyboardBuilder()

    builder.add(
        InlineKeyboardButton(
            text="Факультет английского языка",
            callback_data=User_setting_CallbackFactory(faculty="english").pack()
        ),
        InlineKeyboardButton(
            text="Факультет французского языка",
            callback_data=User_setting_CallbackFactory(faculty="french").pack()
        ),
        InlineKeyboardButton(
            text="Факультет испанского языка",
            callback_data=User_setting_CallbackFactory(faculty="spanish").pack()
        ),
        InlineKeyboardButton(
            text="Назад",
            callback_data=User_setting_CallbackFactory(institut="foreign_languages").pack()
        )
    )

    builder.adjust(1, 1, 1)
    return builder.as_markup()


def setting_faculty_math_computer_science_keyboard():
    builder = InlineKeyboardBuilder()

    builder.add(
        InlineKeyboardButton(
            text="Факультет математики",
            callback_data=User_setting_CallbackFactory(faculty="math").pack()
        ),
        InlineKeyboardButton(
            text="Факультет компьютерных наук",
            callback_data=User_setting_CallbackFactory(faculty="computer_science").pack()
        ),
        InlineKeyboardButton(
            text="Назад",
            callback_data=User_setting_CallbackFactory(institut="math_computer_science").pack()
        )
    )

    builder.adjust(1, 1)
    return builder.as_markup()


def setting_faculty_physics_technology_keyboard():
    builder = InlineKeyboardBuilder()

    builder.add(
        InlineKeyboardButton(
            text="Факультет физики",
            callback_data=User_setting_CallbackFactory(faculty="physics").pack()
        ),
        InlineKeyboardButton(
            text="Факультет технологий",
            callback_data=User_setting_CallbackFactory(faculty="technology").pack()
        ),
        InlineKeyboardButton(
            text="Назад",
            callback_data=User_setting_CallbackFactory(institut="physics_technology").pack()
        )
    )

    builder.adjust(1, 1)
    return builder.as_markup()


def setting_group_keyboard():
    builder = InlineKeyboardBuilder()

    builder.add(
        InlineKeyboardButton(
            text="Группа 1",
            callback_data=User_setting_CallbackFactory(group="group_1").pack()
        ),
        InlineKeyboardButton(
            text="Группа 2",
            callback_data=User_setting_CallbackFactory(group="group_2").pack()
        ),
        InlineKeyboardButton(
            text="Группа 3",
            callback_data=User_setting_CallbackFactory(group="group_3").pack()
        ),
        InlineKeyboardButton(text="Назад", callback_data="main_menu")
    )

    builder.adjust(1, 1, 1)
    return builder.as_markup()


def back_to_my_rudn_keyboard():
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="🔙 Назад", callback_data="my_rudn"))
    return builder.as_markup()