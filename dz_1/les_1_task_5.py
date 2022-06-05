'''
Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
'''

print('Введите две буквы от "a" до "z"')
a_char = ord(input('Введите первую букву: '))
b_char = ord(input('Введите вторую букву: '))
pos_a = a_char - ord('a') + 1
pos_b = b_char - ord('a') + 1

if pos_a == pos_b:
    size_a_b = pos_a - pos_b
elif pos_a > pos_b:
    size_a_b = pos_a - pos_b - 1
else:
    size_a_b = pos_b - pos_a - 1

print(f'Буква {chr(a_char)} стоит на месте {pos_a}')
print(f'Буква {chr(b_char)} стоит на месте {pos_b}')
print(f'Между ними букв: {size_a_b}')
