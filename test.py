import requests
import json


# request = requests.get("api.openweathermap.org/data/2.5/weather?q=Minsk,blr&APPID=1f5154c1cf4498da3cc13f8c539278ec")
request = requests.get("https://api.openweathermap.org/data/2.5/weather",
                        params={
                            'q': 'Минск', 
                            'type': 'like', 
                            'units': 'metric',
                            'appid': '1f5154c1cf4498da3cc13f8c539278ec', 
                            'lang': 'ru'
                        })
temp_dict = json.loads(request.text)
d = {
    "Город": temp_dict["name"],
    "Облачность": temp_dict["weather"][0]["description"], 
    "Температура": temp_dict["main"]["temp"],
    "Влажность": temp_dict["main"]["humidity"],
    "Скорость ветра": temp_dict["wind"]["speed"],
    }
print("Ответ от сервиса OpenWeatherMap:")
for key, val in d.items():
    print(f"{key}: {val}")


# weather [{'id': 804, 'main': 'Clouds', 'description': 'пасмурно', 'icon': '04n'}]
# base stations
# main {'temp': 3.86, 'feels_like': -2.21, 'temp_min': 3.86, 'temp_max': 3.86, 'pressure': 990, 'humidity': 91, 'sea_level': 990, 'grnd_level': 964}
# visibility 10000
# wind {'speed': 11.07, 'deg': 263, 'gust': 20.69}
# clouds {'all': 100}
# dt 1703534398
# sys {'type': 1, 'id': 8939, 'country': 'BY', 'sunrise': 1703485656, 'sunset': 1703512282}
# timezone 10800
# id 625144
# name Минск
# cod 200