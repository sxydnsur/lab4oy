from itertools import combinations, groupby

# Задача 1: Кортежи, кортежи, кортежи
# 1.1 Создание кортежа из пользовательского ввода
user_input = input("Введите строку без пробелов: ")
my_tuple = tuple(user_input)
print("Созданный кортеж:", my_tuple)

# 1.2 Преобразование кортежа в строку
my_tuple = ('T', 'h', 'e', 'B', 'i', 'g', 'B', 'e', 'n')
my_string = ''.join(my_tuple)
print("Строка: ", my_string)

# 1.3 Сцепление двух кортежей
tuple_A = (1, 2, 3, 4, 5, 6, 7)
tuple_B = (5, 6, 7, 9, 7, 1, 10, 10)
combined_tuple = tuple_A[:4] + tuple_B[4:]
print(combined_tuple)

# 1.4 Подсчет и создание кортежа с количеством вхождений элементов
my_tuple = (55, 6, 777, 54, 6, 76, 7777, 1, 777, 6)
element_count = {}
for element in my_tuple:
    element_count[element] = element_count.get(element, 0) + 1
result_tuple = tuple((k, v) for k, v in element_count.items())
print("Элементы и их вхождения:", result_tuple)

# 1.5 Создание кортежей для хранения определенных объектов данных
data = (55, 6, 777, 70.0, '7', 'A')
integers = tuple(x for x in data if isinstance(x, int))
floats = tuple(x for x in data if isinstance(x, float))
strings = tuple(x for x in data if isinstance(x, str))
print(integers)
print(floats)
print(strings)

# Задача 2: Множества и множества по comprehensions
# 2.1 Создание множества из пользовательского ввода с использованием множеств comprehensions
user_input = input("Введите строку без пробелов: ")
my_set = {char for char in user_input}
print("Созданное множество:", my_set)

# 2.2 Нахождение разности двух множеств
set_A = {1, 2, 3, 4, 5}
set_B = {5, 7, 8, 9, 2, 10}
difference_set = set_A.difference(set_B)
print(difference_set)

# 2.3 Удаление элементов из множества А, которые также присутствуют в множестве B
set_A = {1, 2, 3, 4, 5}
set_B = {5, 7, 8, 9, 2, 10}
set_A.difference_update(set_B)
print(set_A)

# 2.4 Обновление множеств на основе элементов в множестве C
set_A = {1, 2, 3, 4, 7}
set_B = {8, 7, 9, 4, 2, 0, 10}
set_C = {4, 0, 1}
set_C.update(set_A.intersection(set_C))
set_A.difference_update(set_A.intersection(set_C))
print("Обновленное множество C:", set_C)

# 2.5 Создание списка множеств размером m из комбинаций из надмножества A
A = {1, 2, 3, 4, 5, 6}
n = 3
m = 5
result = [set(combo) for combo in combinations(A, n)][:m]
print(result)

# Задача 3: Группировка данных по производителю
cars_list = [('BMW', 'X6'), ('Toyota', 'Yaris'), ('Fiat', '500'), ('Fiat', 'Panda'), ('Toyota', 'Camry 30')]

sorted_cars = sorted(cars_list, key=lambda x: x[0])
for manufacturer, group in groupby(sorted_cars, key=lambda x: x[0]):
    group_list = list(group)
    count = len(group_list)
    models = [car[1] for car in group_list]
    print(f"{manufacturer} {count} - {', '.join(models)}")
