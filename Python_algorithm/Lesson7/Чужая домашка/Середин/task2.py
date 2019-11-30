# ЗАДАНИЕ:
# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке
# [0; 50). Выведите на экран исходный и отсортированный массивы.

import random

array = [i for i in range(0,50)]
random.shuffle(array)
print(f'Начальный результат:{array}')
n = 1


def sliyanie(list):
    if len(list)>1:
        mid = len(list)//2
        left_half = list[:mid]
        right_half = list[mid:]

        sliyanie(left_half)
        sliyanie(right_half)

        i=0
        j=0
        k=0
        while i<len(left_half) and j<len(right_half):
            if left_half[i]<right_half[j]:
                list[k]=left_half[i]
                i=i+1
            else:
                list[k]=right_half[j]
                j=j+1
            k=k+1

        while i<len(left_half):
            list[k]=left_half[i]
            i=i+1
            k=k+1

        while j<len(right_half):
            list[k]=right_half[j]
            j=j+1
            k=k+1
    return list

print(f'Итоговый результат:{sliyanie(array)}')