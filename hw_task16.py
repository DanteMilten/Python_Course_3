# '''Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1'''

from random import randint
a = [randint(1, 9) for i in range(int(input('Введите размер массива: ')))]
print(a)
print('Встречается', a.count(int(input('Введите искомое число: '))), 'раз')