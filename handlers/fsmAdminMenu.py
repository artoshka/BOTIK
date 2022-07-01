from aiogram import types, Dispatcher

from aiogram.dispatcher import FSMContext

from aiogram.dispatcher.filters.state import State, StatesGroup

from config import bot, ADMIN
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from database import bot_dp



class FSMAdmin(StatesGroup):
    photo = State()
    food = State()
    description = State()
    price = State()


async def fsm_start(messege: types.Message):
    if messege.from_user.id not in ADMIN:
        await messege.answer("Ты кто? Ты не мой администратор")
    else:
        await FSMAdmin.photo.set()
        await messege.answer(f"Даров {messege.from_user.full_name}, скинь фотку вкусненького блюда")


async def load_photo(messege: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = messege.photo[0].file_id
    await FSMAdmin.next()
    await messege.answer("Вкусно выглядит как называется?")


async def load_food(messege: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['food'] = messege.text
    await FSMAdmin.next()
    await messege.answer("Что это еще за блюдо такое? Расскажи немного про это блюдо")


async def load_description(messege: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = messege.text
    await FSMAdmin.next()
    await messege.answer("Вот оно что а сколько стоит?")


async def load_price(messege: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data['price'] = int(messege.text)
    except:
        await messege.answer("какие букавы? я цену спрашивал а не букавы")

    await bot.send_photo(messege.from_user.id, data['photo'], caption=f"Блюдо: {data['food']}\n"
                                                                      f"Описание: {data['description']}\n"
                                                                      f"Цена: {data['price']}")

    await state.finish()
    await messege.answer("на этом все")

async def delete_data(messege: types.Message):
    if messege.from_user.id in ADMIN and messege.chat.type == "private":
        result = await  bot_dp.sql_command_all()
        for food in result:
            await bot.send_photo(
                messege.from_user.id,
                photo=food[0],
                caption=f"Блюдо: {food[1]}\n"
                        f"Описание: {food[2]}\n"
                        f"Цена: {food[3]}",
                reply_markup=InlineKeyboardMarkup().add(
                    InlineKeyboardButton(
                        f"delete {food[1]}",
                        callback_data=f"delete {food[1]}"
                    )
                )
            )

    else:
        await messege.answer("ты кто?")


async def complete_delete(call: types.CallbackQuery):
    await bot_dp.sql_command_delete(call.data.replace("delete ", ""))
    await call.answer(text="Блюдо удалено!", show_alert=True)
    await bot.delete_message(call.message.chat.id, call.message.message_id)


def register_hendler_fsm_food(dp: Dispatcher):
    dp.register_message_handler(fsm_start, commands=['food'], commands_prefix="/")
    dp.register_message_handler(load_photo, state=FSMAdmin.photo, content_types=['photo'])
    dp.register_message_handler(load_food, state=FSMAdmin.food)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_price, state=FSMAdmin.price)
    dp.register_message_handler(delete_data, commands=['delete'], commands_prefix="/")
    dp.register_callback_query_handler(complete_delete,
                                       lambda call: call.data and
                                                    call.data.startswith('delete '))
