from unittest.mock import patch

from pandas.errors import EmptyDataError

from src.transactions import read_transactions_csv, read_transactions_xlsx


@patch('pandas.read_csv')
def test_read_transactions_csv(mock_read, state_executed):
    """Тестирует поведение функции при корректном содержании файла"""
    mock_read.return_value.to_dict.return_value = state_executed
    assert read_transactions_csv('../data/transactions/transactions.csv') == state_executed


@patch('pandas.read_csv')
def test_read_transactions_csv_empty(mock_read, capsys):
    """Тестирует поведение функции для пустого файла"""
    mock_read.side_effect = EmptyDataError
    assert read_transactions_csv('empty_file.csv') == []
    captured = capsys.readouterr()
    assert captured.out == 'Файл пуст!\n'


@patch('pandas.read_csv')
def test_read_transactions_csv_not_found(mock_read, capsys):
    """Тестирует поведение функции при неверном пути до файла"""
    mock_read.side_effect = FileNotFoundError
    assert read_transactions_csv('wrong_path.csv') == []
    captured = capsys.readouterr()
    assert captured.out == 'Файл не найден!\n'


@patch('pandas.read_excel')
def test_read_transactions_xlsx(mock_read, state_executed):
    """Тестирует поведение функции при корректном содержании файла"""
    mock_read.return_value.to_dict.return_value = state_executed
    assert read_transactions_xlsx('transactions_excel.xlsx') == state_executed


@patch('pandas.read_excel')
def test_read_transactions_xlsx_empty(mock_read, capsys):
    """Тестирует поведение функции для пустого файла"""
    mock_read.side_effect = EmptyDataError
    assert read_transactions_xlsx('empty_file_excel.xlsx') == []
    captured = capsys.readouterr()
    assert captured.out == 'Ошибка данных!\n'


@patch('pandas.read_excel')
def test_read_transactions_xlsx_not_found(mock_read, capsys):
    """Тестирует поведение функции при неверном пути до файла"""
    mock_read.side_effect = FileNotFoundError
    assert read_transactions_xlsx('wrong_path.xlsx') == []
    captured = capsys.readouterr()
    assert captured.out == 'Файл не найден!\n'
