from aiogram.types import Message , CallbackQuery
from aiogram.filters import CommandStart 
from aiogram import Router, F
from lexicon.lexicon_ru import LEXICON_RU
import logging
from logging_setting.logging import setup_logging
from keyboards.main_keyboard import main_menu_keyboard
from keyboards.admission_keyboards import (main_admission_keyboard, dorm_keyboard , back_to_dorm_keyboard, bacavriat_keyboard, magistratura_keyboard, ordinatura_keyboard,aspirantura_keyboard,
                                           back_to_bacalavr , bac_priem_keyboard , back_to_mag , bac_stipend_keyboard, mag_sroki_priem_keyboard)

from aiogram.types import FSInputFile





router = Router()

@router.message(CommandStart())
async def process_start_command(message:Message):
    await message.answer(text=LEXICON_RU['/start'],reply_markup=main_menu_keyboard())

@router.callback_query(F.data == 'main_menu')
async def process_back_to_start_command(callback:CallbackQuery):
    await callback.message.edit_text(text=LEXICON_RU['/start'],reply_markup=main_menu_keyboard())

@router.callback_query(F.data == 'admission')
async def process_admission_btn(callback: CallbackQuery):
    await callback.message.edit_text(
        text='Это раздел поступления, что вас интересует?',
        reply_markup= main_admission_keyboard()
    )


@router.callback_query(F.data == 'dorm')
async def process_dorm_btn(callback: CallbackQuery):
    await callback.message.edit_text(
        text='нажмите на общежитиу чтобы посмотреть ифнормацию о общежитии или посмотрите универсальный список документов для заселения',
        reply_markup= dorm_keyboard()
    )

@router.callback_query(F.data == 'dorm_docs')
async def process_dorm_docs(callback: CallbackQuery):
    await callback.message.edit_text(
        text='''Пакет документов для заселения:
- Фото (цветное, 3*4, 2 шт.)
- Паспорт
- Временное удостоверение из международного департамента (для иностранных граждан)
- Заключение Клинико-диагностического центра РУДН о возможности проживания в общежитии (памятки)
- Студенческий билет или временное удостоверение с номером студенческого билета
- При обучении по контракту — заявление на заселение из Коммерческого управления''',
        reply_markup= back_to_dorm_keyboard()
    )

@router.callback_query(F.data == 'dorm_steps_get')
async def process_dorm_steps_get(callback: CallbackQuery):
    await callback.message.edit_text(
        text='''Пошаговые действия для получения общежития:
        Обратиться в Управление по размещению и сопровождению в общежитиях с пакетом документов (ул. Миклухо-Маклая, д.6, МФЦ РУДН);
- Получить направление для постоянного проживания в общежитии;
- Обратиться к специалисту по размещению и учету общежития для подбора комнаты для проживания;
- Заключить договор на проживание и получить счет на оплату;   
- Оплатить проживание (необходимо своевременно оплачивать проживание в общежитии, оплата производится до каждого 10 числа расчетного месяца);
- Обратиться к заведующему общежитием (дежурному коменданту) для заселения и ознакомления с Правилами проживания и внутреннего распорядка в общежитиях РУДН;
- В 3-дневный срок после заключения договора обратиться в монофункциональный центр РУДН для подачи документов с целью постановки на миграционный/регистрационный учет по Москве..
(Распределение по общежитиям происходит на основании приказов Ректора преимущественно по факультетскому и курсовому принципу и в соответствии с пожеланиями студента. С целью улучшения языковой подготовки студентов расселение осуществляется, как правило, с соблюдением интернационального принципа. При наличии мест, студенту предоставляется право выбора комнаты)''',
        reply_markup= back_to_dorm_keyboard()
    )

@router.callback_query(F.data == 'dorm_pay')
async def process_dorm_pay(callback: CallbackQuery):
    await callback.message.edit_text(
        text='''Размер платы за пользование жилыми помещениями в общежитиях РУДН устанавливается Ректоратом университета и объявляется приказом Ректора.

В стоимость за место в общежитии включено:

стоимость аренды и коммунальных услуг — в пятиэтажных корпусах;
стоимость аренды, коммунальных и дополнительных услуг* — в высотных корпусах.
*Согласно приказу ректора № 272/р от 29.04.15 в комплекс дополнительных услуг входят:

дополнительный объем мебели;
телевизор, холодильник;
повышенный уровень комфортности;
возможность подключения дополнительных электробытовых приборов по согласованию с Университетом.
Размер оплаты за место — от 1 800 до 13 400 рублей в месяц в зависимости от типа общежития и уровня комфортности комнаты.

Способы оплаты за проживание в общежитии:

Воспользоваться Порталом единой информационной системы РУДН (для входа используйте свои учетные записи корпоративной почты Office365) для выписки счета за проживание;
Получить счет на оплату у специалиста по размещению и учету в своем общежитии;
Оплатить счет в любом банке или через мобильное приложение банка (в т.ч. по QR-коду).
Оферта

    Оферта (договор) найма жилого помещения в «гостевом фонде» общежитий РУДН.
    Публичная оферта (договор) на оказание комплекса дополнительных услуг в студенческом общежитий.
    Оферта (договор) найма жилого помещения в общежитии РУДН.''',
                    reply_markup= back_to_dorm_keyboard()
    )



@router.callback_query(F.data.in_([f"dorm_{i}" for i in range(1, 16)]))
async def process_dorm_btn(callback: CallbackQuery):
    await callback.message.edit_text(
        text='при получении необходимых данных тут будет фото и описание соответсвующего общежития',
        reply_markup= back_to_dorm_keyboard()
    )

@router.callback_query(F.data == 'bacalavr')
async def process_bacalavr_btn(callback: CallbackQuery):
    await callback.message.delete()                       
    await callback.message.answer(                    
        text='Это раздел поступления в бакалавриат/специалитет, что вас интересует?',
        reply_markup=bacavriat_keyboard()
    )
    logging.info('handler bacalavr work')



@router.callback_query(F.data == 'save_bac_priem')
async def send_save_back_priem(callback: CallbackQuery):
    await callback.message.delete()                       

    doc = FSInputFile('C:\\Users\\timur\\OneDrive\\Рабочий стол\\project\\aiogram\\tg_bot_study\\code\\RUDN_bot\\photo\\bac_priem.png')
    await callback.message.answer_document(
        document=doc,
        caption='📎 Сохрани себе этот файл с датами приёма',
        reply_markup=back_to_bacalavr()
    )
    await callback.answer()  

    logging.info('photo sended and handler bac_priem work')

@router.callback_query(F.data == 'bac_priem')
async def process_bac_priem_btn(callback: CallbackQuery):
    await callback.message.delete()                     
    photo = FSInputFile('C:\\Users\\timur\\OneDrive\\Рабочий стол\\project\\aiogram\\tg_bot_study\\code\\RUDN_bot\\photo\\bac_priem.png')
    await callback.message.answer_photo(
        photo=photo,
        caption='Сроки приёма в бакалавриат/специалитет',
        reply_markup=bac_priem_keyboard()
    )
    await callback.answer()

    #  InlineKeyboardButton(text="📁 Калькулятор баллов ЕГЭ", callback_data="calculator"),
    # InlineKeyboardButton(text="💰 Сроки приёма в бакалавриат и специалитет в 2025 году", callback_data="bac_priem"),   
    # InlineKeyboardButton(text="📁 Проходные баллы прошлых лет", callback_data="bac_score_past"),
    # InlineKeyboardButton(text="📁 Индивидуальные достижения", callback_data="bac_individual"),
    # InlineKeyboardButton(text="📁 Стипендиальная программа «Лига стипендий»", callback_data="bac_stipend"),


@router.callback_query(F.data == 'calculator')
async def process_calculator_btn(callback: CallbackQuery):
    await callback.message.edit_text(
        text='Это раздел калькулятора баллов ЕГЭ (тут будет калькулятор)',
        reply_markup= back_to_bacalavr()
    )
    await callback.answer()

@router.callback_query(F.data == 'bac_score_past')
async def process_bac_score_past_btn(callback: CallbackQuery):
    await callback.message.edit_text(
    text='''Аграрно-технологический институт

35.03.04
Агрономия
235
Инженерная академия

07.03.00
Архитектура
310
Факультет физико-математических и естественных наук

38.03.05
Бизнес-информатика
264
Аграрно-технологический институт

36.05.01
Ветеринария
281
Аграрно-технологический институт

36.03.01
Ветеринарно-санитарная экспертиза
210
Высшая школа управления

43.03.03
Гостиничное дело
276
Факультет гуманитарных и социальных наук

38.03.04
Государственное и муниципальное управление
300
Филологический факультет

42.03.02
Журналистика
361
Экономический факультет

41.03.01
Зарубежное регионоведение
286
Институт иностранных языков

41.03.01
Зарубежное регионоведение
287
Аграрно-технологический институт

21.03.02
Землеустройство и кадастры
223
Инженерная академия

27.03.05
Инноватика
261
Факультет гуманитарных и социальных наук

50.03.01
Искусства и гуманитарные науки
300
Факультет гуманитарных и социальных наук

46.03.01
История
274
Факультет физико-математических и естественных наук

02.03.00
Компьютерные и информационные науки
252
Инженерная академия

15.03.05
Конструкторско-технологическое обеспечение машиностроительных производств
209
Аграрно-технологический институт

35.03.10
Ландшафтная архитектура
254
Медицинский институт

31.05.01
Лечебное дело
277
Филологический факультет

45.03.02
Лингвистика
300
Институт иностранных языков

45.03.02
Лингвистика
300
Факультет физико-математических и естественных наук

01.03.00
Математика и механика
240
Факультет гуманитарных и социальных наук

41.03.05
Международные отношения
299
Институт мировой экономики и бизнеса

38.03.01
Мировая экономика и международная экономическая безопасность
267
Инженерная академия

28.03.02
Наноинженерия
222
Инженерная академия

21.03.01
Нефтегазовое дело
271
Факультет гуманитарных и социальных наук

41.03.00
Политические науки и регионоведение
300
Инженерная академия

21.05.00
Прикладная геология, горное дело, нефтегазовое дело и геодезия
211
Факультет физико-математических и естественных наук

09.03.03
Прикладная информатика
269
Инженерная академия

01.03.02
Прикладная математика и информатика
239
Институт русского языка

45.03.01
Прикладная цифровая филология
300
Филологический факультет

37.03.01
Психология
267
Институт иностранных языков

44.03.02
Психолого-педагогическое образование
249
Филологический факультет

42.03.01
Реклама и связи с общественностью
297
Институт мировой экономики и бизнеса

42.03.01
Реклама и связи с общественностью
300
Медицинский институт

34.03.01
Сестринское дело
192
Факультет гуманитарных и социальных наук

39.03.01
Социология
274
Аграрно-технологический институт

27.03.01
Стандартизация и метрология
211
Медицинский институт

31.05.03
Стоматология
300
Инженерная академия

08.03.01
Строительство
229
Институт внешнеэкономической безопасности и таможенного дела

38.05.02
Таможенное дело
265
Филологический факультет

42.03.04
Телевидение
352
Инженерная академия

27.03.04
Управление в технических системах
256
Институт экологии

05.03.06
Управление природными ресурсами
222
Медицинский институт

33.05.01
Фармация
240
Факультет физико-математических и естественных наук

03.03.02
Физика
231
Филологический факультет

45.03.01
Филология
300
Факультет гуманитарных и социальных наук

47.03.01
Философия
261
Факультет физико-математических и естественных наук

04.03.01
Химия
267
Институт экологии

05.03.06
Экология и природопользование
220
Экономический факультет

38.03.00
Экономика и управление
300
Инженерная академия

23.03.03
Эксплуатация транспортно-технологических машин и комплексов
201
Инженерная академия

13.03.03
Энергетическое машиностроение
199
Институт экологии

18.03.02
Энерго- и ресурсосберегающие процессы в химической технологии, нефтехимии и биотехнологии
237
Юридический институт

40.03.01
Юриспруденция
300
        ''',
        reply_markup= back_to_bacalavr()
    )
    await callback.answer()

@router.callback_query(F.data == 'bac_individual')
async def process_bac_individual_btn(callback: CallbackQuery):
    await callback.message.edit_text(
        text='''(Сумма баллов, начисленных поступающему за индивидуальные достижения, не может быть более 10 баллов. Баллы, начисленныеза индивидуальные достижения, включаются в сумму конкурсных баллов

Поступающим по решению Университета начисляются баллы за следующие индивидуальные достижения, полученные в 10 или 11 классах)

Наличие аттестата РФ о среднем общем образовании с отличием

10 баллов
Наличие аттестата РФ о среднем (полном) общем образовании с отличием

10 баллов
Наличие аттестата РФ о среднем (полном) общем образовании для награжденных золотой (серебряной) медалью

10 баллов
Наличие диплома РФ о среднем профессиональном образовании с отличием

10 баллов
Наличие диплома РФ о начальном профессиональном образовании с отличием

10 баллов
Наличие диплома РФ о начальном профессиональном образовании для награжденных золотой (серебряной) медалью)

10 баллов
Наличие диплома победителя Олимпиады РУДН для школьников

8 баллов

Наличие диплома победителя международной олимпиады «RUDN JUNIOR MATH OLYMP»


''',

         reply_markup= back_to_bacalavr()
    )           
    await callback.answer()

@router.callback_query(F.data == 'bac_stipend')
async def process_bac_stipend_btn(callback: CallbackQuery):
    await callback.message.delete()                     
    photo = FSInputFile('C:\\Users\\timur\\OneDrive\\Рабочий стол\\project\\aiogram\\tg_bot_study\\code\\RUDN_bot\\photo\\bac_stipend.png')
    await callback.message.answer_photo(
        photo=photo,
        caption='стипендии для бакалавриат/специалитет',
        reply_markup=bac_stipend_keyboard()
    )
    await callback.answer()


@router.callback_query(F.data == 'save_bac_stipend')
async def send_save_bac_stipend_photo(callback: CallbackQuery):
    await callback.message.delete()                       

    doc = FSInputFile('C:\\Users\\timur\\OneDrive\\Рабочий стол\\project\\aiogram\\tg_bot_study\\code\\RUDN_bot\\photo\\bac_stipend.png')
    await callback.message.answer_document(
        document=doc,
        caption='📎 Сохрани себе этот файл с стипендиями для бакалвриата/специалитета',
        reply_markup=back_to_bacalavr()
    )
    await callback.answer()  




        
@router.callback_query(F.data == 'magistr')
async def process_magistratura_btn(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(
        text='Это раздел поступления в магистратуру что вас интересует?',
        reply_markup= magistratura_keyboard()
    )


    # InlineKeyboardButton(text="📁 Как поступить в магистратуру РУДН?", callback_data="mag_priem"),
    # InlineKeyboardButton(text="💰 Сроки приёма в магистратуру", callback_data="mag_sroki"),   
    # InlineKeyboardButton(text="📁 Индивидуальные достижения", callback_data="mag_individ"),
    # InlineKeyboardButton(text="📁 Стипендии для талантливых магистров", callback_data="mag_stipend"),
    # InlineKeyboardButton(text="🔙 Назад", callback_data="admission"),

# @router.callback_query(F.data == 'mag_priem')
# async def process_mag_priem_btn(callback: CallbackQuery):
#     await callback.message.edit_text()


@router.callback_query(F.data == 'mag_sroki')
async def process_mag_priem_sroki_btn(callback: CallbackQuery):
    await callback.message.delete()                     
    photo = FSInputFile('C:\\Users\\timur\\OneDrive\\Рабочий стол\\project\\aiogram\\tg_bot_study\\code\\RUDN_bot\\photo\\mag_sroki.png')
    await callback.message.answer_photo(
        photo=photo,
        caption='сроки поступления в магистратуру',
        reply_markup=mag_sroki_priem_keyboard()
    )
    await callback.answer()


@router.callback_query(F.data == 'save_mag_sroki_priem')
async def send_save_mag_sroki_priem(callback: CallbackQuery):
    await callback.message.delete()                       

    doc = FSInputFile('C:\\Users\\timur\\OneDrive\\Рабочий стол\\project\\aiogram\\tg_bot_study\\code\\RUDN_bot\\photo\\mag_sroki.png')
    await callback.message.answer_document(
        document=doc,
        caption='📎 Сохрани себе этот файл с сроками поступления в магистратуру',
        reply_markup=back_to_mag()
    )
    await callback.answer()  




@router.callback_query(F.data == 'aspirant')
async def process_aspirantura_btn(callback: CallbackQuery):
    await callback.message.edit_text(
        text='Это раздел поступления в аспирантуру что вас интересует?',
        reply_markup= aspirantura_keyboard()
    )

@router.callback_query(F.data == 'ordinat')
async def process_ordinatura_btn(callback: CallbackQuery):
    await callback.message.edit_text(
        text='Это раздел поступления в ординатуру что вас интересует?',
        reply_markup= ordinatura_keyboard()
    )





    
