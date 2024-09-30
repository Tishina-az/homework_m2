from typing import Any

import pytest

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(check_state: list, state_executed: list, state_canceled: list) -> None:
    """Тестирование фильтрации списка словарей по заданному статусу state"""
    assert filter_by_state(check_state) == state_executed
    assert filter_by_state(check_state, 'CANCELED') == state_canceled


def test_filter_by_state_out(state_executed: list, state_canceled: list) -> None:
    """Проверка работы функции при отсутствии словарей с указанным статусом state в списке"""
    assert filter_by_state(state_canceled) == []
    assert filter_by_state(state_executed, 'CANCELED') == []


@pytest.mark.parametrize('list_state, state, filter_list', [
    ([{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}], 12, []),
    ([], "", [])
])
def test_filter_by_state_values(list_state: list, state: Any, filter_list: list) -> None:
    """Параметризация тестов для различных возможных значений статуса state"""
    assert filter_by_state(list_state, state) == filter_list


def test_sort_by_date(check_state: list, check_state_sort_down: list, check_state_sort_up: list) -> None:
    """Тестирование сортировки списка словарей по датам в порядке убывания и возрастания"""
    assert sort_by_date(check_state) == check_state_sort_down
    assert sort_by_date(check_state, False) == check_state_sort_up


def test_sort_by_date_same_date(check_same_date: list, check_same_date_reverse: list) -> None:
    """Проверка корректности сортировки при одинаковых датах"""
    assert sort_by_date(check_same_date) == check_same_date
    assert sort_by_date(check_same_date, False) == check_same_date_reverse


def test_sort_by_date_incorrect(check_same_date_incorrect: list, check_same_date_incorrect_out: list) -> None:
    """Тесты на работу функции с некорректными или нестандартными форматами дат"""
    assert sort_by_date(check_same_date_incorrect) == check_same_date_incorrect_out
