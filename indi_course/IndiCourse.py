# # Функция print()
# # По умолчанию выводит значения через пробел. Для указания кастомного разделителя используем аргумент sep=','
# # По умолчанию выводит 1 строку, 1 принт = строка. Для вывода нескольких принтов в строку используем аргумент end=' '
# print('first row', end=' ')
# print('second row')

# Функция input()
# По умолчанию приостанавливает код и ожидает ввода пользователя. Принимает дефолтно str.
# print(input("Enter something...: "))

# Переменная – это контейнер для хранения значения: число, строка и т.д.
# После сохранения значения в переменной можно им пользоваться по коду.
# Можно присваивать сразу несколько значения для переменных в строку, но важно иметь соответствие между кол-вом.
# Можно вывести тип переменной через встроенную функцию type()
# name, age = "Alice", 25
# print(type(name), type(age))

# Конвенция именований:
# snake_case – имена переменных, функций, методов модулей
# snake_case – имена переменных, функций, методов модулей
# camelCase – имена классов
# another-package – имена пакетов
# CONSTANT – констант


# result = 19 + 3.0  # переменная начинает существовать только после присвоения значения
# print(type(result))  # для вывода типа нужно задействовать переменную, не print

# print(10 + 'lala')  # так не сработает из-за строгой типизации (хотя всё ещё динамической)
# print(10, 'lala')  # так сработает из-за вывода двух типов в перечислении

# a = input()  # 123, например
# print(type(a))  # выведется str в типах, потому что ввод пользователя так преобразуется по умолчанию

# a = int(input())
# print(type(a))  # нельзя преобразовать 'str' в 'int', только наоборот: неприводимые типы

# print(f'Perimeter equals {p}!')  # добавляем f для каждого вывода строк в print
# print('Perimeter equals', p, '!')  # альтернативная нотация вывода

# sentence = "Hello, world!"
# words = sentence.split(", ")  # Разделяем строку по запятой с пробелом
# print(words)  # Вывод: ['Hello', 'world!']

# numbers = ["1", "2", "3", "4", "5"]
# numbers = list(map(int, numbers))  # Преобразуем каждый элемент в список в целое число
# print(numbers)  # Вывод: [1, 2, 3, 4, 5]

# a = a % 10 / 1 # вывод последней цифры введённого числа
# a = a % 100 // 10 # вывод разряда десятка введённого числа
# a = a % 1000 // 100 # вывод разряда сотни введённого числа
# a % 2 == 0 # проверка на чётность

# s = 'hello world'
# print(s[-1])  # индекс, вывод последнего символа в строке

# s = 'hello world'
# print(s[0:5])  # срез (также [:5], вывод среза в строке. Левое значение берется, правое нет

# s = 'hello world'
# print(s[::2])  # шаг, вывод с перемещением по строке

# s = 'hello world'
# print(s[::-1])  # шаг для перевёрнутой строки (начинаем с 0 и по 0, отсчитываем с -1)

# s = 'hello world'
# print(s[:4] + 'a' + s[5:])  # вывод строки с заменой символа

# s = 'hello world'
# print(s[-5:-1])  # срез для вывода 5 последних символов отсекает последний из-за его невключения

# s = 'hello world'
# print(s[-5:])  # так срез для вывода 5 последних символов включит последний

# s = 'hello world'
# print(s[1::2])  # так срез с шагом сместится с подсчёта на второй символ

# s = input()
# print(s[::-3])  # так шаг пойдёт справа налево и начнётся с подсчёта последнего символа

# s = input()
# print(s[-1] + s[0:-1])  # так индекс заберёт последний символ и приклеит его к фразе уже без последнего

# print(a[0:3].upper() + a[3:-3].lower() + a[-3:].upper())  # задачка с выводом трёх первых и последних букв заглавными

# s = 'AbrAcAdAbrA'
# s.find('r')  # вернет индекс первого вхождения символа 'r' (2)
# s.rfind('r')  # вернет индекс первого вхождения символа 'r', но поиск начнется с конца слова (9)
# s.find('r', 5, 10)  # вернет индекс 9, поиск начат с символа с индексом 5, но при ненахождении выкинет -1

# b = input()
# c = b.lower()
# d = c.replace('a', '').replace('o', '').replace('y', '').replace('e', '').replace('u', '').replace('i', '')
# e = d.replace('', '.')
# f = e[:-1]
# print(f)  # задачка с преобразованием строк: убирание гласных, преобразование согласных

# a = int(input())
# b = int(input())
# c = int(input())
# d = hex(a)+hex(b)+hex(c)
# print(d.split())  # задачка с преобразованием HEX


# list[] это список, представляет собой упорядоченную коллекцию элементов, изменяемый объект

# sort() – изменяет объект, к которому применяется этот метод
# sorted() – возвращает отсортированный список, не меняя исходный
# my_list.sort() - список сортируется как объект
# sorted_my_list = sorted(my_list) - список предстанет в отсортированном виде, но не сортируется как объект

# map(int, input().split())  # преобразовывает в целое число всё, что будет введено, с разбиением по пробелам
# list(map(int, input().split()))  # предварительно нужно превратить в список, ведь изначально результатом будет объект
# # a = input().split()  # разбивает строку по пробелам и результатом будет список строк
# a, b, c = map(str, input().split())
# print(a, b, c)  # преобразовывает строку в список объектов, используя пробелы как разделители

# a = input().split()
# b = ' '.join(a)
# print(b, type(b))   # соединяет список объектов в строку в список объектов, добавляя пробелы

# list_numbers = list(map(int, input().split()))
# average = sum(list_numbers) / len(list_numbers)
# print(average)  # задачка с вычислением среднего арифметического

# a = list(map(int, input().split()))
# print(a[-3:])  # задачка с выводом последних трёх символов из списка

# a = list(map(int, input().split()))
# print(a[::-1])  # задачка с выводом символов списка наоборот

# num = (int(input())-1)
# months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
# print(months[num])  # задачка с выводом порядкового номера месяца


# a = list(map(int, input().split()))
# b = [3, 5, 7, 9]
#
# if b[0] in a:
#     a.remove(b[0])
# if b[1] in a:
#     a.remove(b[1])
# if b[2] in a:
#     a.remove(b[2])
# if b[3] in a:
#     a.remove(b[3])
# print(a)  # задачка с удалением заданных чисел из списка

# if 'walrus' in (a := input().split()):
#     print('Нашли моржа')
# else:
#     print('Никаких моржей тут нет')

# n = int(input())
# if str(n) == str(n)[::-1]:
#     print('YES')
# else:
#     print('NO')  # задачка на проверку чисел на палиндром

# a = int(input())
# b = int(input())
# c = int(input())
#
# if (a + b > c) and (a + c > b) and (b + c > a):
#     print('YES')
# else:
#     print('NO')  # задачка на проверку существования треугольника


# a = list(map(int, list(input().rjust(6, '0'))))
# if sum(a[:3]) == sum(a[-3:]):
#     print('YES')
# else:
#     print('NO')
# a = input()
# print(a)
# print(a.split())
# print(list(a))  # задачка на сравнение сумм чисел


# a = int(input())
#
# if a // 3 and a // 5:
#     print('FizzBuzz')
# elif a // 3:
#     print('Fizz')
# elif a // 5:
#     print('Buzz')
# else:
#     print(a)  # задачка на FizzBuzz с заменой символов

# a = input()
#
# while len(a) >= 1:
#     a = a[1:-1]
#     print(a)  # задачка на вывод отсекающихся первых и последних букв

# a, b = map(int, input().split())
# c = 1
#
# while a <= b:
#     a *= 1.15
#     c += 1
#
# print(c)  # задачка с бегуном на определение дня, на который он пробежит заданную дистанцию


# n = int(input())

# while str(n)[0] != '1' and n < 1000000000:
#     n *= int(str(n)[0])
# print(n)  # задачка на умножение первого разряда числа на само себя с ограничениями в 1 и до млрд

# a = []
#
# while True:
#     b = int(input())
#     if b == 0:
#         break
#     a.append(b)
#
# print(sum(a))  # оптимальное решение задачки с выводом списка чисел по строкам с прерыванием в 0 и выводом их суммы

# a = []
#
# # while True:
# #     b = input()
# #     if 5 > len(b) or len(b) > 9:
# #         break
# #     a.append(b)
# #
# # print(a[-1])  # оптимальное решение задачки с выводом валидного пароля с прерыванием на невалидный


# a = input()
# c = a
#
# while 5 <= len(a) <= 9:
#     c = a
#     a = input()
#
# print(c)  # простое решение задачки с выводом валидного пароля с прерыванием на невалидный

# n = int(input())
#
# while n > 0:
#     print(n % 10)
#     n //= 10 # убрали таким образом последнее число

# n = int(input())
# d = 2
#
# while d <= n:
#     if n % d == 0:
#         print(d)
#         break
#     d += 1  # задачка на нахождение минимального делителя числа

# n = int(input())
# c = 0
#
# while n > 0:
#     if n == 1:
#         break
#     if n % 2 == 0:
#         c += 1
#         n /= 2
#         continue
#     if n % 2 != 0:
#         c += 1
#         n = n * 3 + 1
#         continue
#     n -= 1
#
# print(c)  # задачка с вычислением ходов в числовой последовательности перед достижением 1 и заменой

# a = input()
# c = 0
#
# while c < len(a):
#     if a[c] == 'a' or a[c] == 'e':
#         print('Ага! Нашлась')
#         break
#     else:
#         print(f"Текущая буква:", a[c])
#         c += 1
# else:
#     print("Распечатали все буквы")  # задачка с перебором букв и нахождении латинских символов


# a = int(input())
# c = 0
#
# while c < a:
#     c += 1
#     print(c)

# a = int(input())
# b = int(input())
#
# for i in range(a, b + 1):
#     if i % 15 == 0:
#         print('FizzBuzz')
#     elif i % 3 == 0:
#         print('Fizz')
#     elif i % 5 == 0:
#         print('Buzz')
#     else:
#         print(i)  # задачка на FizzBuzz


# a = int(input())
# s = 0
#
# for i in range(a):
#     if i % 3 == 0:
#         s += i
#     elif i % 5 == 0:
#         s += i
# print(s)  # задачка на нахождение суммы чисел, кратных 3 или 5

# a = int(input())
# m = 1
#
# for i in range(1, a + 1):
#     m *= i
# print(m)  # задачка на нахождение факториала


# q = int(input())
# m = 0
# c = 0
#
# for i in range(q):
#     a, b = map(int, input().split())
#     if a > b:
#         m += 1
#         c -= 1
#     elif a < b:
#         m -= 1
#         c += 1
# if m > c:
#     print('Mishka')
# elif m < c:
#     print('Chris')
# else:
#     print('Friendship is magic!^^')  # задачка на игру в кости


# q = int(input())
#
# for i in range(q):
#     a = input().lower()
#     if "рок" in a:
#         b = a.find('рок')
#         print(i + 1, b + 1)  # задачка на поиск слова "рок"


# q = int(input())
# c = []
#
# for i in range(q):
#     a = input()
#     if "соль" not in a:
#         c.append(a)
#
# print(', '.join(c))  # задачка на поиск строки со словом "соль"


# numbers = [-35, 68, -91, 23, -92]
# b = len(numbers)
#
# for i in range(b):
#     numbers[i] *= 2
# print(numbers)  # задачка на увеличение каждого числа в массиве вдвое

# q = int(input())
# b = []
#
# for i in range(q):
#     a = input()
#     b.append(a)
# print(b)  # задачка на заполнение списка


# a = input().lower()
# b = input().split()
# c = []
#
# for i in b:
#     if a in i.lower() or a in i.upper():
#         c.append(i)
#
# print('\n'.join(c))  # задачка на вывод слов только с совпадением по букве

# a = list(map(int, input().split()))
# r = int(input())
# n = len(a)
# j = -1
#
# for i in range(n):
#     if a[i] == r:
#         j = i + 1
#         break
# if j != -1:
#     print(j)
# else:
#     print('ErrorValue')  # задачка на линейный поиск


# a = list(map(int, input().split()))
# b = []
# n = len(a)
#
# for i in range(n):
#     if a[i] > 0:
#         b.append(a[i])
# if len(b) > 0:
#     print(min(b))
# else:
#     print('Empty')  # задачка на поиск наименьшего положительного числа


# a = input().lower()
# j = 0
#
# for i in range(len(a)):
#     if a.count(a[i]) > j:
#         j += 1
# print(j)  # задачка на нахождение повторяющихся символов

# a = input()
# c = 0
# s = 0
#
# for i in a:
#     if i.isdigit():
#         c += 1
#         s += int(i)
# print(c, s)  # задачка на нахождение кол-во и сумму найденных чисел


# a = list(map(int, input().split()))
# n = len(a)
# result = True
#
# for i in range(n - 1):
#     if not a[i] <= a[i + 1]:
#         result = False
#         break
#
# print(result)  # задачка с проверкой на возрастание числовой последовательности


# a = [int(i) for i in range(1, int(input()) + 1)]
# print(a)  # задачка с выводом генератора списка от единицы до введённого числа

# n = int(input())
# a = [i for i in range(1, n + 1) if n % i == 0]
# print(a)  # задачка с выводом целочисленных делителей для введённого числа

# n = int(input())
# a = [i for i in range(n, n ** 2 + 1) if i % 2 != 0]
# print(a)  # задачка с выводом нечётных чисел до квадрата введённого числа

# a, b = map(int, input().split())
# n = [i ** 2 for i in range(a, b + 1)] if a <= b else [i ** 3 for i in range(a, b - 1, -1)]
# print(n)  # задачка на вывод квадратов или кубов в обратном порядке

# st = 'Create a list of the first letters of every word in this string'
# print([i[0] for i in st.split()])  # задачка на вывод первых букв в каждом слове

# phrase = 'Take only the words that start with t in this sentence'
# print([i for i in phrase.split() if i[0] in 'Tt'])  # задачка на вывод только слов с "т"

# from string import ascii_uppercase
#
# a = [ascii_uppercase[i] for i in range(int(input()))]
# print(a)  # задачка на вывод первых заглавных букв исходя из введённого числа


# tuple() это кортеж, представляет собой упорядоченную коллекцию элементов, неизменяемый объект

# words_tuple = ('quaint', 'leftovers', 'thesis', 'density', 'retired', 'weak', 'tolerate',
#                'sensitivity', 'primary', 'definition', 'determine', 'bring', 'monstrous',
#                'hurl', 'timetable', 'month', 'advocate', 'provoke', 'stress', 'omission')
# for i in words_tuple:
#     print(f'''Длина слова {i} = {len(i)}''')  # задачка на нахождение длины слов в кортежах

# my_tuple = (-214, 181, -139, 448, -66412)
# n = [i for i in my_tuple if i % 2 != 0]
# print(sum(n) / len(n))  # задачка на вывод среднего арифметического в кортежах


# dict{} это словарь, представляет собой неупорядоченную коллекцию элементов, изменяемый объект (доступ по ключу),
# может состоять в т.ч из изменяемых объектов

# Неизменяемые объекты:
# целые(int) и вещественные(float) числа
# строки (str)
# кортежи (tuple)
# неизменяемые множества (frozenset)
# ничто (None)

# Изменяемые объекты:
# списки (list)
# словари (dict)
# множества (set)

# person = {}
# s = 'IVANOV IVAN 19 Samara SGU 4 5 5 5 4 3 5 3'.split()
#
# person['last_name'] = s[0]
# person['first_name'] = s[1]
# person['age'] = int(s[2])
# person['city'] = s[3]
# person['university'] = s[4]
# person['marks'] = []
# for i in s[5:]:
#     person['marks'].append(int(i))
#
# print(person)  # пример создания словаря из строки с большим кол-вом элементов


# sweet = {"id": "0001", "type": "donut", "name": 'SuperCake', "ppu": 0.55, "calories": 350, "weight": 230,
#          "have_topping": True}
#
# del sweet["ppu"]
# del sweet["type"]
#
# print(sweet)  # задачка на манипуляцию со словарём

# d = {}
#
# for i in range(1, int(input()) + 1):
#     d[i] = i ** 2
#
# print(d)  # задачка на создание словаря с выводом квадрата введённого числа

# from string import ascii_lowercase
#
# alphabet = {}
#
# for i in range(len(ascii_lowercase)):
#     alphabet[ascii_lowercase[i]] = i + 1
#
# print(alphabet)  #задачка на создание словаря с выводом букв в ключах

# currencies = {
#     'Argentine Peso': 118362.205708,
#     'Venezuelan Bolivar': 511082584.868731
# }
# n = input()
# print(currencies[n]) if n in currencies else print(f'Нет данных по {n}')  # задачка по выводу валют из словаря

# account = {
#   "id": 3136,
#   "uid": "1359acc6-f07a-4a2a-984e-3fb809982948",
#   "account_number": "0847799459",
#   "iban": "GB90XTND56373623909314",
#   "bank_name": "ABN AMRO HOARE GOVETT CORPORATE FINANCE LTD.",
#   "routing_number": "126602476",
#   "swift_bic": "BCYPGB2LHGB"
# }
# keys = list(account)
# print(keys)  # задачка на создание словаря только из ключей исходного

# n = int(input())
# reg = {}
# for i in range(n):
#     lg = input()
#     if lg in reg:
#         reg[lg] += 1
#         reg[f"{lg}{reg[lg]}"] = 0
#         print(f"{lg}{reg[lg]}")
#     else:
#         reg[lg] = 0
#         print('OK')
# print(reg)  # задачка с проверкой пароля

# countries = {
#     "Sweden": ["Stockholm", "Göteborg", "Malmö"],
#     "Norway": ["Oslo", "Bergen", "Trondheim"]
# }
# city = input()
#
# for key, value in countries.items():
#     if city in value:
#         print(f'INFO: {city} is a city in {key})'
#         break
# else:
#     print(f'ERROR: Country for {city} not found)'  # задачка с проверкой вхождения города в страну

# user = {
#     "password": "SyUpfo1ljm",
#     "first_name": "Teresa",
#     "last_name": "Wehner",
# }
#
# user["secret"] = user.pop('password')
# user["surname"] = 'last_name'  # задачка на переименование ключей

# l = [1, 2, 3, 4, 5, 6]
# dic = {l[0]: l[1]}
# print(dic)
#
# dic = {l[1]: dic}
# print(dic)  # создание словаря dic, где ключом будет первый элемент списка l, а значением - второй элемент списка l

# s = input().lower()
# d = {}
# for i in s:
#     if i.isalpha():
#         d[i] = d.get(i, 0) + 1
# print(d)  # задачка с выводом кол-ва букв на вхождение

# supermarket = {
#     "milk": {"quantity": 20, "price": 1.19},
#     "biscuits": {"quantity": 32, "price": 1.45}
# }
#
# result = 0
#
# for i in supermarket:
#     result += supermarket.get(i).get('quantity') * supermarket.get(i).get('price')
#
# print(result)  # задачка с подсчётом суммы стоимости всех продуктов


# a = input()
# b = input()
# d1 = {}
# d2 = {}
#
# for i in a:
#     d1[i] = d1.get(i, 0) + 1
# for j in b:
#     d2[j] = d2.get(j, 0) + 1
#
# print(d1, d2)
# if d2 == d1:
#     print('YES')
# else:
#     print('NO')  # задачка с проверкой на анаграммы


# morze = {'a': '•—', 'b': '—•••', 'c': '—•—•', 'd': '—••',
#          'e': '•', 'f': '••—•', 'g': '——•', 'h': '••••',
#          'i': '••', 'j': '•———', 'k': '—•—', 'l': '•—••',
#          'm': '——', 'n': '—•', 'o': '———', 'p': '•——•',
#          'q': '——•—', 'r': '•—•', 's': '•••', 't': '—',
#          'u': '••—', 'v': '•••—', 'w': '•——', 'x': '—••—',
#          'y': '—•——', 'z': '——••'}
#
# sentence = input().lower()
# for i in sentence:
#     if i in morze:
#         print(morze[i], end=' ')
#     else:
#         print(end='\n')
# print()  # задачка с преобразованием фразы в азбуку Морзе

# people = [
#     ['Amy Smith', '694.322.8133x22426'],
#     ['Brian Shaw', '593.662.5217x338'],
#     ['Christian Sharp', '118.197.8810'],
#     ['Sean Schmidt', '9722527521'],
#     ['Thomas Long', '163.814.9938'],
#     ['Joshua Willis', '+1-978-530-6971x601'],
#     ['Ann Hoffman', '434.104.4302'],
#     ['John Leonard', '(956)182-8435'],
#     ['Daniel Ross', '870-365-8303x416'],
#     ['Jacqueline Moon', '+1-757-865-4488x652'],
#     ['Gregory Baker', '705-576-1122'],
#     ['Michael Spencer', '(922)816-0599x7007'],
#     ['Austin Vazquez', '399-813-8599'],
#     ['Chad Delgado', '979.908.8506x886'],
#     ['Jonathan Gilbert', '9577853541']
# ]
#
# phone_book = {i[1]: i[0] for i in people}
# print(phone_book)  # задачка с выводом индексов в виде телефонов


# set{} это множество, представляет собой неупорядоченную коллекцию уникальных элементов, изменяемый объект,
# может состоять только из неизменяемых объектов

# my_set = set([1, 2, 2, 2, 2, 1, 1, 2, 2, 1, 2])
# print(len(my_set))

# a = set(input())
# print('IGNORE HIM!' if len(a) % 2 != 0 else 'CHAT WITH HER!')  # задачка с подсчётом кол-ва уникальных букв
#
# from string import ascii_lowercase
# text = ascii_lowercase
#
# a = set(input().lower())
# print('YES' if 26 - len(a) == 0 else 'NO')  # задачка на наличие панграммы

# a = int(input())
#
# while True:
#     a += 1
#     if len(set(str(a))) == 4:
#         print(a)
#         break  # задачка с выводом красивого года (все цифры различны)

# a = input()
# b = {i for i in a if i.isalpha()}
# print(len(b))

# my_friend = {'Bill', 'Ash', 'Pikachu', 'Jim'}
# jack_friends = {'Bill', 'Kir', 'Pikachu'}
#
# intersections_me_jack = my_friend & jack_friends
# print('Мои общие друзья с Джеком', intersections_me_jack)

# words = ['mention', 'soup', 'pneumonia', 'tradition', 'concert', 'tease', 'generation',
#          'winter', 'national', 'jacket', 'winter', 'wrestle', 'proposal', 'error',
#          'pneumonia', 'concert', 'value', 'value', 'disclose', 'glasses', 'tank',
#          'national', 'soup', 'feel', 'few', 'concert', 'wrestle', 'proposal', 'soup',
#          'sail', 'brown', 'service', 'proposal', 'winter', 'jacket', 'mention', 'tradition',
#          'value', 'feel', 'bear', 'few', 'value', 'winter', 'proposal', 'government',
#          'control', 'value', 'few', 'generation', 'service', 'national',
#          'tradition', 'government', 'mention', 'proposal']
# a = set()
#
# for i in words:
#     if len(i) > 6:
#         a.add(i)
# print(len(a))  # задачка с выводом кол-ва уникальных слов с длиной больше 6


# n = int(input())
#
# for i in range(n):
#     a = list(input().split())
#     print(len(set(a)))  # задачка с выводом уникальных символов исходя из количеств введённых последовательностей

# my_set = {'government', 'control', 'winter', 'few', 'generation',
#           'service', 'national', 'tradition', 'government'}
# my_set.update(['concert', 'brown', 'jacket', 'value'])
# print(my_set)

# n = int(input())
# b = set()
#
# for i in range(n):
#     a = set(map(int, input().split()))
#     b |= a
# print(len(b))  # задачка с выводом объединяющего множества уникальных символов исходя из количеств последовательностей

# a = input().lower().split(',')
# b = set()
#
# for i in a:
#     if i not in b:
#         b.add(i)
#         print('НЕТ')
#     else:
#         print('ДА')  # задачка с проверкой на повторяемость слов

# set_str = {'car', 'soup', 'bus'}
# set_num = {1, 2, 3}
# my_list = [True, 101, 'hello', 'soup', 2]
# new_set = set_str.union(set_num)

# a = set(map(int, input().split()))
# b = set(map(int, input().split()))
# c = sorted(set((a.intersection(b))))
# print(' '.join(map(str, c)))

# a = input()
# b = set(a)
#
# for i in a:
#     if i in b:
#         print(i, end="")
#         b.remove(i)  # задачка с проверкой на удаление повторных символов


# frozenset{} это множество, представляет собой неупорядоченную коллекцию уникальных элементов, неизменяемый объект

# def() это функция, многократно используемый фрагмент программы. При помощи функций можно объединить несколько
# инструкций в один блок, присвоить этому блоку имя и затем, обращаясь по имени этого блока, выполнить инструкции
# внутри него в любом месте программы необходимое число раз.

# def sum_num(rnd):  #rnd – это параметр, имя, используемое при определении функции
#     for i in rnd:
#         if rnd_str.isdigit():
#             rnd += i
#     print(rnd)
#
#
# rnd_str = input()
# sum_num(rnd_str)    #rnd_str – это аргумент, данные, передаваемое функции в момент вызова

# def sum_num(rnd):
#     s = 0
#     for i in rnd:
#         if i.isdigit():
#             s += int(i)
#     print(s)
#
#
# rnd_str = input()
# sum_num(rnd_str)  # задачка на подсчёт всех чисел в пользовательском вводе


# def get_body_mass_index(w, h):
#     index = w / ((h / 100) ** 2)
#     if index < 18.5:
#         print("Недостаточная масса тела")
#     elif index > 25:
#         print("Избыточная масса тела")
#     else:
#         print("Норма")
#
#
# weight, height = map(int, input().split())
# get_body_mass_index(weight, height)  # задачка на подсчёт всех ИМТ

# def check_password(psw):
#     count_of_digit = 0
#     has_uppercase = False
#     has_special = False
#
#     for i in psw:
#         if i.isdigit():
#             count_of_digit += 1
#         elif i.isupper():
#             has_uppercase = True
#         elif i in "!@#$%*":
#             has_special = True
#
#     if count_of_digit >= 3 and has_uppercase and has_special and len(psw) >= 10:
#         print("Perfect password")
#     else:
#         print("Easy peasy")
#
#
# password = input()
# check_password(password)  # задачка на валидацию пароля


# def count_letters(ltr):
#     count_of_upper = 0
#     count_of_lower = 0
#
#     for i in ltr:
#         if i.isupper():
#             count_of_upper += 1
#         elif i.islower():
#             count_of_lower += 1
#
#     print(f"Количество заглавных символов: {count_of_upper}")
#     print(f"Количество строчных символов: {count_of_lower}")
#
#
# letters = input()
# count_letters(letters)  # задачка на подсчёт кол-ва заглавных и строчных букв


# def count_letter(text, letter):
#     c = 0
#     for letter in text:
#         if letter == symbol:
#             c += 1
#     print(c)
#
#
# phrase = input()
# symbol = input()
# count_letter(phrase, symbol)  # задачка на подсчёт букв в тексте

# def print_initials(name, surname, middlename):
#     print(surname.capitalize() + ' ' + name[0].capitalize() + '.' + middlename[0].capitalize() + '.')
#
#
# a, b, c = input().split()
# print_initials(a, b, c)  # задачка на вывод фамилии с инициалами

# Функция – подпрограмма, выполняющая какие-либо операции и возвращающая значение.
# Процедура – подпрограмма, которая выполняет только операции и не возвращает значения.
# Метод – функция / процедура, которая принадлежит классу или экземпляру класса.

# В задачах без return мы просто вызывали функцию. И этот "просто вызов" выполнял задание, вместе с принтом,
# который был частью тела функции, и выводит результат в консоль. Там же, где используется return, – вызов функции
# уже не "просто вызов", а именно сохранение результата или его "присвоение" в переменную. Поэтому мы либо нуждаемся
# в отдельном принте уже нашей переменной, в которую присвоили результат вызова функции, либо оборачиваем сам вызов
# функции в принт, что бы увидеть результат работы функции. Переменная, объявленная внутри какой-либо функции,
# является локальной. Область видимости локальной переменной ограничена пределами функции, внутри которой она
# объявлена. Чтобы как-то работать с результатом вычислений вне функции и нужен return.

# Утверждение (assert) — это логическое выражение, которое проверяет, является ли утверждение истинным или ложным.
# Если утверждение истинно, то оно ничего не делает и продолжает выполнение, но если утверждение ложно,
# то оно останавливает выполнение программы и выдает ошибку. Инструкция assert может использоваться для проверки
# правильности выполнения кода и тем самым быть основой для тестирования. При помощи assert вы можете написать тесты
# и проверить работоспособность своей функции assert condition [, Error Message]

# def factorial(x):
#     pr = 1
#     for i in range(2, x + 1):
#         pr *= i
#     return pr
#
#
# assert factorial(1) == 1, '1! должен быть равен 1'
# assert factorial(2) == 2, '2! должен быть равен 2'
# assert factorial(3) == 3, '3! должен быть равен 6'
# assert factorial(4) == 24, '4! должен быть равен 24'
# assert factorial(5) == 120, '5! должен быть равен 120'
#
# print('Тесты пройдены')

# assert 200 > 100
# assert [100] * 4 < [100, 100, 100, 10000]
# assert sum([1, 3, 5]) == sum(list((6, 3)))
# assert max(3, -1, 9) != -1
#
# print('Проверки пройдены')

# Выражение [100] * 4 создает новый список, повторяя элемент [100] четыре раза. Внутренний элемент - это число 100,
# но он все равно хранится как список. Таким образом, [100] * 4 создает список, содержащий четыре копии списка [100],
# а не просто четыре числа 100. Это связано с тем, что операция умножения списка на число просто дублирует
# список заданное количество раз, независимо от того, что находится внутри списка. В результате получается список из
# нескольких ссылок на тот же объект [100]. Таким образом, результатом [100] * 4 будет список, содержащий четыре
# ссылки на один и тот же список [100], что дает [100, 100, 100, 100]. Если необходимо получить [400],
# то нужно было бы использовать [100] * 4 для создания списка и затем сложить его элементы вместе.

# sum() принимает итерируемый объект в качестве аргумента и возвращает сумму его элементов. Список [] является
# итерируемым объектом, поэтому его элементы могут быть просуммированы. Однако кортеж () не является итерируемым
# объектом, так как кортеж состоит из фиксированного числа элементов, доступ к которым осуществляется по индексу.

# def is_person_teenager(age):
#     if 12 <= age <= 17:
#         print(True)
#     else:
#         print(False)
#
#
# a = int(input())
# is_person_teenager(a)  # Данная функция напрямую печатает результат проверки


# def is_person_teenager(age):
#     return 12 <= age <= 17
#
#
# a = int(input())
# if is_person_teenager(a):
#     print(True)
# else:
#     print(False)  # Данная функция возвращает результат, который затем используется для принятия решения о выводе

# Функция, которая использует return, более гибкая и может быть использована в различных контекстах, в то время как
# функция с print привязана к выводу на экран и может быть менее удобной для повторного использования.

# def factorial(x):
#     pr = 1
#     for i in range(2, x + 1):
#         pr *= i
#     return pr  # задачка на вывод факториала через функцию


# def generate_fizz_buzz_list(n):
#     l = []
#
#     for i in range(1, n + 1):
#         if i % 15 == 0:
#             l.append('FizzBuzz')
#         elif i % 3 == 0:
#             l.append('Fizz')
#         elif i % 5 == 0:
#             l.append('Buzz')
#         else:
#             l.append(i)
#     return l
#
#
# n = int(input())
# result = generate_fizz_buzz_list(n)
# print(result)  # задачка на генерацию функции FizzBuzz


# def find_duplicate(n):
#     l = []
#
#     for i in n:
#         if n.count(i) > 1 and i not in l:
#             l.append(i)
#
#     return l
#
#
# assert find_duplicate([1, 1, 1, 1, 1, 2, 2, 2, 2]) == [1, 2]
# assert find_duplicate([2, 1, 1, 1, 1, 1, 2, 2, 2, 2]) == [2, 1]
# assert find_duplicate([1, 2, 3, 4]) == []
# assert find_duplicate([8, 7, 6, 5, 4, 3, 4, 5, 6, 7, 8]) == [8, 7, 6, 5, 4]
# print('Все успешно')  # задачка на показ дублей в списке и утверждения (мини-тест)


# def first_unique_char(s):
#
#     for i in range(len(s)):
#         if s.count(s[i]) == 1:
#             return i
#     return -1
#
#
# s = input()
# result = first_unique_char(s)
# print(result)  # задачка на поиск первого уникального символа в строке


# def count_AGTC(dna):
#     l = []
#     s = dna.count
#
#     for i in 'AGCT':
#         l.append(dna.count(i))
#     return s('A'), s('G'), s('T'), s('C')
#
#
# assert count_AGTC('AGGTC') == (1, 2, 1, 1)
# assert count_AGTC('AAAATTT') == (4, 0, 3, 0)
# assert count_AGTC('AGTTTTT') == (1, 1, 5, 0)
# assert count_AGTC('CCT') == (0, 0, 1, 2)
# print('Проверки пройдены')  # задачка на показ вхождений в последовательность нуклеотидов в списке и мини-тест


# def first_repeated_word(s: str) -> str | None:
#     """Находит первый дубль в строке"""
#     s = s.split()
#     l = []
#     for i in s:
#         if i in l:
#             return i
#         else:
#             l.append(i)
#     return None
#
#
# print(first_repeated_word(input()))  # задачка на поиск первого дубля и аннотации


# В Python существует 4 вида пространства имен:
#
# - builtins (встроенное пространство имен)
# - global (глобальное пространство имен)
# - enclosing (объемлющее пространство имен)
# - local (локальное пространство имен)

# MIN_DRIVING_AGE = 18
#
#
# def allowed_driving(name: str, age: int) -> None:
#     global MIN_DRIVING_AGE
#     if age >= MIN_DRIVING_AGE:
#         print(f"{name} может водить")
#     else:
#         print(f"{name} еще рано садиться за руль")
#
#
# allowed_driving('tim', 18)  # задачка на локальные/глобальные переопределения

# def greetings(name, msg="Welcome, Good Morning"):
#     message = f"Hello {name}! {msg}"
#     print(message)  # задачка на вывод необязательных параметров с дефолтным значением


# greetings("Neo")  #если дефолтное значение подходит, его можно не передавать в аргумент
# greetings("Neo", "You are the one") #если дефолтное значение не подходит, его просто передаём в аргумент


# def replace(text: str, old: str, new: str = ''):
#     return text.replace(old, new)  #задачка на замену текста


# def make_header(text: str, level: int = 1):
#     return f"<h{level}>{text}</h{level}>"  #задачка на возврат заголовка html


# В параметре *arg хранится тип данных tuple()
# В параметре **kwarg хранится тип данных dict{}
# *args – произвольное число неименованных, позиционных аргументов
# **kwargs – произвольное число именованных аргументов
# Распаковка – список
# Упаковка – кортеж
# Также при передаче * в методе функции мы принуждаем явно прописать переменные в вызове аргументов функции


# def count_args(*args):
#     return len(args)
#
#
# count_args(1, 3, 4)  # задачка на подсчёт кол-ва аргументов


# def multiply(*args: int):
#     m = 1
#
#     for i in args:
#         m *= i
#     return m
#
#
# print(multiply(1, 2, 3))  # задачка на подсчёт произведения аргументов


# def only_one_positive(*args: int):
#     c = 0
#     for i in args:
#         if i > 0:
#             c += 1
#     return c == 1
#
#
# print(only_one_positive(-1, 0, -3, 5, -3))  # задачка на подсчёт кол-ва положительных чисел


# def print_goods(*elements) -> None:
#     answer = [i for i in elements if type(i) is str and len(i) != 0]
#
#     if not answer:
#         print(f'Нет товаров')
#     else:
#         for i, v in enumerate(answer, 1):
#             print(f'{i}. {v}')  # задачка на вывод списка продуктов


# def info_kwargs(**kwargs):
#     for i, j in sorted(kwargs.items()):
#         print(f"{i}={j}")
#
#
# info_kwargs(first_name="John", last_name="Doe", age=33)  # задачка на вывод сортированного списка


# def create_actor(name='Райан', surname='Рейнольдс', age=46, **kwargs):
#     d = {}
#
#     d.setdefault('name', name)
#     d.setdefault('surname', surname)
#     d.setdefault('age', age)
#
#     for key, value in kwargs.items():
#         d.setdefault(key, value)
#     return d
#
#
# print(create_actor(height=190, movies=['Дедпул', 'Главный герой']))  # задачка на вывод списка актёров


# Рекурсия в программировании – ситуация, когда функция вызывает саму себя

# def fact(n):
#     if n == 1:
#         return 1
#     return fact(n-1) * n
#
#
# print(fact(4))  # рекурсия для факториала


# def fib(n):
#     if n==0:
#         return 0
#     if n==1:
#         return 1
#     return fib(n-1) + fib(n-2)
#
#
# print(fib(5))  # рекурсия для Фибоначчи


# def is_palindrome(s):
#     if len(s) <= 1:
#         return True
#     if s[0] != s[-1]:
#         return False
#     return is_palindrome(s[1:-1])
#
#
# print(is_palindrome("шалаш"))  # рекурсия для палиндрома


# def print_from(n):
#     if n > 0:
#         print(n)
#         print_from(n-1)
#
#
# print_from(4)  # рекурсия с выводом обратной последовательности


# def print_to(n):
#     if n > 0:
#         print_to(n-1)
#         print(n)
#
#
# print_to(4)  # рекурсия с выводом прямой последовательности


# adding_10 = lambda a: a + 10  # задачка с выводом lambda-функции

# average = lambda *args: sum(args) / len(args)  # задачка с выводом среднего арифметического по lambda-функции

# sort – это метод списка (list), а sorted – это функция.
# sort можно применять только к спискам (list), вызывая как метод.
# sorted может сортировать не только списки, но и другие коллекции.
# При использовании метода sort меняется изначальный список, сам метод в качестве результата возвращает None.
# При вызове функции sorted сам объект не меняется, результатом будет новый отсортированный список.

# =СОРТИРОВКА СПИСКА=
# сортировка по возрастанию по числу, если оно является частью элемента списка:
# a = ['ZZZ 800','aaa 45','eee 43', 'DDD 800', 'BBB 43', 'www 14']
# print(sorted(a, key=lambda x: int(x.split()[1])))
#
# >>> ['www 14', 'eee 43', 'BBB 43', 'aaa 45', 'ZZZ 800', 'DDD 800']
#
#
# сортировка по возрастанию по числу и строке, если оно является частью элемента списка:
# a=['ZZZ 800','aaa 45','eee 43', 'ddd 800', 'BBB 43', 'www 14']
# print(sorted(a, key=lambda x: (int(x.split()[1]), x.split()[0].lower())))
#
# >>> ['www 14', 'BBB 43', 'eee 43', 'aaa 45', 'ddd 800', 'ZZZ 800']
#
#
# сортировка по убыванию по числу, если оно является частью элемента списка:
# a=['ZZZ 800','aaa 45','eee 43', 'ddd 800', 'BBB 43', 'www 14']
# print(sorted(a, key=lambda x: (-int(x.split()[1]), x.split()[0].lower())))
#
# >>> ['ddd 800', 'ZZZ 800', 'aaa 45', 'BBB 43', 'eee 43', 'www 14']
#
#
# сортировка по убыванию по числу и строке, если оно является частью элемента списка:
# a=['ZZZ 800','aaa 45','eee 43', 'ddd 800', 'BBB 43', 'www 14']
# print(sorted(a, key=lambda x: (int(x.split()[1]), x.split()[0].lower()) , reverse=True)))
#
# >>> ['ZZZ 800', 'ddd 800', 'aaa 45', 'eee 43', 'BBB 43', 'www 14']
#
#
# сортировка по возрастанию по числу + по убыванию по строке:
# a=['ZZZ 800','aaa 45','eee 43', 'ddd 800', 'AaA 43', 'aaa 14']
# a = sorted(a, key=lambda x: int(x.split()[1]) )
# print(a)
# a = sorted(a, key=lambda x: x.split()[0].lower(), reverse=True )
# print(a)
#
# >>> ['aaa 14', 'eee 43', 'AaA 43', 'aaa 45', 'ZZZ 800', 'ddd 800']
# >>> ['ZZZ 800', 'eee 43', 'ddd 800', 'aaa 14', 'AaA 43', 'aaa 45']


# subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Physics', 93), ('History', 82)]
# sorted_subject_marks = sorted(subject_marks, key=lambda x: x[1])
# [print(*tu) for tu in sorted_subject_marks]  # задачка на вывод отсортированного списка оценок по возрастанию


# subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Physics', 93), ('History', 82),
#                   ('French', 78), ('Art', 58), ('Chemistry', 76), ('Programming', 91)]
# sorted_subject_marks = sorted(subject_marks, key=lambda x: (-int(x[1])))
# [print(*tu) for tu in sorted_subject_marks]  # задачка на вывод отсортированного списка оценок по убыванию


# subject_marks = [('English', 88), ('Science', 90), ('Maths', 88), ('Physics', 93), ('History', 78),
#                  ('French', 78), ('Art', 78), ('Chemistry', 88), ('Programming', 91)]
# sorted_subject_marks = sorted(subject_marks, key=lambda x: (-int(x[1]), str(x[0].lower())))
# [print(*tu) for tu in sorted_subject_marks]  # задачка на вывод отсортированного списка оценок по убыванию и по
# возрастанию предметов


# =СОРТИРОВКА СЛОВАРЯ=
# heroes = {
#     'spider-man':80,
#     'batman': 65,
#     'superman': 85,
#     'wonder woman': 70,
#     'flash': 70,
#     'iron man': 65,
#     'thor': 90,
#     'aquaman': 65,
#     'captain america': 65,
#     'hulk': 87
# }
#
# # 1 сортировка по значениям
# for i in sorted(heroes.items(), key=lambda p: p[1]):
#     print(*i)
#
# # 2 сортировка по значениям + по ключам при одинаковых значениях
# for i in sorted(heroes.items(), key=lambda p: (p[1], p[0])):
#     print(*i)


# models = [{'make': 'Nokia', 'model': 216, 'color': 'Black'},
#           {'make': 'Mi Max', 'model': 2, 'color': 'Gold'},
#           {'make': 'Samsung', 'model': 7, 'color': 'Blue'},
#           {'make': 'Apple', 'model': 10, 'color': 'Silver'},
#           {'make': 'Oppo', 'model': 9, 'color': 'Red'},
#           {'make': 'Huawei', 'model': 4, 'color': 'Grey'},
#           {'make': 'Honor', 'model': 3, 'color': 'Black'}]
#
# sorted_models = sorted(models, key=lambda x: x['color'])
# [print('Производитель: ' + i['make'] + ', модель: ' + str(i['model']) + ', цвет: ' + i['color'])
# for i in sorted_models]
# # задачка на вывод отсортированного словаря по цвету


# l = []
#
# while True:
#     a = list(map(str, input().split(': ')))
#     if a == ['конец']:
#         break
#     l.append(a)
#
# [print(i[0]) for i in sorted(l, key=lambda x: -int(x[1]))]  # задачка на вывод полученных значений по убыванию цены


# l = [i.split(':') for i in iter(input, 'конец')]
# [print(i[0]) for i in sorted(lst, key=lambda x: -int(x[1]))]
# оптимальное решение задачки на вывод полученных значений по убыванию цены


# Команда nonlocal в Python используется во вложенных функциях, чтобы указать, что переменная,
# объявленная во внешней функции, должна быть изменена во вложенной функции,
# а не создана локально как новая переменная с тем же именем.


# def calculate(x: float, y: float, operation_symbol: str = 'a') -> None:
#     def addition():
#         print(x + y)
#
#     def subtraction():
#         print(x - y)
#
#     def multiplication():
#         print(x * y)
#
#     def division():
#         if y == 0:
#             print('На ноль делить нельзя!')
#         else:
#             print(x / y)
#
#     if operation_symbol not in ['a', 's', 'm', 'd']:
#         print(f'Ошибка. Данной операции не существует')
#     else:
#         match operation_symbol:
#             case 'a':
#                 addition()
#             case 's':
#                 subtraction()
#             case 'd':
#                 division()
#             case 'm':
#                 multiplication()  # задача по написанию простого калькулятора

# Замыкание (closure) — это функция, которая находится внутри другой функции и
# ссылается на переменные объявленные в теле внешней функции (свободные переменные).
# Замыканием называется ситуация, когда вложенная функция пользуется переменными, которые не объявлены в её теле.
# Замыканием является область видимости, включающая в себя всё тело глобальной функции.
# При этом локальная переменная, объявленная внутри глобальной, но за пределами внутренней функции,
# не исчезнет после завершения.

# Декоратор – функция, которая принимает одну функцию и возвращает другую функцию.
# Они нужны для того, чтобы функции добавилось новое поведение.

# Работа с файловой системой через чтение/запись:
# with open('my_text.txt') as file:
#     print(file.read())  # способ создания и чтения файлов

# file = open(r'/Users/darliro/Documents/QAMaterials/StudyExec/EducationalRepos/pythonProj/my_text.txt',
#             encoding='utf-8')
# print(file.read())  # альтернативный способ чтения файла через полный путь и с выводом кириллицы


# my_file = open('my_text.txt')

# print(my_file.read(3))  # считываем первые 6 символов
# my_file.seek(0)  # возвращаем каретку в начало файла
# print(my_file.read(50))  # считываем 50 символов с начала
# print(my_file.readline().strip())  # считываем по 1 строке, избавляясь от пустой строки
# print(my_file.readline().strip())
# print(my_file.readline().strip())

# my_file = open('my_text.txt', encoding='utf-8')
#
# rows = my_file.readlines()
# print(rows)
# print('-' * 10)
# print(f'Файл содержит {len(rows)} строк')
# print('-' * 10)
# print('Итерируемся по строкам')
# for row in rows:
#     print(row.strip())  #считываем файл целиком по строкам, строки генерируем в список

# my_file = open('my_text.txt', mode='a')  # режим 'w' перезатрёт все изменения, поэтому используем 'a'
# print(my_file.write('Here we go again\n'))
# print(my_file.write('Again hello and bye!'))  # запись в файл


# def file_read(file_name: str) -> None:
#     file = open(file_name, encoding='utf-8')
#     print(file.read())
#     file.close()  # задачка на функцию о принятии имени файла и печати его содержимого с кириллицей

# def file_n_lines(file_name: str, n: int) -> None:
#     with open(file_name, 'r') as file:
#         rows = file.readlines()
#         for i in range(n):
#             print(rows[i].strip())
#
#
# file_n_lines('my_text.txt', 2)  # задачка на функцию о выводе строк файла


# def create_file_with_numbers(n: int) -> None:
#     with open(f"range_{n}.txt", 'a') as file:
#         for i in range(1, n + 1):
#             file.write(str(i) + '\n')
#
#
# create_file_with_numbers(3)  # задачка на функцию о выводе чисел в новый файл


# numbers = list(map(int, open("numbers.txt").read().split()))
# c = 0
# s = 0
# for i in numbers:
#     if len(str(i)) == 3:
#         c += 1
#     elif len(str(i)) == 2:
#         s += i
#
#
# print(c, s)  # задачка на подсчёт кол-ва трёхзначных и суммы двузначных чисел

# with open('lorem.txt', 'r') as f:
#     f = f.read().lower()
#     count = 0
#     sp = []
#     for i in f.split():
#         sp.append(i)


#     print(len(set(sp)))  # задачка на вывод уникальных слов


# with open('lorem.txt', 'r') as f:
#     f = f.read().upper().split()
#     words = {}
#     for i in f:
#         words[i] = f.count(i)
#
# print(len(set(words)))  # задачка на вывод кол-ва повторений слов


# Сериализация в общем виде – это процесс сохранения объекта в виде последовательности байт, чтобы в будущем
# по этой последовательности можно было бы восстановить исходный объект.
# Это преобразование словаря в JSON-строку.
#
# Например, такой вот словарь:
# {
#  'apple': {"price": 10,"color": "green"},
#  'banana': {"price": 4.5, 'color': "yellow"},
# }
# будет преобразован вот в такую строку:
# '{"apple": {"price": 10, "color": "green"}, "banana": {"price": 4.5, "color": "yellow"}}'
#
#
# Десериализация – это обратный процесс.
# Это «раскодирование» строки JSON-формата обратно в питоновский словарь.
# Если необходимо отправить данные с клиента на сервер, то преобразовываем объект в JSON – сериализация.
# Если необходимо получить данные извне для использования на клиенте – это десериализация.


# Модуль json
# Основным инструментом по работе с форматом JSON является одноименный модуль json.
# Его не нужно устанавливать, он является встроенным модулем и ставится вместе с интерпретатором python.
#
# import json
#
# Функции сериализации:
# -dumps – преобразует объект в строку в формате json
# -dump – преобразует объект в строку в формате json и записывает в файл
#
# Функции десериализации:
# -loads – десериализует JSON-строку в питоновский объект
# -load – десериализует файл, хранящий JSON-строку, в питоновский объект

# ==РАБОТА С JSON В PYTHON==
# Парсинг JSON, сохраняем JSON в файл, преобразуем в питоновский объект при помощи функции load.
# Считываем файлик, а именно, строки в формате json.
# Далее методом dump создаём файлик, а именно, строки в виде json

# import json
# from random import randint
# from datetime import datetime
#
# str_json = """
# {
#     "response": {
#         "count": 5961878,
#         "items": [{
#             "first_name": "Елизавета",
#             "id": 620471795,
#             "last_name": "Сопова",
#             "can_access_closed": true
#         }, {
#             "first_name": "Роман",
#             "id": 614752515,
#             "last_name": "Малышев",
#             "can_access_closed": true
#         }]
#     }
# }"""
# print(type(str_json))
#
# data = json.loads(str_json)
# print(type(data))  # проверяем, какой тип объекта
# # обходим список items циклом for
# for item in data["response"]["items"]:
#     print(item["first_name"], item["last_name"])  # так распарсили джейсонину
#
# # создаём собственную джейсонину
# for item in data["response"]["items"]:
#     del item['id']  # удаляем один ключ
#     item['a'] = None  # добавляем None в джейсоне – это будет null
#     item['likes'] = randint(100, 200)  # добавляем словарь лайков
#     item['now'] = datetime.now().strftime('%d/%m/%y')  # преобразуем в одному из базовых типов с поддержкой джейсон
# print(data["response"]["items"])
#
# # создаём новую джейсонину из нового словарика
# new_json = json.dumps(data, indent=2)  # передаём функции dump объект, который хотим превратить в джейсон
# print(new_json)
#
# # очень часто джейсон нужно будет сохранять в виде файла
# with open('my.json', 'w') as file:  # создаём файл
#     json.dump(data, file, indent=3)  # добавляем indent для красоты вывода
#
# with open("my_json", 'r') as file:  # загружаем наши данные из файлика в переменную data
#     date = json.load(file)
# print(data)


# =ДЕСЕРИАЛИЗАЦИЯ=

# import json
# from pprint import pprint
#
# str_json = """
# {
#     "response": {
#         "count": 32363,
#         "items": [
#             {
#                 "id": 287350527,
#                 "first_name": "Sonya",
#                 "last_name": "Kargina",
#                 "photo_50": "https://pp.vk.me/...2c1/J2EL--qCZa8.jpg"
#             },
#             {
#                 "id": 341523166,
#                 "first_name": "Slava",
#                 "last_name": "Kholod",
#                 "photo_50": "https://pp.vk.me/...321/eTxKNQSJMuk.jpg"
#             }
#         ]
#     }
# }
# """

# data = json.loads(str_json)
# pprint(type(data))
# pprint(data)
# print(data["response"]["count"])

# for item in data["response"]["items"]:
#     print(item["first_name"], item["last_name"])  # обход элементов списка


# =СЕРИАЛИЗАЦИЯ=

# import json
# from pprint import pprint
# from random import randint
#
# str_json = """
# {
#     "response": {
#         "count": 32363,
#         "items": [
#             {
#                 "id": 287350527,
#                 "first_name": "Sonya",
#                 "last_name": "Kargina",
#                 "photo_50": "https://pp.vk.me/...2c1/J2EL--qCZa8.jpg"
#             },
#             {
#                 "id": 341523166,
#                 "first_name": "Slava",
#                 "last_name": "Kholod",
#                 "photo_50": "https://pp.vk.me/...321/eTxKNQSJMuk.jpg"
#             }
#         ]
#     }
# }
# """
#
# data = json.loads(str_json)
#
# for item in data["response"]["items"]:
#     del item["id"]
#     item["likes"] = randint(100, 200)
#
# new_json = json.dumps(data)
# print(new_json)
#
# print('Ниже json с параметром indent'.center(40, '-'))
#
# json_indent = json.dumps(data, indent=2)
# print(json_indent)


# import json
#
# dct_json = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
# 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24,
# 'y': 25, 'z': 26}
#
# json_data = json.dumps(dct_json)
# print(json_data)  # задачка на сериализацию словаря алфавитного списка


# import json
#
# json_string = """
# {
#    "customers": [
#         {
#          "userid": 123456,
#          "username": "Allie Hsu",
#          "phone": [
#             "000-001-0002",
#             "000-002-0002"
#          ],
#           "is_vip": true
#          },
#          {
#             "userid": 223678,
#             "username": "Donald Duck",
#             "phone": null,
#             "is_vip": false
#          }
#       ]
#    }
# """
#
# data = json.loads(json_string)
# print(data['customers'][0]['username'])  # задачка на десериализацию вывода имени клиента

# import json
#
# with open('manager_sales.json', 'r') as file:
#     data = json.load(file)
#
# total_price = 0
# for item in data:
#     s = 0
#     for car in item['cars']:
#         s += car['price']
#     if s > total_price:
#         total_price = s
#         first_name = item['manager']['first_name']
#         last_name = item['manager']['last_name']
#
# print(first_name, last_name, total_price)  # задачка по поиску максимально эффективного продавца


# import json
#
# with open('group_people.json', 'r') as file:
#     data = json.load(file)
#
# count_of_women = 0
# for item in data:
#     max_amount = 0
#     for person in item['people']:
#         if person['gender'] == 'Female' and person['year'] > 1977:
#             max_amount += 1
#     if max_amount > count_of_women:
#         count_of_women = max_amount
#         id_of_group = item['id_group']
#
# print(id_of_group, count_of_women)  # задачка по поиску максимального кол-ва женщин после 1977г

# import json
#
# with open('Abracadabra__1_.txt', encoding='utf-8') as abra, open('Alphabet.json', encoding='utf-8') as alph:
#     data = json.load(alph)
#     text = abra.read()
#     for i in text:
#         print(data.setdefault(i, i), end='')  # задачка по декодированию


# Генератор – итератор; его элементы можно итерировать только один раз
# Итератор – объект, который поддерживает функцию next().
# Помнит о том, какой элемент будет браться следующим
# Итерируемый объект – объект, который предоставляет возможность обойти поочередно свои элементы.
# Может быть преобразован к итератору


# # Создайте генератор
# from_10_to_20 = (i for i in range(10, 21))
#
# # Распечатайте три первых значения
# print(next(from_10_to_20))
# print(next(from_10_to_20))
# print(next(from_10_to_20))
#
# # Выведите все оставшиеся
# for value in from_10_to_20:
#     print(value)

# def utf8_array_to_str(array):
#     out = ""
#     i = 0
#     while i < len(array):
#         c = array[i]
#         i += 1
#         if c >> 7 == 0:  # Одиночный байт: 0xxxxxxx
#             out += chr(c)
#         elif c >> 5 == 6:  # Двойной байт: 110xxxxx 10xxxxxx
#             char2 = array[i]
#             i += 1
#             out += chr(((c & 0x1F) << 6) | (char2 & 0x3F))
#         elif c >> 4 == 14:  # Тройной байт: 1110xxxx 10xxxxxx 10xxxxxx
#             char2 = array[i]
#             char3 = array[i + 1]
#             i += 2
#             out += chr(((c & 0x0F) << 12) | ((char2 & 0x3F) << 6) | (char3 & 0x3F))
#     return out
#
# # Пример использования функции
# byte_array = [72, 101, 108, 108, 111, 44, 32, 119, 111, 114, 108, 100]  # Массив байт, представляющий строку
# print(utf8_array_to_str(byte_array))  # Выведет "Hello, world"


# Создайте генератор
# from_10_to_20 = (i for i in range(10, 21))
#
# # Распечатайте три первых значения
# print(next(from_10_to_20))
# print(next(from_10_to_20))
# print(next(from_10_to_20))
#
# # Выведите все оставшиеся
# for value in from_10_to_20:
#     print(value)

# words = ['feel', 'graduate', 'movie', 'fashionable', 'bacon', 'drop', 'produce', 'acquisition',
#          'cheap', 'strength', 'master', 'perception', 'noise', 'strange', 'am']
#
# lens = (len(i) for i in words)
#
# for i in lens:
#     print(i)  # задачка на создание генератора длин слов


# weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# days = ((i + 1, weekdays[(5 + i) % 7]) for i in range(365))
#
# for i in range(77):
#     print(next(days))  # задачка на создание генератора дней недели для года

# def gen_squares(n: int):
#     q = 1
#     for i in range(1, n + 1):
#         q = i ** 2
#         yield q
#
#
# for sq in gen_squares(5):
#     print(sq)  # задачка на вывод каждого квадрата числа


# def gen_fibonacci_numbers(n):
#     a, b = 1, 1
#
#     for i in range(n):
#         yield a
#
#         a, b = b, a + b
#
#
# for i in gen_fibonacci_numbers(10):
#     print(i)  # задачка на вывод чисел Фибоначчи


# t = list(map(lambda x: (x.upper(), x.lower()), input().split()))
# print(t)  # задачка на вывод списка кортежей из буквы в обоих регистрах


# new_names = list(map(lambda x: (' '.join(x)), names))
# print(new_names)  # задачка на вывод списка имён вместе вместо кортежей


# phones = list(map(lambda x: x.get('phone'), persons))
# print(phones)  # задачка на вывод только значений по ключам телефонов из списка


# negative_numbers = len(list(filter(lambda x: x < 0, numbers)))
# zero_numbers = len(list(filter(lambda x: x == 0, numbers)))
# positive_numbers = len(list(filter(lambda x: x > 0, numbers)))
#
# print(negative_numbers, zero_numbers, positive_numbers)  # задачка на подсчёт кол-ва типов чисел


# days = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve']
# new_days = list(filter(lambda x: x.startswith('S') or len(x) == 4, days))
# new_days.sort()
#
# for day in new_days:
#     print(day)  # задачка на вывод каждого элемента по условию построчно


# employees = [
#     'Pankratiy', 'Innokentiy', 'Anfisa', 'Yaroslava', 'Veniamin',
#     'Leonti', 'Daniil', 'Mishka', 'Lidochka',
#     'Terenti', 'Vladik', 'Svetka', 'Maks', 'Yura', 'Sergei'
# ]
#
# identifiers = [77, 48, 88, 85, 76, 81, 62, 43, 5, 56, 17, 20, 37, 32, 96]
#
# employees_data = dict(zip(sorted(identifiers), sorted(employees)))
# print(employees_data)  # задачка на соотнесение каждого работника с его идентификатором по возрастанию


# def count_strings(*args):
#     c = 0
#
#     for i in args:
#         if isinstance(i, str):
#             c += 1
#     return c
#
#
# print(count_strings(1, 2, 'hello', [2, 3, 4], True))  # задачка на возврат кол-ва строк


# def find_keys(*args, **kwargs):
#     l = []
#
#     for i in kwargs.items():
#         if isinstance(i[1], (list, tuple)):
#             l.append(i[0])
#     return sorted(l, key=lambda x: x.lower())
#
#
# print(find_keys(t=[4, 5], W=[5, 3], A=(3, 2), a={2, 3}, b=[4]))  # задачка на возврат только списков и кортежей


# string_search_a = input()
# print(any(['A' in string_search_a for i in string_search_a]))  # задачка на проверку буквы А хотя бы в одном слове


# numbers_are_sorted = list(map(int, input().split()))
# print(all(numbers_are_sorted[i] > numbers_are_sorted[i + 1] for i in range(len(numbers_are_sorted) - 1)))  # задачка
# # на проверку на убывание

# string_search_ought = input().lower().split()
# print(any([i.endswith('ought') for i in string_search_ought]))  # задачка на проверку окончания слова на 'ought'


# def myoldfunc(s):
#     l = []
#
#     for char in s:
#         if not s.index(char) % 2:
#             l.append(char.lower())
#         else:
#             l.append(char.upper())
#     return ''.join(l)


# print(myoldfunc('Anthropomorphism'))  # не сработает корректно.
# # index возвращает индекс первого вхождения символа в строке.
# # Если в строке есть повторяющиеся символы, это может привести к неправильному определению четности индекса
#
# def myfunc(s):
#     l = []
#
#     for i in range(len(s)):
#         if not i % 2:
#             l.append(s[i].lower())
#         else:
#             l.append(s[i].upper())
#     return ''.join(l)
# #
# #
# # print(myoldfunc('Anthropomorphism'))  # сработает корректно
