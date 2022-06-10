from aiogram import types
from aiogram.utils import executor
from aiogram.types import ParseMode, InlineKeyboardButton, InlineKeyboardMarkup

from config import bot, dp
import logging


@dp.message_handler(commands=['mem'])
async def command_mem(message: types.Message):
    photo = open('media/i.jpg.webp', 'rb')
    await bot.send_photo(message.from_user.id, photo=photo)


@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton(
        "NEXT",
        callback_data='button_call_1',
    )
    markup.add(button_call_1)

    question = 'какой двигатель стоит на Tesla model s?'
    answers = [
        '2JZT', 'электродвигатель', 'RB34', 'На реактивном!'
    ]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="Аче, хотел подсказку?",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )



@dp.callback_query_handler(lambda call: call.data == "button_call_1")
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


@dp.message_handler()
async def echo(message: types.Message):
    await bot.send_message(message.from_user.id, message.text)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)