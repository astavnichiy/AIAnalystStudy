#В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random
import cProfile
import timeit

# def array(a):
#     array = [random.randint(0, a) for _ in range(a)]
#     mn = 0
#     mx = 0
#     for i, items in enumerate(array):
#         if array[i] < array[mn]:
#             mn = i
#         elif array[i] > array[mx]:
#             mx = i
#     num = array[mn]
#     array[mn] = array[mx]
#     array[mx] = num




# array(100)
# 529 function calls in 0.001 seconds
#100 loops, best of 5: 1.68 msec per loop

# array(1000)
#  5038 function calls in 0.006 seconds
#100 loops, best of 5: 11 msec per loop

# array(10000)
# 56288 function calls in 0.071 seconds
#100 loops, best of 5: 94.4 msec per loop





# def array_1(a):
#     array = [random.randint(0, a) for _ in range(a)]
#
#     mn = min(array)
#     mx = max(array)
#     idx_min = array.index(mn)
#     idx_max = array.index(mx)
#
#
#     array[idx_min], array[idx_max] = array[idx_max], array[idx_min]



#array_1(100)
# 533 function calls in 0.000 seconds
#100 loops, best of 5: 1.5 msec per loop

#array_1(1000)
# 5032 function calls in 0.004 seconds
#100 loops, best of 5: 10.1 msec per loop

#array_1(10000)
# 56314 function calls in 0.054 seconds
#100 loops, best of 5: 100 msec per loop


#
def array_2(a):
    array = [random.randint(0, a) for _ in range(a)]

    mx = 0
    for num in array:
        if num > mx:
            mx = num
    mn = a
    for num in array:
        if num < mn:
            mn = num

    idx_min = array.index(mn)
    idx_max = array.index(mx)

    array[idx_min], array[idx_max] = array[idx_max], array[idx_min]


cProfile.run('array_2(100)')



#array_2(100)
#  538 function calls in 0.000 seconds
#100 loops, best of 5: 1.46 msec per loop

#array_2(1000)
# 5034 function calls in 0.010 seconds
#100 loops, best of 5: 8.77 msec per loop

#array_2(10000)
# 56375 function calls in 0.105 seconds
#100 loops, best of 5: 79.6 msec per loop
