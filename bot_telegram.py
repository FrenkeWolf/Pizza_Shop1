from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import os

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)


async def on_startup(_):
    print('бот вышел в онлайн')


# @dp.message_handler()
# async def echo_send(message: types.Message):
#     await message.answer(message.text)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
'''Необходим для пропуска обновлений во время сна бота'''
