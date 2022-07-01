from aiogram import types, Dispatcher
from aiogram.types import ParseMode, InlineKeyboardButton, InlineKeyboardMarkup
from parser import series, anime, cartoons

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

async def parser_series(message: types.Message):
    data = series.parser()
    for movie in data:
        desc = movie['desc'].split(', ')
        await bot.send_message(
            message.from_user.id,
            f"{movie['title']}\n"
            f"Год: {desc[0]}\n"
            f"Город: {desc[1]}\n"
            f"Жанр: #{desc[2]}\n\n"
            f"{movie['link']}"
         )

async def parser_cartoons(message: types.Message):
    data = cartoons.parser()
    for cartoon in data:
        desc = cartoon['desc'].split(', ')
        await bot.send_message(
            message.from_user.id,
            f"{cartoon['title']}\n"
            f"Год: {desc[0]}\n"
            f"Город: {desc[1]}\n"
            f"Жанр: #{desc[2]}\n\n"
            f"{cartoon['link']}"
         )

async def parser_anime(message: types.Message):
    data = anime.parser()
    for animation in data:
        desc = animation['desc'].split(', ')
        await bot.send_message(
            message.from_user.id,
            f"{animation['title']}\n"
            f"Год: {desc[0]}\n"
            f"Город: {desc[1]}\n"
            f"Жанр: #{desc[2]}\n\n"
            f"{animation['link']}"
         )


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(quiz_1, commands=["quiz"], commands_prefix="/")
    dp.register_message_handler(command_mem, commands=["mem"], commands_prefix="/")
    dp.register_message_handler(pin, commands=["pin"], commands_prefix="/")
    dp.register_message_handler(parser_series, commands='series', commands_prefix='/')
    dp.register_message_handler(parser_cartoons, commands='cartoons', commands_prefix='/')
    dp.register_message_handler(parser_anime, commands='anime', commands_prefix='/')
