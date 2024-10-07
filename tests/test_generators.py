import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


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


@pytest.mark.parametrize('start, stop, result', [
    (1, 3, ['0000 0000 0000 0001', '0000 0000 0000 0002', '0000 0000 0000 0003']),
    (12345678, 12345679, ['0000 0000 1234 5678', '0000 0000 1234 5679']),
    (1234123412341234, 1234123412341235, ['1234 1234 1234 1234', '1234 1234 1234 1235']),
    (1234123412341234, 12341234123412352, ['Неверно указан диапазон'])
])
def test_card_number_generator(start: int, stop: int, result: list) -> None:
    """Тест проверяет, что генератор выдает правильные номера карт в заданном диапазоне и требуемом формате,
    и обрабатывает ошибки некорректного ввода номера"""
    generator = list(card_number_generator(start, stop))
    assert generator == result


def test_card_number_generator_error() -> None:
    """Проверка, что генератор корректно обрабатывает крайние значения диапазона
     и правильно завершает генерацию"""
    generator = card_number_generator(1, 2)
    with pytest.raises(StopIteration) as exc_info:
        assert next(generator) == '0000 0000 0000 0001'
        assert next(generator) == '0000 0000 0000 0002'
        assert next(generator) == exc_info
