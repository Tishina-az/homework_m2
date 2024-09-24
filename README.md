# Проект 'Виджет банковских операций'

## Описание:

Проект 'Виджет банковских операций' - это виджет, который показывает несколько последних
успешных банковских операций клиента.

## Установка:

1. Клонируйте репозиторий:
```
git clone git@github.com:Tishina-az/homework_m2.git
```
2. Установите зависимости:

*Раздел находится в разработке.*

## Использование функций:

1. Работа функций в модуле `masks`:
    - Функция `get_mask_card_number` принимает на вход номер карты и возвращает ее маску. 
   Номер карты замаскирован и отображается в формате `XXXX XX** **** XXXX`, где `X` — это цифра номера.
   Пример работы функции:
   ```
    7000792289606361     # входной аргумент
    7000 79** **** 6361  # выход функции
   ```
   - Функция `get_mask_account` принимает на вход номер счета и возвращает его маску. 
   Номер счета замаскирован и отображается в формате `**XXXX`, где `X` — это цифра номера.
   Пример работы функции:
   ```
    73654108430135874305  # входной аргумент
    **4305  # выход функции
   ```
   
2. Работа функций в модуле `widget`:
    - Функция `mask_account_card` принимает один аргумент — строку, типа `Visa Platinum 7000792289606361`, 
    или `Maestro 7000792289606361`, или `Счет 73654108430135874305`. 
    Разделять строку на 2 аргумента (отдельно имя, отдельно номер) **нельзя!**
    Возвращает строку с замаскированным номером, используя разные типы:
    ```
    # Пример для карты
    Visa Platinum 7000792289606361  # входной аргумент
    Visa Platinum 7000 79** **** 6361  # выход функции

    # Пример для счета
    Счет 73654108430135874305  # входной аргумент
    Счет **4305  # выход функции
    ```
   - Функция `get_date`, которая принимает на вход строку с датой в формате `"2024-03-11T02:26:18.671407"`
   и возвращает строку с датой в формате `"ДД.ММ.ГГГГ"` (`"11.03.2024"`).


3. Работа функций в модуле `processing`:
    - Функция `filter_by_state`, которая принимает список словарей и опционально значение для ключа 
    `state` (по умолчанию `'EXECUTED'`):
    ```
    # Выход функции со статусом по умолчанию 'EXECUTED'
    [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
    
    # Выход функции, если вторым аргументов передано 'CANCELED'
    [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
    ```
    - Функция `sort_by_date`:
   ``` 
    # Выход функции (сортировка по убыванию, т. е. сначала самые последние операции)
    [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
   ```

## Документация:

*Раздел находится в разработке.*

## Лицензия:

*Раздел находится в разработке.*
