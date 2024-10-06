import pytest

from src.widget import get_date, mask_account_card

# from tests.conftest import card_number_int, card_number_str


def test_mask_account_card(card_type: str, account_type: str) -> None:
    """Тест на распознавание типа вводных данных и корректной маскировки"""
    assert mask_account_card(card_type) == 'Maestro 1596 83** **** 5199'
    assert mask_account_card(account_type) == 'Счет **9589'


@pytest.mark.parametrize('name_account_card, mask_number', [
    ('MasterCard 7158300734726758', 'MasterCard 7158 30** **** 6758'),
    ('Счет 35383033474447895560', 'Счет **5560'),
    ('Visa Classic 6831982476737658', 'Visa Classic 6831 98** **** 7658'),
    ('Visa Platinum 8990922113665229', 'Visa Platinum 8990 92** **** 5229'),
    ('Счет 73654108430135874305', 'Счет **4305')
])
def test_mask_account_card_values(name_account_card: str, mask_number: str) -> None:
    """Параметризованные тесты с разными типами карт и счетов для проверки универсальности функции"""
    assert mask_account_card(name_account_card) == mask_number


@pytest.mark.parametrize('name_account_card, mask_number', [
    ('MasterCard 71583004726758', 'Некорректные данные!'),
    ('Счет 3538303347400447895560', 'Некорректные данные!'),
    ('', '')
])
def test_mask_account_card_incorrect(name_account_card: str, mask_number: str) -> None:
    """Тестирование функции на обработку некорректных входных данных и проверка ее устойчивости к ошибкам"""
    assert mask_account_card(name_account_card) == mask_number


def test_get_date() -> None:
    """Тестирование правильности преобразования даты"""
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"


@pytest.mark.parametrize('input_date, output_date', [
    ('2024-03-11T02.671407', '11.03.2024'),
    ('2h24-03-11T02:26:18.671407', 'Неверный формат даты!')
])
def test_get_date_varius(input_date: str, output_date: str) -> None:
    """Тестирование различных форматов даты"""
    assert get_date(input_date) == output_date


def test_get_date_empty(empty_value: str) -> None:
    """Тестирование функции при отсутствии даты"""
    assert get_date(empty_value) == "Неверный формат даты!"
