import re
from collections import Counter
from typing import Iterable


def filter_by_state(list_state: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """ Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению """

    return [i for i in list_state if i.get('state').lower() == state.lower()]


def sort_by_date(list_date: Iterable[dict], sort_dir: bool = True) -> list[dict]:
    """ Функция возвращает список словарей, отсортированный по дате """

    return sorted(list_date, key=lambda i: i['date'], reverse=sort_dir)


def filter_by_search_line(list_transactions: list[dict], search_line: str) -> list[dict]:
    """ Функция возвращает список словарей, содержащих строку поиска в описании """

    # return [i for i in list_transactions if search_line.lower() in i.get('description').lower()]
    return [i for i in list_transactions if re.search(search_line, i.get('description'), flags=re.IGNORECASE)]


def count_by_category(list_transactions: list[dict], list_category: list) -> dict:
    """ Функция возвращает словарь, в котором ключ - название категории, а значение - количество операций """

    category = [i['description'] for i in list_transactions if i.get('description') in list_category]
    count_category = dict(Counter(category))

    return count_category
