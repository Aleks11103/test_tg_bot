import asyncio
import json
import requests
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from datetime import datetime

from config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет!\n\nДля получения списка комманд введите /help")


@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    res = ["Существующие команды:", 
           "/start - приветственное сообщение", 
           "/help - окно справочной информации", 
           "/course - курсы валют на сегодня",
           "/weather - текущая погода по городу Минск"
    ]
    await message.answer("\n".join(res))


@dp.message(Command("course"))
async def cmd_course(message: types.Message):
    dict_course = {}
    # Список запрашиваемых курсов валют
    list_rates = ["RUB", "USD", "EUR"]
    res = []
    # Получение текущей даты
    temp_data = datetime.now()
    str_data = f"{temp_data.day}.{temp_data.month}.{temp_data.year}"
    res.append(f"Курсы валют на {str_data}:\n")
    # Получение текущего курса валют
    # temp_all = requests.get("https://api.nbrb.by/exrates/currencies")
    for el in list_rates:
        req = f"https://api.nbrb.by/exrates/rates/{el}?parammode=2"
        request = requests.get(req)
        temp_dict = json.loads(request.text)
        name = f'{temp_dict["Cur_Scale"]} {temp_dict["Cur_Name"]}'
        dict_course[name] = temp_dict["Cur_OfficialRate"]
    for key, val in dict_course.items():
        res.append(f"{key} = {val} бел. руб.")
    await message.answer("\n".join(res))


@dp.message(Command("weather"))
async def cmd_course(message: types.Message):
    res = ["Ответ от сервиса OpenWeatherMap:\n"]
    # Отправка запроса к API сервису OpenWetherMap.org
    request = requests.get("https://api.openweathermap.org/data/2.5/weather",
                        params={
                            'q': 'Минск', 
                            'type': 'like', 
                            'units': 'metric',
                            'appid': '1f5154c1cf4498da3cc13f8c539278ec', 
                            'lang': 'ru'
                        })
    temp_dict = json.loads(request.text)
    # Формирование словаря с данными
    d = {
        "Город": temp_dict["name"],
        "Облачность": temp_dict['weather'][0]['description'],
        "Температура": f"{temp_dict['main']['temp']} °C",
        "Влажность": f"{temp_dict['main']['humidity']} %",
        "Скорость ветра": f"{temp_dict['wind']['speed']} м/с",
    }
    for key, val in d.items():
        res.append(f"{key}:   {val}")
    await message.answer("\n".join(res))


@dp.message()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
