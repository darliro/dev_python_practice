# import pytest
# import random


# 1 задача. Написать функцию по нахождению первого числа от 1 до n, которое будет делиться на b, но НЕ будет
# делиться на c. После написания попросили написать сразу тесты, которые бы проверили этот функционал. Тут проверяют
# подход к написанию, как мыслишь, насколько ты хорош в тест дизайне. Задача "разминочная", но по ходу ее решения
# добавлялись условия, чтоб ты переделал код под нужный кейс (а давай сделаем так, чтоб было первое число,
# которое делится и на c и на d, а пропиши инпуты)


# def divisible_condition(n, b, c):
#     for num in range(n + 1):
#         if not num % b and num % c:
#             return num
#
#
# print(divisible_condition(10, 3, 2))


# 2 задача. Напишите программу, которая выводит на экран числа из входного параметра. Каждый вывод на новой строке.
# Вместо чисел, кратных трем, программа должна выводить слово «Fizz», а вместо чисел, кратных пяти — слово «Buzz».
# Если число кратно и 3, и 5, то программа должна выводить слово «FizzBuzz»

# def fizz_buzz_gen(n):
#     for i in range(1, n + 1):
#         if not i % 15:
#             yield "FizzBuzz"
#         elif not i % 3:
#             yield "Fizz"
#         elif not i % 5:
#             yield "Buzz"
#         else:
#             yield i
#
#
# for x in fizz_buzz_gen(15):
#     print(x)


# 3 задача. Посчитать однострочником квадраты чисел от 0 до 9
# def square_gen(n):
#     for i in range(1, n + 1):
#         yield i ** 2
#
#
# for x in square_gen(10):
#     print(x)

# def func_square(n):
#     return [i ** 2 for i in range(1, n + 1)]
#
#
# print(func_square(10))


# 4 задача. Найти уникальные слова в строке, метод должен возвращать массив с уникальными слова
# from typing import List
#
#
# def unique_words(arr: List[str]) -> List[str]:
#     return list(set(arr))
#

# print(unique_words['away', 'way', 'tray', 'stay', 'gray', 'way', 'stay'])

# def unique_words_list(arr):
#     unique = []
#
#     for word in arr:
#         if word not in unique:
#             unique.append(word)
#     return unique
#
#
# print(unique_words(['away', 'way', 'tray', 'stay', 'gray', 'way', 'stay']))

# def unique_words_dict(arr):
#     unique = {}
#
#     for word in arr:
#         unique[word] = None
#     return list(unique.keys())
#
#
# print(unique_words_dict(['away', 'way', 'tray', 'stay', 'gray', 'way', 'stay']))


# 5 задача. Дано слово, разделитель и количество. Вернуть строку с количеством слов через разделитель
# def wrapper(n: str, s: str, q: int):
#     print((n + s) * (q - 1) + n, end='')
#
#
# wrapper('la', '-', 5)


# 6 задача. Написать "hello world" через разделитель
# print('-'.join("hello how are you".split()))
# print(* "hello how are you".split(), sep='-')


# Простая функция сложения:
# def calc_sum(a, b):
#     return a + b
#
# def test_calc_sum():
#     # Arrange
#     a = 3
#     b = 5
#     expected_result = 8
#
#     # Act
#     result = calc_sum(a, b)
#
#     # Assert
#     assert result == expected_result, f"Expected {expected_result}, but got {result}"
#
# def main():
#     a = int(input('Введите число a: '))
#     b = int(input('Введите число b: '))
#     print('Сейчас я сложу ваши числа!')
#     result = calc_sum(a, b)
#     print(f'{a} + {b} = {result}')
#
# if __name__ == "__main__":
#     test_calc_sum()  # Вызов теста перед основной логикой
#     main()


# def test_addition(a, b):
#     result = a + b
#     print(f'{a} + {b} = {result}')
#     assert result == a + b, "Результат сложения некорректен"
#
#
# test_addition(1, 2)


# def get_number():
#     return 1
#
#
# def test_addition_1(c, d):
#     result1 = c + d
#     print(f'{c} + {d} = {c + d}')
#     assert result1 == c + d, "Результат сложения некорректен"


# @pytest.fixture
# def first_number():
#     print('Начало работы фикстуры...')
#     yield 1
#     print('Завершение работы фикстуры...')
#
#
# def test_addition_2(first_number):
#     s = 2
#     result2 = first_number + s
#     print(f'{first_number} + {s} = {result2}')
#     assert result2 == first_number + s, "Результат сложения некорректен"


# РЕАЛИЗАЦИЯ ПРОСТОГО АВТОТЕСТА ЧЕРЕЗ ФИКСТУРЫ
# @pytest.fixture(scope="session")  # для scope="function" значение перегенерится
# def random_number():
#     r = random.randint(1, 100)
#     return r
#
#
# def test_addition_random(random_number):
#     s = 2
#     res = random_number + s  # примет значение из первого рандома
#     print(f'{random_number} + {s} = {res}')
#     assert res == random_number + 1, "Результат сложения некорректен"
#
#
# def test_addition_random_2(random_number):
#     s = 2
#     res = random_number + s  # также примет значение из первого рандома
#     print(f'{random_number} + {s} = {res}')
#     assert res == random_number + 1, "Результат сложения некорректен"


# class Point:
#     "Класс для определения точек"
#     color = 'red'
#     circle = 2


# class NewMap:
#     "Класс для определения типа карты"
#     material = ['paper', 'digital']
#     volume = ['2D', '3D']
#
#     def __init__(self, a, b):
#         self.x = a
#         self.y = b
#
#     def __del__(self):
#
#     def set_coords(self, x, y):
#         self.x = x
#         self.y = y
#
#     def get_coords(self):
#         return (self.x, self.y)
#
#
# TrainingDemo = NewMap(1, 2)