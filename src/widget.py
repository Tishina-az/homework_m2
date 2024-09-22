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
            mask_number += num + " "
            # mask_number += " "

    return mask_number


# print(mask_account_card('Visa Classic 6831982476737658')) - проверка кода

def get_date(date: str) -> str:
    """ Функция, которая возвращает корректную дату вида "ДД.ММ.ГГГГ" ("11.03.2024") """
    return f'{date[8:10]}.{date[5:7]}.{date[0:4]}'


# print(get_date('2024-03-11T02:26:18.671407')) - проверка кода
