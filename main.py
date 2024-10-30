import os

from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date, filter_by_search_line
from src.transactions import read_transactions_csv, read_transactions_xlsx
from src.utils import read_file_transactions
from src.widget import get_date, mask_account_card

path_to_json = os.path.join(os.path.dirname(__file__), 'data', 'operations.json')
path_to_csv = os.path.join(os.path.dirname(__file__), 'data', 'transactions', 'transactions.csv')
path_to_xlsx = os.path.join(os.path.dirname(__file__), 'data', 'transactions', 'transactions_excel.xlsx')

def user_greeting():
    """ Функция приветствия и выбора формата файла с транзакциями """

    greeting = input('''
Привет! Добро пожаловать в программу работы с банковскими транзакциями. 
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла

Введите цифру: 
    ''')
    return greeting

def get_transaction_list(user_choice):
    """ Получение списка словарей с транзакциями, согласно выбора пользователя """

    if user_choice == '1':
        print('Для обработки выбран JSON-файл.')
        return read_file_transactions(path_to_json)
    elif user_choice == '2':
        print('Для обработки выбран CSV-файл.')
        return read_transactions_csv(path_to_csv)
    elif user_choice == '3':
        print('Для обработки выбран XLSX-файл.')
        return read_transactions_xlsx(path_to_xlsx)
    else:
        print('Введены некорректные данные, попробуйте ещё раз!')
        return []


def user_choice_state(transactions_list):
    """ Фильтрация списка транзакций по статусу, который выбирает пользователь"""

    state_list = ['EXECUTED', 'CANCELED', 'PENDING']
    user_state = input('''
    Введите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING: 
''')

    while user_state.upper() not in state_list:
        print(f'Статус операции "{user_state}" недоступен.')
        user_state = input('''
        Введите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING.
''')

    print(f'Операции отфильтрованы по статусу "{user_state.upper()}"')
    return filter_by_state(transactions_list, user_state.upper())


def final_filter_transactions(filtered_transactions):
    """ Фильтрация списка транзакций по различным параметрам """
    yes_no = ['да', 'нет']
    up_down = ['по возрастанию', 'по убыванию']

    transactions_by_date = []
    user_date = input('Отсортировать операции по дате? Да/Нет: ').lower()
    while user_date not in yes_no:
        print('Введены неверные параметры, попробуйте ещё!')
        user_date = input('Отсортировать операции по дате? Да/Нет: ').lower()
    if user_date == 'да':
        user_dir = input('Отсортировать по возрастанию или по убыванию? ')
        while user_dir not in up_down:
            print('Введены неверные параметры, попробуйте ещё!')
            user_dir = input('Отсортировать по возрастанию или по убыванию? ').lower()
        if user_dir.lower() == 'по возрастанию':
            transactions_by_date = sort_by_date(filtered_transactions, sort_dir=False)
        elif user_dir.lower() == 'по убыванию':
            transactions_by_date = sort_by_date(filtered_transactions)
    elif user_date == 'нет':
        transactions_by_date = filtered_transactions

    transactions_currency = []
    user_currency = input('Выводить только рублевые транзакции? Да/Нет: ').lower()
    while user_currency not in yes_no:
        print('Введены неверные параметры, попробуйте ещё!')
        user_currency = input('Выводить только рублевые транзакции? Да/Нет: ').lower()
    if user_currency == 'да':
        transactions_currency = list(filter_by_currency(transactions_by_date, 'RUB'))
    elif user_currency == 'нет':
        transactions_currency = transactions_by_date

    transactions_final = []
    user_key_word = input('Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ').lower()
    while user_key_word not in yes_no:
        print('Введены неверные параметры, попробуйте ещё!')
        user_key_word = input('Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ').lower()
    if user_key_word == 'да':
        user_word = input('Введите слово: ')
        transactions_final = filter_by_search_line(transactions_currency, user_word)
    elif user_key_word == 'нет':
        transactions_final = transactions_currency

    return transactions_final


def main():
    """ Вывод результирующей информации по транзакциям, согласно запросам пользователя """

    user_choice = user_greeting()
    transactions_list = get_transaction_list(user_choice)
    transactions_state = user_choice_state(transactions_list)
    result_answer = final_filter_transactions(transactions_state)

    print('Распечатываю итоговый список транзакций...')
    if len(result_answer) > 0:
        print(f'Всего банковских операций в выборке: {len(result_answer)}')
        for res in result_answer:
            date = get_date(res.get('date'))
            description = res.get('description')
            operation = ''
            amount = 0
            if 'from' in res:
                operation += mask_account_card(str(res.get('from'))) + ' -> ' + mask_account_card(str(res.get('to')))
            else:
                operation += mask_account_card(res.get('to'))
            if 'amount' in res:
                amount += float(res.get('amount'))
            else:
                amount += float(res.get('operationAmount').get('amount'))
            print(f'''
            {date} {description}
            {operation}
            Сумма: {amount}
            ''')
    else:
        print('Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.')


if __name__ == '__main__':
    main()
