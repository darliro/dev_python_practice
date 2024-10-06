"""ЗАДАЧИ С CODEWARS ПО УРОВНЯМ"""

# === 7-EASY ===

# def get_count(sentence):
#     return sum(1 for char in sentence if char in "aeiouAEIOU")  # функция на нахождение гласных

# def remove_vowels(sentence):
#     return ''.join([char for char in sentence if char not in 'aeiouAEIOU'])  # функция на вычленение гласных

# def square_digits(nums):
#     return int(''.join(str(int(num) ** 2) for num in str(nums)))  # функция на конкатенацию квадратов чисел

# def high_and_low(numbers):
#     return f"{max(list(map(int, numbers.split())))} {min(list(map(int, numbers.split())))}"  # функция на вывод
# максимального и минимального числа из строки с пробелами

# def descending_order(num):
#     return int(''.join(sorted(str(num), reverse=True)))  # функция на вывод отсортированной числовой
# последовательности

# def get_middle(s):
#     while len(s) > 2:
#         s = s[1:-1]
#     return s  # функция на вывод средней буквы или двух (чёт или нечёт)

# def filter_list(l):
#     return [num for num in l if type(num) is int]  # функция на вывод только чисел в списке

# def accum(sentence):
#     return '-'.join(sym.upper() + sym.lower() * char for char, sym in enumerate(sentence))  # функция на
# # возвращение определённого паттерна фразы

# def is_square(log):
#     return log > 0 and (log ** 0.5) % 1 == 0  # функция на проверку на логарифм

# def is_isogram(string):
#     return len(string) == len(set(string.lower()))  # функция на проверку на изограмму

# def xo(s):
#     return s.lower().count('x') == s.lower().count('o')  # функция на поиск равного вхождения 'x' и 'o'

# def find_short(s):
#     return min(len(word) for word in s.split())  # функция на поиск длины минимального слова

# def dna_strand(dna):
#     base = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
#     return ''.join([base[char] for char in dna])  # функция на дополнение ДНК-оснований
