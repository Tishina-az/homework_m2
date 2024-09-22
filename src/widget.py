from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(name_account_card: str) -> str:
    """ Функция возвращает строку с замаскированным номером счета или карты """
    mask_number = ""
    numbers = name_account_card.split()
    for num in numbers:
        if num.isdigit():
            if len(num) == 16:
                mask_num = get_mask_card_number(num)
                mask_number += mask_num
            else:
                mask_num = get_mask_account(num)
                mask_number += mask_num
        else:
            mask_number += num
            mask_number += " "

    return mask_number


# print(mask_account_card('Счет 73654108430135874305')) - проверка кода
