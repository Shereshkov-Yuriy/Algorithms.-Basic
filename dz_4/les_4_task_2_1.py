'''Решето Эратосфена'''
import timeit


def sieve(a):
    m = 2
    while m < len(a):
        if a[m] != 0:
            j = m * 2
            while j < len(a):
                a[j] = 0
                j = j + m
        m = m + 1
    return a


N = 100
a = [i for i in range(N)]
a[1] = 0

a = sieve(a)

for i in a:
    if a[i]:
        print(a[i], end=' ')

print()
print('*' * 20)
print(timeit.timeit('sieve(a)', number=1_000, globals=globals()))

# 0.024140697999999988
