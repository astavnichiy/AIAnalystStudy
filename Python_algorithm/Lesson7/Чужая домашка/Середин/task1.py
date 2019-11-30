# Задание:
# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на промежутке
# [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Примечания:
# a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком. Улучшенные версии
# сортировки, например, расчёской, шейкерная и другие в зачёт не идут.

import random

size = 10

array = [i for i in range(-100, 100)]
random.shuffle(array)
print(array)

# МОДИФИКАЦИЯ: разделим массив на значения < 0, = 0 и > 0
min_list = []
zero_list = []
max_list = []

def puzyrek(list):
    n = 1
    while n < len(list):
        for i in range(len(list) - n):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
        n += 1
    print(f'Итог: {list}')
    return list


for num in array:
    if num > 0:
        max_list.append(num)
    if num == 0:
        zero_list.append(num)
    if num < 0:
        min_list.append(num)
    print(num)

min_list_new = puzyrek(min_list)
zero_list_new = puzyrek(zero_list)
max_list_new = puzyrek(max_list)

total_array = min_list_new + zero_list_new + max_list_new

print(total_array)