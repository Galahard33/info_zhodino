from typing import Union

from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery, ParseMode

from .keyboards import items_keyboard, item_keyboard, menu_cd, menu, bus_callback, schedule_bus, day_week, \
    final_schedule
from ..services import get_text_item, get_schedule, get_text_schedule


def register_handlers(dp: Dispatcher):
    # Register your handlers here
    dp.register_message_handler(simple_handler, commands=["test_app"])
    dp.register_message_handler(show_menu, text=["Афиша"])
    dp.register_message_handler(show_schedule_menu, text=["Расписане транспорта"])
    dp.register_message_handler(show_main_menu, commands=["menu"])
    dp.register_callback_query_handler(navigate_bus or navigate, bus_callback.filter() or menu_cd.filter())
    dp.register_callback_query_handler(navigate, menu_cd.filter())


# Create your handlers here

async def simple_handler(message: Message):
    await message.answer('Hello from "TestApp" app!')


async def show_main_menu(message: Message):
    await message.answer('Меню', reply_markup=menu)


async def show_schedule_menu(message: Union[CallbackQuery, Message], **kwargs):
    markup = await schedule_bus()
    if isinstance(message, Message):
        await message.answer("Расписание", reply_markup=markup)
    elif isinstance(message, CallbackQuery):
        call = message
        await call.message.edit_reply_markup(markup)


async def show_schedule_day(callback: CallbackQuery, id, **kwargs):
    markup = await day_week(id)
    text = 'Выберите день'
    await callback.message.edit_text(text=text, reply_markup=markup, parse_mode=ParseMode.HTML)


async def show_menu(message: Message):
    # Выполним функцию, которая отправит пользователю кнопки с доступными категориями
    await list_categories(message)


async def list_categories(message: Union[CallbackQuery, Message], **kwargs):
    # Клавиатуру формируем с помощью следующей функции (где делается запрос в базу данных)
    markup = await items_keyboard()

    # Проверяем, что за тип апдейта. Если Message - отправляем новое сообщение
    if isinstance(message, Message):
        await message.answer("Смотри, что сейчас идет в кино", reply_markup=markup)

    # Если CallbackQuery - изменяем это сообщение
    elif isinstance(message, CallbackQuery):
        call = message
        await call.message.edit_reply_markup(markup)


async def item_text(callback: CallbackQuery, item_id, **kwargs):
    markup = item_keyboard()
    text1 = await get_text_item(item_id)
    text = text1.text
    await callback.message.edit_text(text=str(text), reply_markup=markup, parse_mode=ParseMode.HTML)


async def schedule_text(callback: CallbackQuery, id, b, **kwargs):
    markup = final_schedule(id, b)
    text = await get_text_schedule(id, b)
    await callback.message.edit_text(text=str(text), reply_markup=markup, parse_mode=ParseMode.HTML)


async def navigate(cal: CallbackQuery, callback_data : dict):
    current_level = callback_data.get("level")
    id = int(callback_data.get('item_id'))

    levels = {
        "0": list_categories,
        "1": item_text
    }
    current_level_function = levels[current_level]
    await current_level_function(cal, item_id=id)


async def navigate_bus(cal: CallbackQuery, callback_data : dict):
    current_level = callback_data.get("level")
    id = int(callback_data.get('id'))
    b= int(callback_data.get('b'))

    levels = {
        "0": show_schedule_menu,
        "1": show_schedule_day,
        "2": schedule_text
    }
    current_level_function = levels[current_level]
    await current_level_function(cal, id=id, b=b)