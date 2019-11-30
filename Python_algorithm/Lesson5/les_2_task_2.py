"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры
числа. Например, пользователь ввёл A2 и C4F. Сохранить их как ['A', '2'] и
['C', '4', 'F'] соответственно. Сумма чисел из примера: ['C', 'F', '1'],
произведение - ['7', 'C', '9', 'F', 'E'].
"""
"""
Примечание: Вводить надо посимвольно!
"""

hex_simbols = ['1','2','3','4','5','6','7','8','9','A', 'B', 'C', 'D','E', 'F']



def input_hex (to_string):
    hex_number = []   
    print (to_string)
    while True:
        hex_simbol = input('Введите натуральное число (любое не hex символ закончит ввод):')
        if hex_simbol.upper() in hex_simbols:
            #print (hex_simbol.upper())
            hex_number.append(hex_simbol.upper())
        else:
            break    
    # print (hex_number)
    return hex_number


hex_number1 = input_hex ('Число 1:')
hex_number2 = input_hex ('Число 2:')


#hex_number1 = ['A','1']
#hex_number2 = ['F','9']

#Преобразуем в 10чное
int_number1 = int(''.join(hex_number1), 16)
int_number2 = int(''.join(hex_number2), 16)

#Выполняем функции и переводим в 1ричное
result_sum = hex(int_number1 + int_number2)
result_multiplier = hex(int_number1 * int_number2)  

#Убераем лишнее из результатов
result_sum = result_sum[2:]
result_multiplier = result_multiplier [2:]

#выводим результат 
print ('---------------------')
print ('Сложение: ',list(result_sum))
print ('Умножение: ',list(result_multiplier))


 
    