from aiogram import Bot, Dispatcher, executor
from handlers import start, process_message
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("TG_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

if __name__ == '__main__':
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(process_message, content_types=['text'])
    executor.start_polling(dp, skip_updates=True)
