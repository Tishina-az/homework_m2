import logging
from typing import Union


masks_logger = logging.getLogger('app.masks')
file_handler = logging.FileHandler('../logs/masks.log', mode='w')
file_formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(filename)s:%(name)s: %(message)s')
file_handler.setFormatter(file_formatter)
masks_logger.addHandler(file_handler)
masks_logger.setLevel(logging.INFO)


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """Принимает на вход номер карты и возвращает ее маску"""
    masks_logger.info('Запуск функции преобразования номера карты.')
    if 16 <= len(str(card_number)) <= 18:
        if str(card_number).isdigit():
            formated_card = str(card_number).replace(str(card_number)[6:-4], "******")
            mask_card = " ".join([formated_card[i:i + 4] for i in range(0, len(str(card_number)), 4)])
            masks_logger.info('Номер карты успешно отформатирован!')
            masks_logger.info('Завершение работы функции.')
            return mask_card
        masks_logger.error(f'Номер карты содержит недопустимые символы: {card_number}.')
        masks_logger.info('Завершение работы функции.')
        return 'Неверный формат номера карты!'
    masks_logger.error(f'Неверный формат номера карты: {card_number}.')
    masks_logger.info('Завершение работы функции.')
    return 'Неверный формат номера карты!'


def get_mask_account(account_number: Union[int, str]) -> str:
    """Преобразует номер счёта в маску вида **XXXX"""
    masks_logger.info('Запуск функции преобразования номера счёта.')
    if len(str(account_number)) == 20:
        if str(account_number).isdigit():
            mask_account = str(account_number).replace(str(account_number)[:-4], "**")
            masks_logger.info('Номер счёта успешно отформатирован!')
            masks_logger.info('Завершение работы функции.')
            return mask_account
        masks_logger.error(f'Номер счёта содержит недопустимые символы: {account_number}.')
        masks_logger.info('Завершение работы функции.')
        return 'Неверный формат номера счёта!'
    masks_logger.error(f'Неверная длина номера счёта: {account_number}.')
    masks_logger.info('Завершение работы функции.')
    return 'Неверный формат номера счёта!'
