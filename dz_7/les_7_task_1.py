"""
Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на
промежутке [-100; 100).Выведите на экран исходный и отсортированный массивы.
Примечания:
● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
  Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.
"""
from random import randint

N, M = 100, 10
data = [randint(-N, N - 1) for _ in range(M)]
print(data)


def bubble_sort(array, desc=True):
    len_array = len(array)
    for n in range(1, len_array):
        for i in range(len_array - n):
            if not desc and array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
            elif desc and array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
    return array


print(bubble_sort(data))
