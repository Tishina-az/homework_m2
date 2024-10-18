import os

import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY_EX")


def get_amount_transaction(transaction: dict) -> float:
    """Функция возвращает сумму транзакции в рублях"""
    currency = transaction["operationAmount"]["currency"]["code"]
    amount = transaction["operationAmount"]["amount"]
    if currency == "RUB":
        return float(amount)
    else:
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"

        headers = {"apikey": api_key}

        response = requests.get(url, headers=headers)
        status_code = response.status_code

        if status_code != 200:
            print(f"Ошибка {status_code}, попробуйте ещё раз!")
            return False
        else:
            result = round(response.json().get("result"), 2)
            return float(result)
