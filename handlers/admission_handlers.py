from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram import Router, F
from lexicon.lexicon_ru import LEXICON_RU, LEXICON_COMMANDS, LEXICON_RU_ADMISSION
import logging
from logging_setting.logging import setup_logging
from keyboards.main_keyboard import main_menu_keyboard
from keyboards.admission_keyboards import (
    main_admission_keyboard, dorm_keyboard, back_to_dorm_keyboard, 
    bacavriat_keyboard, magistratura_keyboard, ordinatura_keyboard, aspirantura_keyboard,
    back_to_bacalavr, bac_priem_keyboard, back_to_mag, back_to_ord, 
    bac_stipend_keyboard, mag_sroki_priem_keyboard, mag_admission_keyboard, back_to_asp
)
from aiogram.types import FSInputFile

router = Router()

setup_logging()


@router.callback_query(F.data == 'main_menu')
async def process_back_to_start_command(callback: CallbackQuery):
    await callback.message.edit_text(text=LEXICON_RU['/start'], reply_markup=main_menu_keyboard())
    await callback.answer()

@router.callback_query(F.data == 'admission')
async def process_admission_btn(callback: CallbackQuery):
    await callback.message.edit_text(
        text=LEXICON_RU_ADMISSION['admission'],
        reply_markup=main_admission_keyboard()
    )
    await callback.answer()

@router.callback_query(F.data == 'dorm')
async def process_dorm_btn(callback: CallbackQuery):
    await callback.message.edit_text(
        text=LEXICON_RU_ADMISSION['dorm'],
        reply_markup=dorm_keyboard()
    )
    await callback.answer()


@router.callback_query(F.data == 'dorm_docs')
async def process_dorm_docs(callback: CallbackQuery):
    await callback.message.edit_text(
        text=LEXICON_RU_ADMISSION['dorm_docs'],
        reply_markup=back_to_dorm_keyboard()
    )
    await callback.answer()



@router.callback_query(F.data == 'dorm_steps_get')
async def process_dorm_steps_get(callback: CallbackQuery):
    await callback.message.edit_text(
        text=LEXICON_RU_ADMISSION['dorm_steps_get'],
        reply_markup=back_to_dorm_keyboard()
    )
    await callback.answer()


@router.callback_query(F.data == 'dorm_pay')
async def process_dorm_pay(callback: CallbackQuery):
    await callback.message.edit_text(
        text=LEXICON_RU_ADMISSION['dorm_pay'],
        reply_markup=back_to_dorm_keyboard()
    )
    await callback.answer()


@router.callback_query(F.data.in_([f"dorm_{i}" for i in range(1, 16)]))
async def process_dorm_info(callback: CallbackQuery):
    await callback.message.edit_text(
        text=LEXICON_RU_ADMISSION['dorm_info'],
        reply_markup=back_to_dorm_keyboard()
    )
    await callback.answer()


@router.callback_query(F.data == 'bacalavr')
async def process_bacalavr_btn(callback: CallbackQuery):
    await callback.message.delete()                       
    await callback.message.answer(                    
        text=LEXICON_RU_ADMISSION['bacalavr'],
        reply_markup=bacavriat_keyboard()
    )
    await callback.answer()
    logging.info('handler bacalavr work')

@router.callback_query(F.data == 'save_bac_priem')
async def send_save_back_priem(callback: CallbackQuery):
    await callback.message.delete()                       
    doc = FSInputFile('C:\\Users\\timur\\OneDrive\\Рабочий стол\\project\\aiogram\\tg_bot_study\\code\\RUDN_bot\\photo/bac_priem.png')
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
    photo = FSInputFile('C:\\Users\\timur\\OneDrive\\Рабочий стол\\project\\aiogram\\tg_bot_study\\code\\RUDN_bot\\photo/bac_priem.png')
    await callback.message.answer_photo(
        photo=photo,
        caption=LEXICON_RU_ADMISSION['bac_priem_caption'],
        reply_markup=bac_priem_keyboard()
    )
    await callback.answer()

@router.callback_query(F.data == 'calculator')
async def process_calculator_btn(callback: CallbackQuery):
    await callback.message.edit_text(
        text=LEXICON_RU_ADMISSION['calculator'],
        reply_markup=back_to_bacalavr()
    )
    await callback.answer()

@router.callback_query(F.data == 'bac_score_past')
async def process_bac_score_past_btn(callback: CallbackQuery):
    await callback.message.edit_text(
        text=LEXICON_RU_ADMISSION['bac_score_past'],
        reply_markup=back_to_bacalavr()
    )
    await callback.answer()

@router.callback_query(F.data == 'bac_individual')
async def process_bac_individual_btn(callback: CallbackQuery):
    await callback.message.edit_text(
        text=LEXICON_RU_ADMISSION['bac_individual'],
        reply_markup=back_to_bacalavr()
    )           
    await callback.answer()

@router.callback_query(F.data == 'bac_stipend')
async def process_bac_stipend_btn(callback: CallbackQuery):
    await callback.message.delete()                     
    photo = FSInputFile('C:\\Users\\timur\\OneDrive\\Рабочий стол\\project\\aiogram\\tg_bot_study\\code\\RUDN_bot\\photo/bac_stipend.png')
    await callback.message.answer_photo(
        photo=photo,
        caption=LEXICON_RU_ADMISSION['bac_stipend_caption'],
        reply_markup=bac_stipend_keyboard()
    )
    await callback.answer()

@router.callback_query(F.data == 'save_bac_stipend')
async def send_save_bac_stipend_photo(callback: CallbackQuery):
    await callback.message.delete()                       
    doc = FSInputFile('C:\\Users\\timur\\OneDrive\\Рабочий стол\\project\\aiogram\\tg_bot_study\\code\\RUDN_bot\\photo/bac_stipend.png')
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
        text=LEXICON_RU_ADMISSION['magistr'],
        reply_markup=magistratura_keyboard()
    )
    await callback.answer()

@router.callback_query(F.data == 'mag_priem')
async def process_mag_priem_btn(callback: CallbackQuery):
    await callback.message.edit_text(
        text=LEXICON_RU_ADMISSION['mag_priem'],
        reply_markup=mag_admission_keyboard()
    )
    await callback.answer()

@router.callback_query(F.data == 'mag_budget')
async def process_mag_budget_btn(callback: CallbackQuery): 
    await callback.message.edit_text(
        text=LEXICON_RU_ADMISSION['mag_budget'],
        reply_markup=back_to_mag()
    )
    await callback.answer()     

@router.callback_query(F.data == 'mag_grant')
async def process_mag_grant_btn(callback: CallbackQuery):
    await callback.message.edit_text(
        text=LEXICON_RU_ADMISSION['mag_grant'],
        reply_markup=back_to_mag()
    )
    await callback.answer() 

@router.callback_query(F.data == 'mag_purpose_study')
async def process_mag_purpose_study_btn(callback: CallbackQuery):  
    await callback.message.edit_text(
        text=LEXICON_RU_ADMISSION['mag_purpose_study'],
        reply_markup=back_to_mag()
    )
    await callback.answer() 

@router.callback_query(F.data == 'mag_pay_study')
async def process_mag_pay_study_btn(callback: CallbackQuery):
    await callback.message.edit_text(
        text=LEXICON_RU_ADMISSION['mag_pay_study'],
        reply_markup=back_to_mag()
    )       
    await callback.answer()

@router.callback_query(F.data == 'mag_sroki')
async def process_mag_priem_sroki_btn(callback: CallbackQuery):
    await callback.message.delete()                     
    photo = FSInputFile('C:\\Users\\timur\\OneDrive\\Рабочий стол\\project\\aiogram\\tg_bot_study\\code\\RUDN_bot\\photo/mag_sroki.png')
    await callback.message.answer_photo(
        photo=photo,
        caption=LEXICON_RU_ADMISSION['mag_sroki_caption'],
        reply_markup=mag_sroki_priem_keyboard()
    )
    await callback.answer()

@router.callback_query(F.data == 'save_mag_sroki_priem')
async def send_save_mag_sroki_priem(callback: CallbackQuery):
    await callback.message.delete()                       
    doc = FSInputFile('C:\\Users\\timur\\OneDrive\\Рабочий стол\\project\\aiogram\\tg_bot_study\\code\\RUDN_bot\\photo/mag_sroki.png')
    await callback.message.answer_document(
        document=doc,
        caption='📎 Сохрани себе этот файл с сроками поступления в магистратуру',
        reply_markup=back_to_mag()
    )
    await callback.answer()  

@router.callback_query(F.data == 'mag_individ')
async def process_mag_individ_btn(callback: CallbackQuery):
    await callback.message.edit_text(
        text=LEXICON_RU_ADMISSION['mag_individ'],
        reply_markup=back_to_mag()
    )       
    await callback.answer()

@router.callback_query(F.data == 'mag_stipend')
async def process_mag_stipend_btn(callback: CallbackQuery):
    await callback.message.edit_text(
        text=LEXICON_RU_ADMISSION['mag_stipend'],
        reply_markup=back_to_mag()
    )
    await callback.answer()

@router.callback_query(F.data == 'aspirant')
async def process_aspirantura_btn(callback: CallbackQuery):
    await callback.message.edit_text(
        text=LEXICON_RU_ADMISSION['aspirant'],
        reply_markup=aspirantura_keyboard()
    )
    await callback.answer()

@router.callback_query(F.data == 'asp_sroki')
async def process_asp_sroki_btn(callback: CallbackQuery):
    await callback.message.edit_text(
        text=LEXICON_RU_ADMISSION['asp_sroki'],
        reply_markup=back_to_asp()
    )
    await callback.answer()

@router.callback_query(F.data == 'asp_individual')
async def process_asp_individual_btn(callback: CallbackQuery):
    await callback.message.edit_text(
        text=LEXICON_RU_ADMISSION['asp_individual'],
        reply_markup=back_to_asp()
    )       
    await callback.answer() 

@router.callback_query(F.data == 'asp_stipend')
async def process_asp_stipend_btn(callback: CallbackQuery):
    await callback.message.edit_text(
        text=LEXICON_RU_ADMISSION['asp_stipend'],
        reply_markup=back_to_asp()
    )       
    await callback.answer() 

@router.callback_query(F.data == 'ordinat')
async def process_ordinatura_btn(callback: CallbackQuery):
    await callback.message.edit_text(
        text=LEXICON_RU_ADMISSION['ordinat'],
        reply_markup=ordinatura_keyboard()
    )
    await callback.answer()

@router.callback_query(F.data == 'ord_priem')
async def process_ord_priem_btn(callback: CallbackQuery):
    await callback.message.edit_text(
        text=LEXICON_RU_ADMISSION['ord_priem'],
        reply_markup=back_to_ord()
    )
    await callback.answer() 
    
@router.callback_query(F.data == 'ord_individual')
async def process_ord_individual_btn(callback: CallbackQuery):
    await callback.message.edit_text(
        text=LEXICON_RU_ADMISSION['ord_individual'],
        reply_markup=back_to_ord()
    )       
    await callback.answer() 

@router.callback_query(F.data == 'ord_stipend')
async def process_ord_stipend_btn(callback: CallbackQuery): 
    await callback.message.edit_text(
        text=LEXICON_RU_ADMISSION['ord_stipend'],
        reply_markup=back_to_ord()
    )       
    await callback.answer()