'''
Алгоритм поиска i-го по счету простого числа.
Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритма.
Моя версия.
'''
import cProfile
import timeit


def prime(n):
    arr = [i for i in range(2, n * 100) if i % 2]
    prime_list = [2]

    def p(n, arr):
        i = 1
        while i < n:
            prime_list.append(arr[0])
            arr = [i for i in arr if i % arr[0]]
            i += 1
        return prime_list[-1]

    return p(n, arr)


print(prime(10000))    # 104729

print(timeit.timeit('prime(10)', number=1_000, globals=globals()))  # 0.15567789799999998
print(timeit.timeit('prime(50)', number=1_000, globals=globals()))  # 1.993146749
print(timeit.timeit('prime(100)', number=1_000, globals=globals()))  # 6.612871123
print(timeit.timeit('prime(500)', number=1_000, globals=globals()))  # 128.07371455900002
print(timeit.timeit('prime(1000)', number=1_000, globals=globals()))  # 471.50122874199997

cProfile.run('prime(10000)')

'''
         20004 function calls in 57.046 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.004    0.004   57.046   57.046 <string>:1(<module>)
        1    0.001    0.001   57.042   57.042 les_4_task_2_3.py:11(prime)
        1    0.078    0.078    0.078    0.078 les_4_task_2_3.py:12(<listcomp>)
        1    7.615    7.615   56.963   56.963 les_4_task_2_3.py:14(p)
     9999   49.340    0.005   49.340    0.005 les_4_task_2_3.py:18(<listcomp>)
        1    0.000    0.000   57.046   57.046 {built-in method builtins.exec}
     9999    0.008    0.000    0.008    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

'''
'''
С чего начать? Попробуй list. Не лучший вариант, зато сам придумал.
Классический вариант не вспомнил и не нашел.
'''
