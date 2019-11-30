# ЗАДАНИЕ:
# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше
# медианы, в другой — не больше медианы. Примечание: задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, используйте метод сортировки, который не рассматривался на уроках
# (сортировка слиянием также недопустима).

import random

size = int(input('Введите размерность массива'))

if size % 2 == 0:
    size+=1
    print(f'Приводим массив к виду 2m+1. Размер стал {size}')

array = [i for i in range(size)]
random.shuffle(array)
print(array)

# за основу был взят алгоритм сортировки "Перемешиванием" ака Cocktail sort

def peremeshivanie(array):
    levo = 0
    pravo = len(array) - 1
    while levo <= pravo:
        # правый край
        for i in range(levo, pravo, +1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        pravo -= 1
        # левый край
        for i in range(pravo, levo, -1):
            if array[i - 1] > array[i]:
                array[i], array[i - 1] = array[i - 1], array[i]
        levo += 1
    print(array)
    return array

peremeshivanie(array)
index = round(len(array) / 2)
mean = array[index]
print(mean)