

from aiogram import types, Dispatcher
from random import choice
from config import bot, ADMIN




#@dp.message_handler()
async def echo(message: types.Message):
      try:
            a = int(message.text)
            await message.reply(a ** 2)
      except:
            await bot.send_message(message.from_user.id, message.text)



      if message.text.lower() == 'game':
            if message.from_user.id not in ADMIN:
                await message.answer("Ты кто? Ты не мой администратор")

            else:
                 a = ['🎯', '🎲', '⚾', '🎰', '🎳', '🏀']
                 d = await bot.send_dice(message.chat.id, emoji=choice(a))




def register_hendlers_extra(dp: Dispatcher):
      dp.register_message_handler(echo)



