from typing import Optional, Iterable


def filter_by_state(list_dict: Iterable[dict], state: Optional[str] = 'EXECUTED') -> list[dict]:
    """ Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению """

    return [i for i in list_dict if i['state'] == state]
