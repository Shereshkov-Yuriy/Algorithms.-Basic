'''
Определить, какое число в массиве встречается чаще всего.
'''

from random import randint

N = 20  # От 20000 элементов уже заметна нагрузка
MIN_SIZE = 0
MAX_SIZE = 100
a = [randint(MIN_SIZE, MAX_SIZE) for _ in range(N)]
number = None
max_count = 0

for i in range(len(a)):  # Количество итераций N ** 2.
    cnt = 0
    for k in a:  # Можно уменьшить число операций, исключая уже проверенные, если взять срез a[i:]
        if a[i] == k:
            cnt += 1
    if cnt > max_count:
        max_count = cnt
        number = a[i]

print(f'Список: ', a, sep='\n')
print(f'{number=}\n{max_count=}')
