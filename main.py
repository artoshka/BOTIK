from aiogram.utils import executor

from config import dp
from  handlers import  extra, callback, client, fsmAdminMenu
import logging

client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
fsmAdminMenu.register_hendler_fsm_food(dp)

extra.register_hendlers_extra(dp)



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)