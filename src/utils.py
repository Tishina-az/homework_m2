import json
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s:%(levelname)s:%(filename)s:%(name)s: %(message)s",
    filename="../logs/utils.log",
    filemode="w",
)

utils_logger = logging.getLogger("app.utils")


def read_file_transactions(path: str) -> list[dict]:
    """Функция читает json-файл и возвращает список словарей с транзакциями"""
    try:
        utils_logger.info("Запуск функции...")
        with open(path) as file:
            try:
                utils_logger.info("Чтение json-файла...")
                transactions = json.load(file)
                if isinstance(transactions, list):
                    utils_logger.info("Файл успешно прочитан и возвращён в виде списка.")
                    return transactions
                else:
                    utils_logger.warning("Неверный формат данных в файле!")
                    return []
            except (TypeError, json.JSONDecodeError) as error:
                utils_logger.error(f"Чтение файла привело к ошибке: {error}.")
                print("Некорректное содержание файла!")
                return []
    except FileNotFoundError as error_1:
        utils_logger.error(f"Файл не найден! Ошибка: {error_1}.")
        print("Файл не найден!")
        return []
    finally:
        utils_logger.info("Завершение работы функции...")
