'''
 Посчитать четные и нечетные цифры введенного натурального числа.
 Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
'''


def apart(a, even=0, uneven=0):
    if a % 10 % 2:
        uneven += 1
    else:
        even += 1
    if a // 10:
        return apart(a // 10, even, uneven)
    return even, uneven


a = int(input('Введи натуральное число: '))
even, uneven = apart(a)
print(f'Четных чисел {even}, нечетных - {uneven}')
