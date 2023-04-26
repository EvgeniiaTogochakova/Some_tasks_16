# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# Пример:
# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# Диапазон от 6 до 12
# Вывод: [1, 9, 13, 14, 19]

from random import randint

minny = int(input('Укажите минимальное число, которое может использоваться для генерации списка: '))
maxxy = int(input('Укажите максимальное число, которое может использоваться для генерации списка: '))
print(list_n := [randint(minny, maxxy) for _ in range(int(input('Сколько чисел в списке? ')))])
range_min = int(input('Значение нижней границы диапазона поиска: '))
range_max = int(input('Значение верхней границы диапазона поиска: '))
list_indexes = list()
for i in range(len(list_n)):
    if list_n[i] >= range_min and list_n[i] <= range_max:
        list_indexes.append(i)
print('Вывожу перечень индексов: ', list_indexes)