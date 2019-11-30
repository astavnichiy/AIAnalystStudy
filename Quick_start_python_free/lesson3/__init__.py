import os
import psutil
import random
import sys

#===============================================================================
# Домашнее задание 3
#===============================================================================

program_name = 'MayneKlyaineProgramma' 
i = 'hello world'
print(program_name)
print(i)

player_name = input("Ваше имя:  ")
print(player_name, ', Добро пожаловать, уважаемый')

main_answer = input('Хочешь поиграть со мной? (Y/N)')

if main_answer =='Y':
    print("Вы хотите напасть на Огра? Он большой и свирепый! (Y/N)")
    answer_ogr_fighting = input()
    if answer_ogr_fighting == 'Y':
        ogr_fighting_result = random.randint(0,1)
        print('Вероятность победы', ogr_fighting_result*100)
        if ogr_fighting_result == 1:
            print('Вы замочили Огра')
        else:
            print('Прощай, нам будет тебя не хватать', program_name)
    else:
        print('Вы сбежали')
elif main_answer =='N':
    print("Тогда придется поработать!")
    print("--------------------------")
    print("|Имя директории (1)")
    print("|Платформа ОС (2)")
    print("|Кодировка файловой системы (3)")
    print("|Логин пользователя (4)")
    print("|Кол-во логических CPU (5)")
    print("|Все меню (9)")
    print("|Выйти (0 или любой другой символ)")
    print("--------------------------")       
    chosen_action_from_os = input("Выбери, какую информацию, Вы бы хотели получить?")
    chosen_action_from_os = int(chosen_action_from_os)
    if chosen_action_from_os == 1:
        print('Имя директории:', os.getcwd())
    elif chosen_action_from_os == 2:
        print('Платформа ОС:', os.name)
    elif chosen_action_from_os == 3:
        print('Кодировка файловой системы:', sys.getfilesystemencoding())
    elif chosen_action_from_os == 4:
        print('Логин пользователя:', os.getlogin())
    elif chosen_action_from_os == 5:
        print('Кол-во логических CP:', os.cpu_count())
    elif chosen_action_from_os == 9:
        print('Все данные:')
        print('Имя директории:', os.getcwd())
        print('Платформа ОС:', os.name)
        print('Кодировка файловой системы:', sys.getfilesystemencoding())
        print('Логин пользователя:', os.getlogin())
        print('Кол-во логических CP:', os.cpu_count())
    else:
        print('Пока!')
elif main_answer =='Q':
    print("Выход")
else:
    print("Неизвестный ввод") 