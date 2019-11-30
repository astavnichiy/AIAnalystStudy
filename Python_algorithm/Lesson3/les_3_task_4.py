# 4.	Определить, какое число в массиве встречается чаще всего.


from random import randint
mass1 = [randint(0,12) for i in range(1,randint(1,60))]
print (mass1)

mass2 = []
for i in range(0,max(mass1)+1):
    mass2.append(mass1.count(i))
    
print(mass2)
print('Число, которе встречается чаще всего',mass2.index(max(mass2)))  
