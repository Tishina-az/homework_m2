import pytest

from src.generators import filter_by_currency, transaction_descriptions


def test_filter_by_currency(transactions: list, transactions_usd: list, transactions_rub: list) -> None:
    """Тестирование функции на корректность фильтрации транзакций по указанной валюте"""
    result_usd = list(filter_by_currency(transactions, 'USD'))
    result_rub = list(filter_by_currency(transactions, 'RUB'))
    assert result_usd == transactions_usd
    assert result_rub == transactions_rub


def test_filter_by_currency_out(transactions: list) -> None:
    """Тестирование функции на обработку случаев, когда транзакции в заданной валюте отсутствуют"""
    result = list(filter_by_currency(transactions, 'AED'))
    assert result == []


def test_filter_by_currency_empty() -> None:
    """Тестирование функции на обработку случаев, когда транзакции в заданной валюте отсутствуют"""
    result = list(filter_by_currency([], 'AED'))
    assert result == []


def test_transaction_descriptions(transactions: list) -> None:
    """Тестирование функции на возврат корректного описания каждой транзакции"""
    generator = transaction_descriptions(transactions)
    assert next(generator) == 'Перевод организации'
    assert next(generator) == 'Перевод со счета на счет'
    assert next(generator) == 'Перевод со счета на счет'
    assert next(generator) == 'Перевод с карты на карту'
    assert next(generator) == 'Перевод организации'


def test_transaction_descriptions_values(transactions_rub: list) -> None:
    """Тестирование функции на пустой список"""
    with pytest.raises(StopIteration):
        assert next(transaction_descriptions([])) == []
        assert next(transaction_descriptions([])) == []
