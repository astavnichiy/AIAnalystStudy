"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
"""
from random import randint

def bsort (seq):
    """Accepts a mutable sequence. Utilizes merge_sort to sort in place, return
    a sorted sequence"""
    if len(seq) == 1:
        return seq
    else:
        mid = int(len(seq)//2)
        left = bsort(seq[:mid])
        right = bsort(seq[mid:])

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):

            if left[i] < right[j]:
                seq[k] = left[i]
                i += 1; k += 1
            else:
                seq[k] = right[j]
                j += 1; k += 1

        remaining = left if i < j else right
        r = i if remaining == left else j

        while r < len(remaining):
            seq[k] = remaining[r]
            r += 1; k += 1

        return seq


massiv = [randint(-100,100) for i in range(1,50)]
print(massiv)

massiv = bsort (massiv)
print(massiv)