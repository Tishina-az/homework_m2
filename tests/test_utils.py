import json
import os.path
from unittest.mock import patch

from src.utils import read_file_transactions


@patch('builtins.open')
def test_read_file_transactions(mock_open):
    path = os.path.join(os.path.dirname(__file__), 'data/operations.json')
    path_wrong = os.path.join(os.path.dirname(__file__), 'data/operation.json')
    mock_file = mock_open.return_value.__enter__.return_value
    mock_file.read.return_value = json.dumps([{'login': 'testuser', 'name': 'Test User'}])
    assert read_file_transactions(path) == [{'login': 'testuser', 'name': 'Test User'}]
    mock_file.read.return_value = json.dumps({'login': 'testuser', 'name': 'Test User'})
    assert read_file_transactions(path) == []
    mock_file.read.return_value = ''
    assert read_file_transactions(path) == []
