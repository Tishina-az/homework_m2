from typing import Generator, Optional


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


def card_number_generator(start: Optional[int] = 1, finish: Optional[int] = 9999999999999999) -> Generator:
    """Функция генерирует номера карт в заданном диапазоне"""
    for i in range(start, finish + 1):
        card_number = str(i)
        while len(card_number) < 16:
            card_number = '0' + card_number
        mask_card = " ".join([card_number[i:i + 4] for i in range(0, len(str(card_number)), 4)])
        yield mask_card
