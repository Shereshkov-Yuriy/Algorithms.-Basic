'''
Определить, какое число в массиве встречается чаще всего.
'''

from random import randint
import timeit


def max_num_dict_1(arr):
    dct = {}
    max_num = 0
    key_num = 0

    for v in arr:
        if v in dct:
            dct[v] += 1
        else:
            dct[v] = 1
        if dct[v] > max_num:
            key_num, max_num = v, dct[v]

    return key_num, max_num


# 0.002231129999999998  -20
# 0.021525568999999994  -200
# 0.21662267899999998   -2_000
# 2.069908367           -20_000
# 22.967665379          -200_000


def max_num_dict_2(arr):
    dct = {}
    max_num = 0
    key_num = 0

    for v in arr:
        if v in dct:
            dct[v] += 1
        else:
            dct[v] = 1
    for k, v in dct.items():
        if v > max_num:
            key_num, max_num = k, v

    return key_num, max_num


# 0.004368614999999999  -20
# 0.018921799000000003  -200
# 0.15933808            -2_000
# 1.527295532           -20_000
# 17.38348781           -200_000


def max_num_count_array(arr):
    num_count = 0
    max_count = 0

    for i in range(len(arr)):
        cnt = 0
        for k in arr[i:]:
            if arr[i] == k:
                cnt += 1
        if cnt > max_count:
            max_count = cnt
            num_count = arr[i]

    return num_count, max_count


# 0.008838354999999999  -20
# 0.611428494           -200
# 56.296667408000005    -2_000
# очень долго           -20_000
# очень-очень долго     -200_000

n = 10
l_1, l_2, l_3 = [], [], []
for x in range(1, 4):
    arr = [randint(0, 100) for _ in range(2 * n ** x)]
    l_1.append(timeit.timeit('max_num_dict_1(arr)', number=1_000, globals=globals()))
    l_2.append(timeit.timeit('max_num_dict_2(arr)', number=1_000, globals=globals()))
    l_3.append(timeit.timeit('max_num_count_array(arr)', number=1_000, globals=globals()))
print(l_1, l_2, l_3, sep='\n')

'''
Уменьшение числа проверок в первоначальном алгоритме не изменяет квадратичную сложность алгоритма.
Использование словаря как хранилища чисел и их повторений позволяет от квадратичной сложности перейти
к линейной сложности алгоритма. В 1-ом варианте задача решается за один проход списка. Во 2-ом случае -
во время первого прохода создается словарь, где ключ - это число, значение - это количество вхождений
данного числа в массив, а во время второго - происходит проверка по первому наибольшему значению. 
Несмотря на одинаковую асимптотику, 2-ой вариант работает чуть быстрее.
'''
