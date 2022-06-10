"""
Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
"""
from random import uniform

N, M = 49, 10
data = [round(uniform(0, N), 3) for _ in range(M)]
print(data)


def merge_sort(array):
    len_array = len(array)
    a = 0
    if len_array < 2:
        return array
    elif len_array == 2:
        if array[a] > array[a + 1]:
            array[a], array[a + 1] = array[a + 1], array[a]
        return array

    mid = len_array // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    len_left = len(left)
    len_right = len(right)
    i = j = 0

    while len_left > i and len_right > j:
        if left[i] < right[j]:
            array[i + j] = left[i]
            i += 1
        else:
            array[i + j] = right[j]
            j += 1

    while len_left > i:
        array[i + j] = left[i]
        i += 1

    while len_right > j:
        array[i + j] = right[j]
        j += 1

    return array


print(merge_sort(data))
