from typing_extensions import Generator


def filter_by_currency(transactions: list[dict], currency: str) -> Generator:
    """Функция возвращает итератор, который поочередно выдает транзакции,
     где валюта операции соответствует заданной (например, USD)."""
    for trans in transactions:
        if trans["operationAmount"]["currency"]["code"] == currency:
            yield trans
