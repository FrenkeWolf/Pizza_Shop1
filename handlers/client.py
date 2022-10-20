from bot_telegram import dp, bot
from aiogram import types



@dp.message_handler(commands=['start', 'help'])
async def commands_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Привет')
        await message.delete()
    except:
        await message.reply('Общение с ботом только через ЛС. Перейди на:\n https://t.me/Fluffy_my_bot') \


@dp.message_handler(commands=['Узнать адрес'])
async def commands_address(message: types.Message):
    await bot.send_message(message.from_user.id, 'Береговая 2')


@dp.message_handler(commands=['Меню'])
async def commands_menu(message: types.Message):
    await bot.send_message(message.from_user.id, 'menu')


@dp.message_handler(commands=['Режим работы'])
async def commands_working_time(message: types.Message):
    await bot.send_message(message.from_user.id, 'Пн-Пт с 09.00 по 20.00')
