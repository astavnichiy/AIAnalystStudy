import os
import psutil
import random
import sys
import shutil


#===============================================================================
# Домашнее задание 5 - Не закончено
#===============================================================================


def sys_info():
    # Информация о системе
    print("актуальное имя:", os.getlogin())
    print("система:", sys.platform)
    print("текущая директория:", os.getcwd())
    print("файловая система:", sys.getfilesystemencoding())
    print("CPU:", psutil.cpu_count())


def duplicate_file(file_name):
    if os.path.isfile(file_name):
        newfile = file_name + '.dupl'
        shutil.copy(file_name, newfile)
        if os.path.exists(newfile):
            print("файл скопирован успешно:", newfile)
            return True 
        else:
            print("Что-то пошло не так с копирование этого файла:", file_name)
            return False
    return 0
    
    
def delete_file(file_list):    
    # Функция удаления дубликатов 
    k = 0
    for file_name in file_list:
        fullname = os.path.join(dirname, file_name)
        if fullname.endswith('.dupl'):
            os.remove(fullname)
            k += 1
        else:
            pass
    return k

def main():
    program_name = 'MayneKlyaineProgramma'
    # Основная часть программы 
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
        print("1 - вывести список файлов")
        print("2 - сведения о системе")
        print("3 - дублирование")
        print("4 - дублирование конкретного файла ")
        print("5 - удаление дубликатов")
        print("6 - ")
        do = int(input("выбор действия:"))
        if do == 1:
            print(os.listdir())
            
        elif do == 2:
            sys_info()
            
        elif do == 3:
            print("дублирование файлов:")
            file_list = os.listdir()
            i = 0
            while i < len(file_list):
                duplicate_file(file_list[i])   
                i += 1
                    
        elif do == 4:
            print("дублирование конкретного файла:")
            filename = input("введите имя файла:")
            if os.path.isfile(filename):
                newfile = filename + '.dupl'
                shutil.copy(filename, newfile)
                
        elif do == 5:
            print("удаление")
            dirname = input("укажите имя директории:")
            file_list = os.listdir(dirname)
            print(file_list)
            print("Удалено файлов:", delete_file(file_list))
            
        else:
            print('Пока!')
    elif main_answer =='Q':
        print("Выход")
    else:
        print("Неизвестный ввод") 
        
if __name__ == "__main__":
    main()