#3.	В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.


from random import randint
mass1 = [randint(-10,99) for i in range(1,randint(5,8))]
print (mass1)

max_pos = 0
min_pos = 0
min_znach = 0 

for i in range(0,len(mass1)-1):
    if mass1[max_pos] <= mass1[i+1]:
        max_pos = i+1

    if mass1[min_pos] >= mass1[i+1]:
        min_pos = i+1   

print (max_pos)
print (min_pos)

mass1[max_pos], mass1[min_pos] = mass1[min_pos], mass1[max_pos]

print (mass1)