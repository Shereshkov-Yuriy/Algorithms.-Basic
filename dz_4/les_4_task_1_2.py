'''
Определить, какое число в массиве встречается чаще всего.
'''

from random import randint
import timeit
import cProfile


def max_num_count_array(arr):
    num_count = None
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


n = 10
for x in range(1, 4):
    arr = [randint(0, 100) for _ in range(2 * n ** x)]
    print(timeit.timeit('max_num_count_array(arr)', number=1_000, globals=globals()))

# 0.008928951999999997
# 0.60377843
# 55.789364218
# по прежнему долго
# алгоритм имеет квадратичную сложность

arr = [randint(0, 100) for _ in range(20_000)]
cProfile.run('max_num_count_array(arr)')

'''
         5 function calls in 5.721 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    5.721    5.721 <string>:1(<module>)
        1    5.721    5.721    5.721    5.721 les_4_task_1_2.py:10(max_num_count_array)
        1    0.000    0.000    5.721    5.721 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

'''
'''
Возможности кода по прежнему ограничены. Цикл в цикле увеличивает сложность алгоритма.
'''
