from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,
                           KeyboardButton, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)

from aiogram.utils.callback_data import CallbackData

from ..services import get_item, get_text_item, get_schedule

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Афиша'),
            KeyboardButton(text='Расписане транспорта')
        ],
        [
            KeyboardButton(text='Расписане транспорwsта')
        ],
    ],
    resize_keyboard=True
)

# Создаем CallbackData-объекты, которые будут нужны для работы с менюшкой
menu_cd = CallbackData("show_menu", "level", "item_id")
bus_callback = CallbackData('schedule', 'level', 'id', 'b')


def make_callback_data(level, item_id="0"):
    return menu_cd.new(level=level, item_id=item_id)


def make_callback_data_bus(level, id="0", b='0'):
    return bus_callback.new(level=level, id=id, b=b)


async def items_keyboard():
    # Указываем, что текущий уровень меню - 0
    CURRENT_LEVEL = 0

    # Создаем Клавиатуру
    markup = InlineKeyboardMarkup(row_width=2)

    # Забираем список товаров из базы данных с РАЗНЫМИ категориями и проходим по нему
    items = await get_item()
    for item in items:
        # Сформируем текст, который будет на кнопке
        button_text = f"{item.name}"

        # Сформируем колбек дату, которая будет на кнопке. Следующий уровень - текущий + 1, и перечисляем категории
        callback_data = make_callback_data(level=CURRENT_LEVEL+1, item_id=item.pk)

        # Вставляем кнопку в клавиатуру
        markup.insert(
            InlineKeyboardButton(text=button_text, callback_data=callback_data)
        )

    # Возвращаем созданную клавиатуру в хендлер
    return markup


async def schedule_bus():
    CURRENT_LEVEL = 0
    markup = InlineKeyboardMarkup(row_width=2)
    items = await get_schedule()
    for item in items:
        button_text = f"{item.title}"
        callback_data = make_callback_data_bus(level=CURRENT_LEVEL+1, id=item.pk)
        markup.insert(
            InlineKeyboardButton(text=button_text, callback_data=callback_data)
        )
    return markup


async def day_week(id):
    CURRENT_LEVEL = 1
    markup = InlineKeyboardMarkup(inline_keyboard=[
                                  [
                                      InlineKeyboardButton(
                                          text='    Будние    ',
                                          callback_data=make_callback_data_bus(level=CURRENT_LEVEL+1, id=id, b='1')
                                      ),
                                      InlineKeyboardButton(
                                          text='    Выходные    ',
                                          callback_data=make_callback_data_bus(level=CURRENT_LEVEL + 1, id=id, b='2'))

                                  ]])
    markup.row(
        InlineKeyboardButton(
            text="Назад",
            callback_data=make_callback_data_bus(level=CURRENT_LEVEL - 1, id=id))
    )

    return markup


def final_schedule(id, b):
    CURRENT_LEVEL = 2
    markup = InlineKeyboardMarkup()
    markup.row(
        InlineKeyboardButton(
            text="Назад",
            callback_data=make_callback_data_bus(level=CURRENT_LEVEL - 1, id=id, b=b))
    )
    return markup


def item_keyboard():
    CURRENT_LEVEL = 1
    markup = InlineKeyboardMarkup()
    markup.row(
        InlineKeyboardButton(
            text="Назад",
            callback_data=make_callback_data(level=CURRENT_LEVEL-1))
    )
    return markup



