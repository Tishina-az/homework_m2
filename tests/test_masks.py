from src.masks import get_mask_account, get_mask_card_number

# from tests.conftest import account_number_int, account_number_str, card_number_int, card_number_str


def test_get_mask_card_number_int(card_number_int: int, card_number_str: str) -> None:
    """Тестирование правильности маскирования номера карты в формате числа и строки"""
    assert get_mask_card_number(card_number_int) == "7000 79** **** 6361"
    assert get_mask_card_number(card_number_str) == "7000 79** **** 6361"


def test_get_mask_card_number_letter() -> None:
    """Тест на обработку ошибки ввода номера карты, в случае ввода посторонних символов"""
    assert get_mask_card_number("7000792a89606361") == "Неверный формат номера карты!"
    assert get_mask_card_number("7&00792a89-06361") == "Неверный формат номера карты!"


def test_get_mask_card_number_long(account_number_int: int, account_number_str: str) -> None:
    """Тест на обработку неверной длины номера карты"""
    assert get_mask_card_number(account_number_int) == "Неверный формат номера карты!"
    assert get_mask_card_number(account_number_str) == "Неверный формат номера карты!"


def test_get_mask_card_number_empty(empty_value: str) -> None:
    """Тест на обработку ошибки, при пустом значении номера карты"""
    assert get_mask_card_number(empty_value) == "Неверный формат номера карты!"


def test_get_mask_account(account_number_int: int, account_number_str: str) -> None:
    """Тестирование правильности маскирования номера счёта в формате числа и строки"""
    assert get_mask_account(account_number_int) == "**4305"
    assert get_mask_account(account_number_str) == "**4305"


def test_get_mask_account_letter() -> None:
    """Тест на обработку ошибки ввода номера счёта, в случае ввода посторонних символов"""
    assert get_mask_account("736541084N013a874305") == "Неверный формат номера счёта!"
    assert get_mask_account("73654#08430-35874305") == "Неверный формат номера счёта!"


def test_get_mask_account_long(card_number_int: int, card_number_str: str) -> None:
    """Тест на обработку неверной длины номера счёта"""
    assert get_mask_account(card_number_int) == "Неверный формат номера счёта!"
    assert get_mask_account(card_number_str) == "Неверный формат номера счёта!"


def test_get_mask_account_empty(empty_value: str) -> None:
    """Тест на обработку ошибки, при пустом значении номера счёта"""
    assert get_mask_account(empty_value) == "Неверный формат номера счёта!"
