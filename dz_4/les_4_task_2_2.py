'''
Алгоритм поиска i-го по счету простого числа.
Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритма.
Решето Эратосфена
'''
import cProfile
import timeit


def sieve(n):
    arr = [i for i in range(n * 100)]
    arr[1] = 0
    len_ = len(arr)
    p = 2
    while p ** 2 < len_:
        if arr[p] != 0:
            j = p ** 2
            while j < len_:
                arr[j] = 0
                j += p
        p += 1

    arr = [i for i in arr if i != 0]
    return arr[n - 1]


print(sieve(10000))

print(timeit.timeit('sieve(10)', number=1_000, globals=globals()))  # 0.15662653599999998
print(timeit.timeit('sieve(100)', number=1_000, globals=globals()))  # 1.4914242940000002
print(timeit.timeit('sieve(1000)', number=1_000, globals=globals()))  # 20.772568545000002

cProfile.run('sieve(10000)')

'''
         7 function calls in 0.261 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.004    0.004    0.261    0.261 <string>:1(<module>)
        1    0.195    0.195    0.257    0.257 les_4_task_2_2.py:11(sieve)
        1    0.041    0.041    0.041    0.041 les_4_task_2_2.py:12(<listcomp>)
        1    0.021    0.021    0.021    0.021 les_4_task_2_2.py:24(<listcomp>)
        1    0.000    0.000    0.261    0.261 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

'''
