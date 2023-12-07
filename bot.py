import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from datetime import datetime

from config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет!")

@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer("""Существующие команды:/n  
                         /start - приветственное сообщение/n
                         /help - окно справочной информации/n
                         /course - курсы валют на сегодня""")

@dp.message(Command("course"))
async def cmd_course(message: types.Message):
    # написать функционал получения текущего курса валют

    temp_data = datetime.now()
    str_data = f"{temp_data.day}.{temp_data.month}.{temp_data.year}"
    # await message.answer(f"курсы валют на {str_data}:\n" + "\n".join(res))

@dp.message()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
