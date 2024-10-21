import json
import os.path
from unittest.mock import patch

from src.utils import read_file_transactions


@patch('builtins.open')
def test_read_file_transactions(mock_open):
    """Тестирует поведение функции при различных вариантах содержания файла"""
    path = os.path.join(os.path.dirname(__file__), 'data/operations.json')
    mock_file = mock_open.return_value.__enter__.return_value
    # корректные данные
    mock_file.read.return_value = json.dumps([{'login': 'testuser', 'name': 'Test User'}])
    assert read_file_transactions(path) == [{'login': 'testuser', 'name': 'Test User'}]
    # данные не соответствуют условиям, не список
    mock_file.read.return_value = json.dumps({'login': 'testuser', 'name': 'Test User'})
    assert read_file_transactions(path) == []
    # пустой файл
    mock_file.read.return_value = ''
    assert read_file_transactions(path) == []
