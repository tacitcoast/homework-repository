# Запишите функцию, которая считывает входные данные построчно и находит максимальное и минимальное значения.
# Функция должна возвращать кортеж с максимальным и минимальным значениями.
# Например, для [1, 2, 3, 4, 5] функция должна возвращать [1, 5]
# Мы гарантируем, что этот файл существует и содержит целые числа, разделенные строками.


from typing import Tuple


my_list = []


def find_maximum_and_minimum(file) -> Tuple[int, int]:
    max_num = 0
    min_num = 0

    for num in file:
        if int(num) > max_num:
            max_num = int(num)
        if min_num == 0:
            min_num = int(num)
        elif int(num) < min_num:
            min_num = int(num)

    return [min_num, max_num]


# with open('some_file.txt') as file:
#     print(find_maximum_and_minimum(file))
