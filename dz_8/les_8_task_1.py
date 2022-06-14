"""
Определение количества различных подстрок с использованием хеш-функции.
Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
Примечание: в сумму не включаем пустую строку и строку целиком.
"""
import hashlib


def count_substring(text) -> int:
    length = len(text)
    hash_set = set()

    for i in range(length):
        for j in range(i + 1, length + 1):
            if i == j - length:
                continue
            else:
                hash_set.add(hashlib.sha1(text[i:j].encode()).hexdigest())

    return len(hash_set)


print(count_substring('papa'))  # 6
print(count_substring('sova'))  # 9
