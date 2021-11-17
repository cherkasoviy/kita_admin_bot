from aiogram import Bot, Dispatcher, executor, types
from db import Database

TOKEN = "2138280761:AAFm9Mo__bmS9lLDBamjyLY4XEdZCHQHyHA"
CHANNEL_ID = '-1001618707300'

bot = Bot(token=TOKEN)
db = Database('identifier.sqlite')
dp = Dispatcher(bot)


def check_sub_channel(chat_member):
    if chat_member['status'] != 'left':
        return True


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if not db.user_exists(message.from_user.id):
        db.add_user(message.from_user.id)
        await bot.send_message(message.from_user.id, 'Укажите имя вашей компании')
    elif not check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
        await bot.send_message(message.from_user.id, 'Подпишитесь на канал!')
    else:
        await bot.send_message(message.from_user.id, 'Вы уже зарегистрированы и подписаны!')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
