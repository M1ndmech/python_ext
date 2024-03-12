'''
1. Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. Функцию hex используйте для проверки своего результата.
2. Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions 
'''

def to_hex(num):
    hex_digits = "0123456789abcdef"
    hex_str = ""
    while num > 0:
        hex_str = hex_digits[num % 16] + hex_str
        num = num // 16
    return hex_str

def fractions_sum_prod(frac1, frac2):
    num1, den1 = map(int, frac1.split("/"))
    num2, den2 = map(int, frac2.split("/"))

    sum_num = num1 * den2 + num2 * den1
    sum_den = den1 * den2
    sum_frac = (sum_num, sum_den)

    prod_num = num1 * num2
    prod_den = den1 * den2
    prod_frac = (prod_num, prod_den)

    return sum_frac, prod_frac

print("Что вы хотите?\n"
      "1. Преобразовать число в шестнадцатеричное'\n"
      "2. Произвести действия с дробями\n"
      "Введите номер: ")

choice = int(input())

match choice:
    case 1:
        num1 = int(input("Введите число для преобразования в шестнадцатеричный формат: "))
        hex1 = to_hex(num1)
        print(f"Шестнадцатеричное представление числа {num1} - {hex1}")
    case 2:
        frac1 = input("Введите первую дробь в формате n/m: ")
        frac2 = input("Введите вторую дробь в формате n/m: ")
        sum_frac, prod_frac = fractions_sum_prod(frac1, frac2)
        print(f"Сумма дробей {frac1} и {frac2} - {sum_frac[0]}/{sum_frac[1]}")
        print(f"Произведение дробей {frac1} и {frac2} - {prod_frac[0]}/{prod_frac[1]}")    
    case _:
        print("Некорректный ввод")