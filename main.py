import asyncio

from aiogram.utils import executor

from config import dp
from handlers import extra, callback, client, fsmAdminMenu, notification, inline
import logging
from database.bot_dp import sql_create

async def on_startup(_):
    asyncio.create_task(notification.scheduler())
    sql_create()





client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
fsmAdminMenu.register_hendler_fsm_food(dp)
notification.register_handler_notification(dp)
inline.register_inline_handler(dp)

extra.register_hendlers_extra(dp)



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)