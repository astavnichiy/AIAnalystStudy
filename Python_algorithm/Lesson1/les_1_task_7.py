#===============================================================================
# 7. Определить, является ли год, который ввел пользователь, високосным или не високосным.
#===============================================================================

year = int(input())
if year % 4 != 0:
    print("Обычный год")
elif year % 100 == 0:
    if year % 400 == 0:
        print("Высокосный год")
    else:
        print("Обычный год")
else:
    print("Высокосный год")