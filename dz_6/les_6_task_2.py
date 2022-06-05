'''List'''

import sys


def size(data):
    size_data = sys.getsizeof(data)
    size_key = 0
    size_value = 0
    size_item = 0
    if hasattr(data, '__iter__'):
        if hasattr(data, 'items'):
            for key, value in data.items():
                size_key += size(key)
                size_value += size(value)
            return size_key + size_value + size_data
        elif not isinstance(data, str):
            for item in data:
                size_item += size(item)
            return size_item + size_data
    return size_data


a = [i for i in range(2, 10_000)]
b = [i for i in range(2, 10)]
c = [0] * len(b)

for i, v in enumerate(b):
    for j in a:
        if j % v == 0:
            c[i] += 1

memory_cost = size(a) + size(b) + size(c) + size(i) + size(j) + size(v)

print(f'Суммарные затраты на хранение в памяти: {memory_cost} байт')  # 365892 байт
