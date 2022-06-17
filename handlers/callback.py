from aiogram import types, Dispatcher
from aiogram.types import ParseMode, InlineKeyboardButton, InlineKeyboardMarkup

from config import bot





#@dp.callback_query_handler(lambda call: call.data == "button_call_1")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton(
        "NEXT",
        callback_data='button_call_2',
    )
    markup.add(button_call_2)

    question = 'Кто директор компании Tesla motorsport?'
    answers = [
        "Илон Маск",
        "Жак Фреско",
        "Тони Старк",
        "Брюс Уэйн"
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="Сту пудов Тони Старк, а не не он",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )

async def quiz_3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_3 = InlineKeyboardButton(
        "NEXT",
        callback_data='button_call_3',
    )
    markup.add(button_call_3)

    question = 'Кто главный злодей в Star Wars?'
    answers = [
        "Дарт Вэйдер",
        "Дарт мул",
        "Палпатин",
        "Рэй"
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="ДА да Вэйдер главный злодей канеш канеш",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )

async def quiz_4(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_4 = InlineKeyboardButton(
        "NEXT",
        callback_data='button_call_4',
    )
    markup.add(button_call_4)

    question = 'Что ждет форсаж?'
    answers = [
        "БЕСКОНЕЧНОСТЬ НЕ ПРЕДЕЛ",
        "street racing",
        "БЕСКОНЕЧНОСТЬ НЕ ПРЕДЕЛ",
        "БЕСКОНЕЧНОСТЬ НЕ ПРЕДЕЛ"
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="БЕСКОНЕЧНОСТЬ НЕ ПРЕДЕЛ",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )

async def quiz_5(call: types.CallbackQuery):


    question = 'ХО АР Ю?'
    answers = [
        "АЙ ЭМ Ю",
        "АЙ ДОНТ НОУ",
        "Человек",
        "АЙМБЭТМЕН"
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="АЙМПЕТЕРМЭН",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,

    )


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, lambda call: call.data == "button_call_1")
    dp.register_callback_query_handler(quiz_3, lambda call: call.data == "button_call_2")
    dp.register_callback_query_handler(quiz_4, lambda call: call.data == "button_call_3")
    dp.register_callback_query_handler(quiz_5, lambda call: call.data == "button_call_4")
