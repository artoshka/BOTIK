from aiogram import types, Dispatcher
from aiogram.types import ParseMode, InlineKeyboardButton, InlineKeyboardMarkup

from config import bot







#@dp.message_handler(commands=['mem'])
async def command_mem(message: types.Message):
    photo = open('media/i.jpg.webp', 'rb')
    await bot.send_photo(message.from_user.id, photo=photo)


#@dp.message_handler(commands=['quiz'])
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


async def pin(messege: types.Message):
    if not messege.reply_to_message:
        await messege.answer("комманда должна работать на ответном сообщении")
    else:
        await bot.pin_chat_message(messege.chat.id, messege.message_id)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(quiz_1, commands=["quiz"], commands_prefix="!")
    dp.register_message_handler(command_mem, commands=["mem"], commands_prefix="!")
    dp.register_message_handler(pin, commands=["pin"], commands_prefix="!")