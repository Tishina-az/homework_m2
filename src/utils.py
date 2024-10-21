import json


def read_file_transactions(path: str) -> list[dict]:
    """Функция читает json-файл и возвращает список словарей с транзакциями"""
    try:
        with open(path) as file:
            try:
                transactions = json.load(file)
                if isinstance(transactions, list):
                    return transactions
                else:
                    return []
            except (TypeError, json.JSONDecodeError):
                print("Некорректное содержание файла!")
                return []
    except FileNotFoundError:
        print("Файл не найден!")
        return []
