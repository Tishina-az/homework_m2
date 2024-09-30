from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(name_account_card: str) -> str:
    """Функция возвращает строку с замаскированным номером счета или карты"""

    mask_number: str = ""
    numbers: list[str] = name_account_card.split()
    for num in numbers:
        if num.isdigit():
            if 16 <= len(num) <= 18:
                mask_number += get_mask_card_number(num)
            elif len(num) == 20:
                mask_number += get_mask_account(num)
            else:
                return "Некорректные данные!"
        else:
            mask_number += num + " "

    return mask_number


def get_date(date: str) -> str:
    """Функция, которая возвращает корректную дату вида "ДД.ММ.ГГГГ" ("11.03.2024")"""

    if "".join(date[:10].split("-")).isdigit():
        return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"
    else:
        return "Неверный формат даты!"
