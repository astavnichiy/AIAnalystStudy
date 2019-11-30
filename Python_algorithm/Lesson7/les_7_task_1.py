"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""

from random import randint

def bsort (a):
    for i in range(int(len(a))-1):
        for j in range(int(len(a))-1 -i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
            if a[j] == a[j+1]:
                continue
    return a


massiv = [randint(-100,100) for i in range(1,50)]
print(massiv)

massiv = bsort (massiv)
print(massiv)