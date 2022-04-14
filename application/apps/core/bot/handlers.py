from aiogram import Dispatcher
from aiogram.types import Message

from config.apps import INSTALLED_APPS

from .. import services


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands=["start"])

    dp.register_message_handler(send_my_id, commands=["id"])

    dp.register_message_handler(send_my_apps, commands=["apps"])

    dp.register_message_handler(simple_handler, commands=["core"])


async def start(message: Message):
    user, is_created = await services.add_user(
        tg_id=message.from_user.id,
        chat_id=message.chat.id,
        first_name=message.from_user.first_name,
    )

    if is_created:
        await message.answer("Это информационный бот города Жодино\nНа данный момент вы можете посмотреть афишу кинотеатра Юность и расписание городского транспорта и маршруток\nНовая информация будет добовляться по мере развития бота \n\nЧто бы зайти в меню отправьте /menu ")
    else:
        await message.answer("Это информационный бот города Жодино\nНа данный момент вы можете посмотреть афишу кинотеатра Юность и расписание городского транспорта и маршруток\nНовая информация будет добовляться по мере развития бота \n\nЧто бы зайти в меню отправьте /menu ")


async def send_my_id(message: Message):
    await message.answer(
        f"User Id: <b>{message.from_user.id}</b>\n" f"Chat Id: <b>{message.chat.id}</b>"
    )


async def send_my_apps(message: Message):
    apps_names = ""
    for app in INSTALLED_APPS:
        apps_names += app.Config.name + "\n"

    await message.answer("Installed apps:\n" f"{apps_names}")


async def simple_handler(message: Message):
    await message.answer('Hello from "Core" app!')
