from aiogram import Bot, Dispatcher, executor, types
import logging
from db import Database

TOKEN = "2138280761:AAFm9Mo__bmS9lLDBamjyLY4XEdZCHQHyHA"

bot = Bot(token=TOKEN)
db = Database('identifier.sqlite')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if not db.user_exists(message.from_user.id):
        db.add_user(message.from_user.id)
        await bot.send_message(message.from_user.id, 'Укажите имя вашей компании')
    else:
        await bot.send_message(message.from_user.id, 'Вы уже зарегистрированы!')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
