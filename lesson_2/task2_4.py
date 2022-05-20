"""
Задание 4.	Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75
Решите через рекурсию. В задании нельзя применять циклы.
Нужно обойтисть без создания массива!
"""


def sum_elements(i, n, num, result):
    if i == n:
        return print(f'Количество элементов - {n}, их сумма - {result}')
    else:
        return sum_elements(i + 1, n, (num / 2 * -1), result + num)
    return 0


col_elem = int(input("Введите количество элементов:\n"))
sum_elements(0, col_elem, 1, 0)
