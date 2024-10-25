import logging

import pandas as pd
from pandas.errors import EmptyDataError

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(filename)s:%(name)s: %(message)s",
    filename="../logs/transactions.log",
    filemode="w",
)

trans_logger = logging.getLogger("app.transactions")


def read_transactions_csv(path_csv: str) -> list[dict]:
    """Функция принимает на вход путь до файла"""
    try:
        trans_logger.info('Чтение файла .csv...')
        df = pd.read_csv(path_csv, delimiter=';')
        new_list = df.to_dict(orient='records')
        trans_logger.info('Чтение файла .csv выполнено успешно и возвращено в виде списка.')
        return new_list
    except FileNotFoundError as e:
        print('Файл не найден!')
        trans_logger.error(f'Файл не найден! Ошибка: {e}.')
        return []
    except EmptyDataError as e:
        print('Файл пуст!')
        trans_logger.error(f'Файл не содержит данных! Ошибка: {e}.')
        return []
    finally:
        trans_logger.info("Завершение работы функции...")


def read_transactions_xlsx(path_xlsx: str) -> list[dict]:
    """Функция принимает на вход путь до файла"""
    try:
        trans_logger.info('Чтение файла .xlsx...')
        df = pd.read_excel(path_xlsx)
        new_list = df.to_dict(orient='records')
        trans_logger.info('Чтение файла .xlsx выполнено успешно и возвращено в виде списка.')
        return new_list
    except FileNotFoundError as e:
        print('Файл не найден!')
        trans_logger.error(f'Файл не найден! Ошибка: {e}.')
        return []
    except ValueError as e:
        print('Ошибка данных!')
        trans_logger.error(f'Файл не содержит данных! Ошибка: {e}.')
        return []
    finally:
        trans_logger.info("Завершение работы функции...")
