'''
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
'''

from random import randint

a = [randint(0, 100) for _ in range(20)]
min_a = a[0]
max_a = a[0]
idx_min = 0
idx_max = 0

print(f'Список до: ', a, sep='\n')

for i in range(len(a)):
    if a[i] < min_a:
        min_a = a[i]
        idx_min = i
    elif a[i] > max_a:
        max_a = a[i]
        idx_max = i

tmp = a[idx_min]
a[idx_min] = a[idx_max]
a[idx_max] = tmp

print(f'Список после: ', a, sep='\n')
print(f'{min_a=}\n{max_a=}')
