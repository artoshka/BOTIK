
from aiogram import types

from config import bot, ADMIN

from  database.bot_dp import sql_commands_get_all_id




async def mailing(message: types.Message):
    if message.from_user.id in ADMIN:
        result = await sql_commands_get_all_id()
        for id in result:
            await bot.send_message(id[0], message.text[3:])
    else:
        await message.answer("Ты кто?")