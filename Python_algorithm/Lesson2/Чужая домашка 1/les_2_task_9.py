# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

def sum_func(number, digit_sum=0):
    if number > 0:
        digit_sum += number%10
        return sum_func(number//10, digit_sum)
    return digit_sum


def func(n, max_sum=0, output_number=0):
    if n > 0:
        number = int(input("Введите любое натуральное число: "))
        digit_sum = sum_func(number)
        if digit_sum > max_sum:
            max_sum = digit_sum
            output_number = number
        return func(n-1, max_sum, output_number)
    print(f"Число: {output_number}")
    print(f"Максимальная сумма цифр: {max_sum}")

func(3)

