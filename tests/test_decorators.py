import tempfile

from src.decorators import log


def test_log_good():
    """Тестирует выполнение декорированной функции"""
    @log()
    def my_function(x, y):
        return x + y

    assert my_function(1, 2) == 3


def test_log(capsys):
    """Тестирует вывод в консоль после успешного выполнения функции"""
    @log()
    def my_function(x, y):
        return x + y

    my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == """Функция my_function работает корректно!
Результат работы функции: 3. Время работы функции: 0.00000.\n\n"""


def test_log_error(capsys):
    """Тестирует вывод в консоль после ошибки"""
    @log()
    def my_function(x, y):
        return x + y

    my_function(1, 'f')
    captured = capsys.readouterr()
    assert captured.out == """Функция my_function работает некорректно, ошибка: unsupported operand type(s) for +: 'int' and 'str'.
Входные данные: (1, 'f'), {}.\n\n"""


def test_log_good_file(capsys):
    """Тестирование записи в файл после успешного выполнения функции"""
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        log_file_path = tmp_file.name

    @log(filename=log_file_path)
    def my_function(x, y):
        return x + y
    my_function(1, 2)
    with open(log_file_path, 'r', encoding='utf-8') as file:
        logs = file.read()
    assert """Функция my_function работает корректно!
Результат работы функции: 3. Время работы функции: 0.00000.\n""" in logs


def test_log_error_file(capsys):
    """Тестирование записи в файл после ошибки в выполнении функции"""
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        log_file_path = tmp_file.name

    @log(filename=log_file_path)
    def my_function(x, y):
        return x + y
    my_function(1, 'f')
    with open(log_file_path, 'r', encoding='utf-8') as file:
        logs = file.read()
    assert """Функция my_function работает некорректно, ошибка: unsupported operand type(s) for +: 'int' and 'str'.
Входные данные: (1, 'f'), {}.\n""" in logs
