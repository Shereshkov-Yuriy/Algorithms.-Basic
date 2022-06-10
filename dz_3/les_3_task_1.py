'''
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
'''

a = [i for i in range(2, 100)]
b = [i for i in range(2, 10)]
c = [0] * len(b)

for i, v in enumerate(b):
    for j in a:
        if j % v == 0:
            c[i] += 1

print(f'От {a[0]} до {a[-1]}:')

for i in range(len(b)):
    print(f'Числу {b[i]} кратно {c[i]} чисел', sep='\n')
