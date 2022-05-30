'''
Определить, какое число в массиве встречается чаще всего.
'''

from random import randint
import timeit
import cProfile


def max_num_count_array(N):
    a = [randint(0, 100) for _ in range(N)]
    num_count = None
    max_count = 0

    for i in range(len(a)):
        cnt = 0
        for k in a:
            if a[i] == k:
                cnt += 1
        if cnt > max_count:
            max_count = cnt
            num_count = a[i]

    # print(f'Список: ', a, sep='\n')
    return num_count, max_count


# num_count, max_count = max_num_count_array()
# print(f'{num_count=}\n{max_count=}')
print(timeit.timeit('max_num_count_array(20)', number=1_000, globals=globals()))  # 0.037660187
print(timeit.timeit('max_num_count_array(200)', number=1_000, globals=globals()))  # 1.2169243939999999
print(timeit.timeit('max_num_count_array(2_000)', number=1_000, globals=globals()))  # 108.04022045900001
print(timeit.timeit('max_num_count_array(20_000)', number=1_000, globals=globals()))  # долго

cProfile.run('max_num_count_array(20_000)')

'''
         105230 function calls in 11.298 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000   11.298   11.298 <string>:1(<module>)
        1   11.262   11.262   11.298   11.298 les_4_task_1_1.py:10(max_num_count_array)
        1    0.005    0.005    0.036    0.036 les_4_task_1_1.py:11(<listcomp>)
    20000    0.009    0.000    0.013    0.000 random.py:238(_randbelow_with_getrandbits)
    20000    0.012    0.000    0.025    0.000 random.py:291(randrange)
    20000    0.006    0.000    0.031    0.000 random.py:335(randint)
        1    0.000    0.000   11.298   11.298 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
    20000    0.002    0.000    0.002    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    25224    0.002    0.000    0.002    0.000 {method 'getrandbits' of '_random.Random' objects}
'''
'''
Частый вызов random. Проверенные числа повторно проверяются. Вынесу создание массива за пределы функции, 
уменьшу число операций, исключая уже проверенные числа в массиве. 
'''
