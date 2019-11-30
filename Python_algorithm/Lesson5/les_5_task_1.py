"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""
from random import randint
import collections

COMP_LIST = ['Российский алюминий',
             'УГМК',
             'ГК «ТАИФ»',
             'Металлоинвест',
             'Группа ГАЗ',
             'Русснефть',
             'МегаФон',
             'Эльдорадо (сеть магазинов)',
             'Евросеть',
             'Объединенная металлургическая компания'] 

# Ввод кол-ва предприятий
def num_of_comp ():
    try:
        number1 = int(input('Введите число предприятий (хоть 1000):'))
        return number1
    except:
        print ('Ввел неверно. Будет 5')
        return 5

# просто линия для читаемости
def print_line ():
    print('------------------')


#Создание namedtuple
Company = collections.namedtuple('Company', ['name', 'q_1', 'q_2','q_3', 'q_4'])
 
comp_number = num_of_comp ()
print_line ()
# Создание списка предприятий. Не хочу руками вводить. Будет генератор.    
Companies = []
for i in range(0,int(comp_number)):
    comp_name = COMP_LIST[randint(0,len(COMP_LIST)-1)]
    p = Company(comp_name,randint(0,100), randint(0,100), randint(0,100),randint(0,100))    
    
    # вывод на экран результатов генерации
    print(p)
    Companies.append(p)

print_line ()
    
middle_profit = 0

# высчитываем среднюю для всех компаний
for Company in Companies:
    middle_profit += Company[1]+Company[2]+Company[3]+Company[4]

middle_profit1 = middle_profit / int(comp_number)
print('Средняя:', middle_profit1)

#Выводим компании больше и меньше средней 

print_line ()

for Company in Companies:
    if Company[1]+Company[2]+Company[3]+Company[4] > middle_profit1:
        print('Компания выше среднего:', Company[0])

print_line ()

for Company in Companies:    
    if Company[1]+Company[2]+Company[3]+Company[4] < middle_profit1:
        print('Компания ниже среднего:', Company[0])        
     
