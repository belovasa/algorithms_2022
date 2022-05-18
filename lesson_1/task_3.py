"""
Задание 3.
Для этой задачи
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
3) оцените итоговую сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему
Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""


def check_1(in_dict):
    """
    Функция поискa трех компаний с наибольшей годовой прибылью..
    Алгоритм 1:
    Сложность #O(nlogn)
    """
    in_dict = sorted(in_dict, key=in_dict.get, reverse=True)  # O(nlogn)
    return in_dict[0:3]  # О(n):


def check_2(in_dict):
    """
       Функция поискa трех компаний с наибольшей годовой прибылью..
       Алгоритм 2:
       Сложность #O(n^2)
       """
    list_value = list(in_dict.values())  # O(n)
    list_value.sort(reverse=True)  # O(nlogn)
    new_dict = {}  # O(1)
    for i in list_value[0:3]:  # O(n)+O(n)
        for k, v in in_dict.items():  # O(n)
            if v == i:  # O(n)+ O(1)
                new_dict[k] = v  # O(1)
    return new_dict  # О(n):


my_dict = {'One': 20, 'Two': 82, 'Three': 80, 'Four': 34, 'Five': 46}
print(check_1(my_dict))
print(check_2(my_dict))
