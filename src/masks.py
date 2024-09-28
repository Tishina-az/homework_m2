from typing import Union


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """Принимает на вход номер карты и возвращает ее маску"""
    if 16 <= len(str(card_number)) <= 18:
        if str(card_number).isdigit():
            formated_card = str(card_number).replace(str(card_number)[6:-4], "******")
            mask_card = " ".join([formated_card[i:i + 4] for i in range(0, len(str(card_number)), 4)])
            return mask_card
        return 'Неверный формат номера карты!'
    return 'Неверный формат номера карты!'


def get_mask_account(account_number: Union[int, str]) -> str:
    """Преобразует номер счёта в маску вида **XXXX"""
    if len(str(account_number)) == 20:
        if str(account_number).isdigit():
            mask_account = str(account_number).replace(str(account_number)[:-4], "**")
            return mask_account
        return 'Неверный формат номера счёта!'
    return 'Неверный формат номера счёта!'
