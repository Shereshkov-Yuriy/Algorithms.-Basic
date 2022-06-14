"""
Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
"""
from random import randint

m = int(input('Введи натуральное число: '))
f_m = 2 * m + 1
data = [randint(0, 100) for _ in range(f_m)]
print(data)


def gnome_sort(array):
    len_arr = len(array)
    i = 1
    j = 2
    while i < len_arr:
        if array[i - 1] < array[i]:
            i = j
            j += 1
        else:
            array[i - 1], array[i] = array[i], array[i - 1]
            i = i - 1
            if i == 0:
                i = j
                j += 1
    return array


print(gnome_sort(data))
print(data[m])
