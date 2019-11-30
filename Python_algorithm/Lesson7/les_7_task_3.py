"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
 который не рассматривался на уроках
"""
from random import randint
import threading
from statistics import median


def sort (massiv, mediana, direction):
    new_mass=[]
    
    for i in range (0, len(massiv)):
        if direction == "up":
            if massiv[i] >= mediana:
                new_mass.append(massiv[i])
        else:
            if massiv[i] < mediana:
                new_mass.append(massiv[i])
    
    print (new_mass)


massiv = [randint(-100,100) for i in range(1,22)]
print(massiv)
#mediana = (max(massiv) + min(massiv))//2        
#print(max(massiv))
#print(min(massiv))

mediana = median(massiv)
print (mediana)

threading.Thread(target = sort, args = (massiv, mediana,"up")).start()
threading.Thread(target = sort, args = (massiv, mediana,"")).start()





