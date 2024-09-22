from typing import Union


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """Принимает на вход номер карты и возвращает ее маску"""
    formated_card = str(card_number).replace(str(card_number)[6:-4], "******")
    num_length = 4  # Число для разбивки номера карты на блоки
    mask_card = " ".join([formated_card[i:i + num_length] for i in range(0, len(str(card_number)), num_length)])
    return mask_card


def get_mask_account(account_number: Union[int, str]) -> str:
    """Преобразует номер счёта в маску вида **XXXX"""
    mask_account = str(account_number).replace(str(account_number)[:-4], "**")
    return mask_account
