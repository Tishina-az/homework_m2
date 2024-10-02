from typing import Generator


def filter_by_currency(transactions: list[dict], currency: str) -> Generator:
    """Функция возвращает итератор, который поочередно выдает транзакции,
     где валюта операции соответствует заданной (например, USD)."""
    for trans in transactions:
        if trans["operationAmount"]["currency"]["code"] == currency:
            yield trans


def transaction_descriptions(transactions: list[dict]) -> Generator:
    """Генератор принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""
    for trans in transactions:
        if trans["description"]:
            yield trans["description"]
