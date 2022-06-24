import asyncio
import aioschedule
from aiogram import types, Dispatcher
from config import bot

async def get_chat_id(messege: types.Message):
    global chat_id
    chat_id = messege.chat.id
    await bot.send_message(chat_id=chat_id, text="got your id!")


async def go_to_lern():
    await bot.send_message(chat_id=chat_id, text="Go to lern!")


async def scheduler():
    aioschedule.every().friday.at("13:15").do(go_to_lern)

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(2)



def register_handler_notification(dp: Dispatcher):
    dp.register_message_handler(get_chat_id,
                                lambda word: 'remind' in word.text)