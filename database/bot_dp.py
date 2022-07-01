import sqlite3
from config import bot

import random


def sql_create():
    global dp, cursor
    dp = sqlite3.connect("bot.sqlite3")
    cursor = dp.cursor()


    if dp:
        print("База данных подключена")


    dp.execute("CREATE TABLE IF NOT EXISTS menu"
               "( photo TEXT, food TEXT PRIMARY KEY,"
               "description TEXT, price INTEGER)"
               )
    dp.commit()


async def sql_command_random(message):
    result = cursor.execute("SELECT * FROM menu").fetchall()
    random_food = random.choice(result)
    await bot.send_photo(
        message.from_user.id,
        photo=random_food[0],
        caption=f"Блюдо: {random_food[1]}\n"
                f"Описание: {random_food[2]}\n"
                f"Цена: {random_food[3]}"
    )


async def sql_command_all():
    return cursor.execute("SELECT * FROM anketa").fetchall()


async def sql_command_delete(id):
    cursor.execute("DELETE FROM menu WHERE food == ?", (id, ))
    dp.commit()


async def sql_commands_get_all_id():
    return cursor.execute("SELECT food FROM menu").fetchall()