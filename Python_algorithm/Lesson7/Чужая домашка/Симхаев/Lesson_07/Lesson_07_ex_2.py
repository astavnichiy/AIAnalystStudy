# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
# промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
from random import randint


def mergesort(array):

    print("Splitting ", array)
    if len(array) > 1:
        mid = len(array)//2
        lefthalf = array[:mid]
        righthalf = array[mid:]

        mergesort(lefthalf)
        mergesort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                array[k] = lefthalf[i]
                i = i+1
            else:
                array[k] = righthalf[j]
                j = j+1
            k = k+1

        while i < len(lefthalf):
            array[k] = lefthalf[i]
            i = i+1
            k = k+1

        while j < len(righthalf):
            array[k] = righthalf[j]
            j = j+1
            k = k+1
    print("Merging ", array)

N = 10
a = []
for i in range(N):
    a.append(randint(0, 49))

mergesort(a)
print(a)
