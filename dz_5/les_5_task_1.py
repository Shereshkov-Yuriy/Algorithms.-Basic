"""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого
предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования
предприятий, чья прибыль выше среднего и ниже среднего.
"""

from collections import namedtuple

Company = namedtuple('Company', 'profit_1_q profit_2_q profit_3_q profit_4_q profit_year')
companies = {}
total_profit = 0
p = int(input('Введи количество предприятий: '))

for i in range(1, p + 1):
    name = input(f'Введи наименование {i} предприятия: ')
    profit_1_q = float(input('Введи прибыль за 1 квартал: '))
    profit_2_q = float(input('Введи прибыль за 2 квартал: '))
    profit_3_q = float(input('Введи прибыль за 3 квартал: '))
    profit_4_q = float(input('Введи прибыль за 4 квартал: '))
    profit_year = profit_1_q + profit_2_q + profit_3_q + profit_4_q
    total_profit += profit_year
    companies[name] = Company(profit_1_q, profit_2_q, profit_3_q, profit_4_q, profit_year)

# print(companies)

avg_profit = total_profit / p
print(f'\nПредприятия с прибылью выше средней {avg_profit}: ')

for name, profit in companies.items():
    if profit.profit_year >= avg_profit:
        print(name)

print(f'\nПредприятия с прибылью ниже средней {avg_profit}: ')

for name, profit in companies.items():
    if profit.profit_year < avg_profit:
        print(name)
