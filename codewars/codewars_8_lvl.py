"""ЗАДАЧИ С CODEWARS ПО УРОВНЯМ"""

# === 8-EASY ===

# def solution(string):
#     return string[::-1]  # функция на переворот строки

# def number_to_string(n):
#     return str(n)  # функция на конвертацию числа в строку

# def remove_char(s):
#     return s[1:-1]  # функция на отсечение первой и последней букв

# def no_space(x):
#     return x.replace(' ', '')  # функция на вычленение пробелов

# def abbrevName(name):
#     first, last = name.title().split(' ')
#     return first[0] + '.' + last[0]  # функция на объединение инициалов

# def greet(name):
#     return f"Hello, {name} how are you doing today?"  # функция на вывод приветствия

# def century(year):
#     return (year + 99) // 100  # функция по переводу годов в век

# def digitize(n):
#     return map(int, str(n)[::-1])  #  функция по преобразованию числа в массив наоборот

# def is_divisible(n, x, y):
#     return n % x == n % y == 0 # функция по проверке на делимость

# def sum_array(a):
#     return sum(a)  # функция по суммированию элементов коллекции

# def invert(lst):
#     return [-x for x in lst]  # функция по преобразованию элементов в негативные

# def positive_sum(arr):
#     return sum(x for x in arr if x > 0)  # функция по возвращению суммы позитивных чисел

# def square_sum(numbers):
#     return sum(num ** 2 for num in numbers)  # функция по возвращению суммы квадратов чисел

# def maps(a):
#     return [2 * x for x in a]  # функция по возвращению умноженного вдвое элемента коллекции

# def find_average(numbers):
#     return sum(numbers) / len(numbers) if numbers else 0  # функция на поиск среднего арифметического

# def digitize(number):
#     return [int(num) for num in str(number)[::-1]]  # функция на конвертацию числа в перевёрнутый список

# def count_sheep(sheep):
#     return sheep.count(True)  # функция на подсчёт овец

# def love_flowers(flower1, flower2):
#     return (flower1 + flower2) % 2  # функция на подсчёт лепестков для чётного и нечётного кол-ва на цветках

# def find_needle(haystack):
#     return f"found the needle at position {haystack.index('needle')}"  # функция на поиск иголки в стоге сена

# def better_than_average(class_points, your_points):
#     return your_points > sum(class_points) / len(class_points)  # функция по сравнению оценок с одноклассниками
