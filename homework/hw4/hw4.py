'''
1. Напишите функцию для транспонирования матрицы
2. Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение переданного аргумента, а значение — имя аргумента.
Если ключ не хешируем, используйте его строковое представление.
3. Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции. Дополнительно сохраняйте все операции поступления и снятия средств в список.

Начальная сумма = 0
Действия: пополнить, снять, выйти
Суммы пополнения и снятия кратны 50 у.е.
Процент за снятие - 1,5% от суммы, но не менее 30 и не более 600 у.е.
После каждой третьей операции пополнения или снятия начисляются проценты - 3%
Нельзя снять больше, чем есть на счёте
При превышении суммы в 5 млн вычитать налог на богатство ПЕРЕД каждой операцией, даже ошибочной
Любое действие выводит сумму денег

'''

from decimal import Decimal as dec
import time


def transpose(matrix):
    transposed = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]
    for i in range (len(matrix)):
        for j in range(len(matrix[0])):
            transposed[j][i] = matrix[i][j]
    return transposed


matrix = [[1, 2, 3], [4, 5, 6]]
transp_matrix = transpose(matrix)
print (matrix)
print (transp_matrix)


def function(**kwargs):
    return {v if v.__hash__ is not None else str(v): k for k, v in kwargs.items()}


def wealth_check(bal, tax):
    reduction = bal * tax
    if bal > wealth_threshold:
        bal -= reduction
        print(f'Удержан налог на богатство {tax*100}% в размере {reduction} у.е.\n'
              f'Остаток на Вашей карте {bal}')
    return bal


def mult_check(amount, multiplier):
    if amount % multiplier != 0:
        print(f'Ошибка! Введена сумма, не кратная {multiplier}. Операция отменена.')
        return 0
    return amount


menu = ("Что вы хотите?\n"
        "1. Пополнить счёт\n"
        "2. Произвести снятие\n"
        "3. Вывести историю операций\n"
        "4. Выйти из меню\n"
        "Введите номер: ")

wealth_threshold = dec(5000000)
wealth_tax = dec(10)/dec(100)
withdrawal_fee = dec(15)/dec(1000)
min_wit_tax = 30
max_wit_tax = 600
multiplier = dec(50)
balance = 0
operation_count = 1
op_count_mult = 3
interest = dec(3)/dec(100)
operations_dict = dict()

while True:
    time.sleep(0.5)
    print(menu)
    choice = int(input())
    if operation_count % op_count_mult == 0:
        balance *= (1 + interest)
    match choice:
        case 1:
            balance = wealth_check(balance, wealth_tax)
            topup_amount = int(input('Введите сумму пополнения: '))
            balance += mult_check(topup_amount, multiplier)
            print(f'Завершено. Текущий баланс карты {balance} у.е.')
            operations_dict[f'{operation_count} - пополнение'] = topup_amount
            operation_count += 1
        case 2:
            balance = wealth_check(balance, wealth_tax)
            print(f'Обратите внимание на взимание комиссии за снятие денежных средств в размере {withdrawal_fee*100}%.')
            withdraw_amount = int(input('Введите сумму снятия: '))
            withdraw_tax = withdraw_amount * withdrawal_fee
            withdraw_tax = min_wit_tax if withdraw_tax < min_wit_tax else max_wit_tax if withdraw_tax > max_wit_tax else withdraw_tax
            multiplier_check = mult_check(withdraw_amount, multiplier)
            total_withdraw = multiplier_check + withdraw_tax * (1 if multiplier_check > 0 else 0)
            if total_withdraw == 0:
                print(f'Снятие средств отменено. Текущий баланс карты {balance} у.е.')
            elif balance - total_withdraw >= 0 and total_withdraw > 0:
                balance -= total_withdraw
                print(f'Снятие успешно. Текущий баланс карты {balance} у.е.')
                operations_dict[f'{operation_count} - снятие'] = total_withdraw
                operation_count += 1
            else:
                print(f'Ошибка! Недостаточно средств на карте. Доступный баланс карты {balance} у.е.')
        case 3:
            for k, v in operations_dict.items():
                print(f'{k}: {v}')
        case 4:
            print(f'Остаток на Вашей карте {balance} у.е. Спасибо за визит!')
            break
        case _:
            print('Некорректный ввод')



