'''
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
'''

from random import randint

N = 20
MIN_SIZE = -10
MAX_SIZE = 10
a = [randint(MIN_SIZE, MAX_SIZE) for _ in range(N)]
max_a = None
idx_a = None

for i in range(len(a)):
    if a[i] < 0:
        max_a = a[i]
        idx_a = i
        break

for i, v in enumerate(a):
    if 0 > v > max_a:
        max_a = v
        idx_a = i

print(a)
print(f'Максимальное отрицательное число {max_a} находится на позиции {idx_a + 1}')
