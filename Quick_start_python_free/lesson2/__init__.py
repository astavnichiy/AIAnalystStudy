import random

program_name = 'MayneKlyaineProgramma' 
i = 'hello world'
print(program_name)
print(i)

player_name = input("Ваше имя:  ")
print(player_name, ', Добро пожаловать, уважаемый')

main_answer = input('Вы любите текстовые квесты? (Y/N)')

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
    print("Досвидания,", program_name, "!")
elif main_answer =='Q':
    print("Выход")
else:
    print("Неизвестный ввод") 