import timeit

#Проанализировать скорость и сложность одного любого алгоритма,
#разработанных в рамках домашнего задания первых трех уроков.

#Алгоритм: Сформировать из введенного числа обратное по порядку входящих в него
#цифр и вывести на экран. Например, если введено число 3486,
#то надо вывести число 6843.



def my_slice(a):
    return a[::-1]


def my_reverse(a):
    a = list(a)
    i, j = 0, len(a) - 1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    return "".join(a)


def my_recursion(a):
    if len(a) == 1:
        return a
    else:
        return a[-1] + my_recursion(a[:-1])


a = "1234567890"

print(timeit.timeit("my_slice(a)", setup="from __main__ import my_slice, a", number=10000))
print(timeit.timeit("my_reverse(a)", setup="from __main__ import my_reverse, a", number=10000))
print(timeit.timeit("my_recursion(a)", setup="from __main__ import my_recursion, a", number=10000))


#1. Измерение времени работы с использованием timeit:
#my_slice(): 0.0028080249999999987
#my_reverse(): 0.029595101999999998
#my_recursion(): 0.053995769999999985
#2. Оценка сложности алгоритма:
#my_slice(): O(n) - быстродействие функции прямо пропорционально входному значению n; самый выгодный алгоритм, т. к.
#не используется видимый цикл
#my_reverse(): O(n) - быстродействие функции прямо пропорционально входному значению n; чем больше n, тем больше
#итераций цикла
#my_recursion(): O(n) - быстродействие функции прямо пропорционально входному значению n; чем больше n, тем больше
#раз функция вызовет сама себя

