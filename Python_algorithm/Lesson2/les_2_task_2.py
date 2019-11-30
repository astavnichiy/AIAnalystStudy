"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
"""

number2 = input('Введите натуральное число:')    

chet = 0
nechet = 0

try:
    int(number2)

except:
    print ('Хреновое число')
    
for i in range(0,len(number2)):
    print (number2[i])
    if int(number2[i]) % 2 == 0:
        chet += 1
    else:
        nechet += 1        
print('Четное =', chet)
print('Нечетное =', nechet) 