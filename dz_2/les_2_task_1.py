'''
Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
Числа и знак операции вводятся пользователем.
После выполнения вычисления программа не завершается, а запрашивает новые данные для вычислений.
Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
программа должна сообщать об ошибке и снова запрашивать знак операции.
Также она должна сообщать пользователю о невозможности деления на ноль, если он ввел его в качестве делителя.
'''


def calc(a, b, z):
    if z == '+':
        return a + b
    elif z == '-':
        return a - b
    elif z == '*':
        return a * b
    elif b == 0:
        return 'На ноль делить нельзя!'
    return a / b


print('Введи два числа, знак действия "/, *. -, +" или 0 вместо знака, чтобы выйти')
is_end = True
while is_end:
    a = int(input('Введи первое число: '))
    b = int(input('Введи второе число: '))
    z = input('Введи знак: ')
    if z == '0':
        is_end = False
    elif z == '/' or z == '*' or z == '-' or z == '+':
        res = calc(a, b, z)
        print(f'Ответ: {res}')
    else:
        print('Ошибка. Неверная операция. Начните заново.')
print('Пока-пока...')
