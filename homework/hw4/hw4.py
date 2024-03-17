'''
1. Напишите функцию для транспонирования матрицы
2. Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение переданного аргумента, а значение — имя аргумента.
Если ключ не хешируем, используйте его строковое представление.
3. Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции. Дополнительно сохраняйте все операции поступления и снятия средств в список.
'''


def transpose(matrix):
    transposed = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]
    for i in range (len(matrix)):
        for j in range(len(matrix[0])):
            transposed[j][i] = matrix[i][j]
    return transposed


def function(**kwargs):
    return {v if v.__hash__ is not None else str(v): k for k, v in kwargs.items()}


