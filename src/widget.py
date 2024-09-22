from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(name_account_card: str) -> str:
    """Функция возвращает строку с замаскированным номером счета или карты"""

    mask_number: str = ""
    numbers: list[str] = name_account_card.split()
    for num in numbers:
        if num.isdigit():
            if len(num) == 16:
                mask_number += get_mask_card_number(num)
            else:
                mask_number += get_mask_account(num)
        else:
            mask_number += num + " "

    return mask_number


def get_date(date: str) -> str:
    """Функция, которая возвращает корректную дату вида "ДД.ММ.ГГГГ" ("11.03.2024")"""

    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"
