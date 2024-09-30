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


@pytest.fixture
def check_state() -> list:
    return [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]


@pytest.fixture
def state_executed() -> list:
    return [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    ]


@pytest.fixture
def state_canceled() -> list:
    return [
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]


@pytest.fixture
def check_state_sort_up() -> list:
    return [
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}
    ]


@pytest.fixture
def check_state_sort_down() -> list:
    return [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
    ]


@pytest.fixture
def check_same_date() -> list:
    return [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 41428850, 'state': 'CANCELED', 'date': '2019-07-03T18:33:50.512362'}
    ]


@pytest.fixture
def check_same_date_reverse() -> list:
    return [
        {'id': 41428850, 'state': 'CANCELED', 'date': '2019-07-03T18:33:50.512362'},
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}
    ]


@pytest.fixture
def check_same_date_incorrect() -> list:
    return [
        {'id': 41428850, 'state': 'CANCELED', 'date': '2019:07:03T18:33:50.512362'},
        {'id': 41428829, 'state': 'EXECUTED', 'date': '20190703T18:35:29.512364'},
        {'id': 41428829, 'state': 'EXECUTED', 'date': ''},
        {'id': 41428850, 'state': 'CANCELED', 'date': '2019:07:03'}
    ]


@pytest.fixture
def check_same_date_incorrect_out() -> list:
    return [
        {'id': 41428850, 'state': 'CANCELED', 'date': '2019:07:03T18:33:50.512362'},
        {'id': 41428850, 'state': 'CANCELED', 'date': '2019:07:03'},
        {'id': 41428829, 'state': 'EXECUTED', 'date': '20190703T18:35:29.512364'},
        {'id': 41428829, 'state': 'EXECUTED', 'date': ''}
    ]
