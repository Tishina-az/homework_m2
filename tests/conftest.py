import pytest


@pytest.fixture
def card_number_int() -> int:
    return 7000792289606361


@pytest.fixture
def card_number_str() -> str:
    return '7000792289606361'


@pytest.fixture
def account_number_int() -> int:
    return 73654108430135874305


@pytest.fixture
def account_number_str() -> str:
    return '73654108430135874305'


@pytest.fixture
def empty_value() -> str:
    return ''


@pytest.fixture
def card_type() -> str:
    return 'Maestro 1596837868705199'


@pytest.fixture
def account_type() -> str:
    return 'Счет 64686473678894779589'
