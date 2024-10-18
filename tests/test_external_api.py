from unittest.mock import patch, MagicMock

from src.external_api import get_amount_transaction


def test_get_amount_transaction_rub(transactions_rub: list[dict]) -> None:
    """Тестируем поведение функции для атрибута RUB"""
    transactions_1 = transactions_rub[0]
    transactions_2 = transactions_rub[1]
    assert get_amount_transaction(transactions_1) == 43318.34
    assert get_amount_transaction(transactions_2) == 67314.70


@patch('requests.get')
def test_get_amount_transaction_usd(mock_get: MagicMock, transactions_usd: list[dict]) -> None:
    """Тестируем функцию на возврат суммы операции с учетом курса USD"""
    transaction = transactions_usd[1]
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 3724.30}
    assert get_amount_transaction(transaction) == 3724.30


@patch('requests.get')
def test_get_amount_transaction_error(mock_get: MagicMock, transactions_usd: list[dict]) -> None:
    """Тестируем функцию в случае несоответствия статус-кода"""
    transaction = transactions_usd[1]
    mock_get.return_value.status_code = 401
    mock_get.return_value.json.return_value = {"massage": "Ошибка авторизации"}
    assert get_amount_transaction(transaction) == False
