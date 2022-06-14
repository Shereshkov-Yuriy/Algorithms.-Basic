"""
Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел. При этом каждое число
представляется как коллекция, элементы которой — цифры числа. Например, пользователь ввёл A2 и C4F.
Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

from collections import deque


def addition_col(num_1, num_2):
    sum_num = deque()  # Для записи результата вычисления
    high_digit = 0  # Для увеличения старшего разряда на единицу
    len_1 = len(num_1)  # Количество цифр в первом числе больше по умолчанию
    len_2 = len(num_2)

    if len_2 > len_1:
        num_1, num_2 = num_2, num_1
        len_1, len_2 = len_2, len_1

    for _ in range(len_1 - len_2):
        num_2.appendleft(ZERO)

    for _ in range(len_1):
        n_1 = num_1.pop()
        n_2 = num_2.pop()
        sum_digits = HEX_TUPLE.index(n_1) + HEX_TUPLE.index(n_2) + high_digit
        high_digit = 0
        if sum_digits > 15:
            sum_digits -= 16
            high_digit = 1
        sum_num.appendleft(HEX_TUPLE[sum_digits])
        if not num_1 and high_digit:
            sum_num.appendleft('1')

    return sum_num


HEX_TUPLE = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F')
ZERO = '0'
num_1 = deque(input('Введи первое положительное целое шестнадцатеричное число: ').upper())
num_2 = deque(input('Введи второе положительное целое шестнадцатеричное число: ').upper())
print(*num_1, '\n+\n', *num_2, '\n=\n', *addition_col(num_1, num_2), sep='')
