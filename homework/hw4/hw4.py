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


def transpose(matrix):
    transposed = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]
    for i in range (len(matrix)):
        for j in range(len(matrix[0])):
            transposed[j][i] = matrix[i][j]
    return transposed


def function(**kwargs):
    return {v if v.__hash__ is not None else str(v): k for k, v in kwargs.items()}


menu = ("Что вы хотите?\n"
        "1. Пополнить счёт\n"
        "2. Произвести снятие\n"
        "3. Выйти из меню\n"
        "Введите номер: ")

wealth_threshold = dec(5000000)
wealth_tax = dec(10)/dec(100)
withdrawal_fee = dec(15)/dec(1000)
balance = 0


while True:
    print(menu)
    choice = int(input())
    match choice:
        case 1:
            if balance >
        case 2:
            print(2)
        case 3:
            print(f"Остаток на Вашей карте {account} у.е. Спасибо за визит!")
            break
        case _:
            print("Некорректный ввод")



