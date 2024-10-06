from functools import wraps
from time import time
from typing import Any, Callable, Optional


def log(filename: Optional[str]=None) -> Callable:
    def wrappers(function: Callable) -> Callable:
        @wraps(function)
        def inner(*args: Any, **kwargs: Any) -> Any:
            try:
                time_start = time()
                result_log = function(*args, **kwargs)
                time_end = time()
                result_txt = f"""Функция {function.__name__} работает корректно!
Результат работы функции: {result_log}. Время работы функции:{time_end - time_start: .10f}.\n"""
                if filename is not None:
                    with open(filename, 'a', encoding='utf-8') as file:
                        file.write(result_txt)
                else:
                    print(result_txt)
            except Exception as e:
                result_txt = f"""Функция {function.__name__} работает некорректно, ошибка: {e}
Входные данные: {args}, {kwargs}.\n"""
                if filename is not None:
                    with open(filename, 'a', encoding='utf-8') as file:
                        file.write(result_txt)
                else:
                    print(result_txt)
        return inner
    return wrappers
