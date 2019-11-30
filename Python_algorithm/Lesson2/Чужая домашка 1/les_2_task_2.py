# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

def func(number, even_counter=0, odd_counter=0):
    if number > 0:
        if number%10%2 ==0:
            even_counter += 1
        else:
            odd_counter += 1
        return func(number//10, even_counter, odd_counter)
    print(f"Количество четных чисел: {even_counter}")
    print(f"Количество нечетных чисел: {odd_counter}")


number = int(input("Введите любое натуральное число: "))
if number == 0:
    print("Количество четных чисел: 1")
    print("Количество нечетных чисел: 0")
else:
    func(number)

