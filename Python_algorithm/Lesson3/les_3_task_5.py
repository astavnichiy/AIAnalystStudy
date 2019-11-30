#5.	В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.


from random import randint
mass1 = [randint(-12,12) for i in range(0,randint(1,10))]
print (mass1)

mass2 = []
i_mass = 0

for i in range (0, len(mass1)):
    if mass1[i] < 0:
        mass2.append(mass1[i])
        i_mass = i
        
print (max(mass2), i_mass + 1)