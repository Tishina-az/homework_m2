from typing import Optional, Iterable


def filter_by_state(list_state: Iterable[dict], state: Optional[str] = 'EXECUTED') -> list[dict]:
    """ Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению """

    return [i for i in list_state if i['state'] == state]


def sort_by_date(list_date: Iterable[dict], sort_dir: bool = True) -> list[dict]:
    """ Функция возвращает список словарей, отсортированный по дате """

    return sorted(list_date, key=lambda i: i['date'], reverse=sort_dir)
