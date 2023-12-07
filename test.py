import requests


def get_current_courses():
    temp_rub = requests.get(" https://api.nbrb.by/exrates/rates/456")
    temp_usd = requests.get(" https://api.nbrb.by/exrates/rates/USD?parammode=2")
    print(temp_rub.text)
    print()
    print(temp_usd.text)