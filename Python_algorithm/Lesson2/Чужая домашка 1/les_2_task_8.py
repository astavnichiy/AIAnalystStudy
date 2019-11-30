# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

def func(number, digit, counter=0):
    if number > 0:
        if number%10 == digit:
            counter += 1
        return func(number//10, digit, counter)
    else:
        if number == digit:
            counter += 1
        return counter


n = int(input("Введите количество натуральных чисел: "))
digit = int(input("Введите искомую цифру: "))
counter = 0
for i in range(n):
    number = int(input("Введите натуральное число: "))
    counter = func(number, digit, counter)
print(f"Частота искомой цифры: {counter}")

