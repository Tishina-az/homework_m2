from src.generators import filter_by_currency


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
