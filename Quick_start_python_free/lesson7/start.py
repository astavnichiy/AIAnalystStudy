import random
import turtle

answer = ''
while answer != 'N':
    answer = turtle.textinput("Нарисовать окружность?", "Y|N")
    if answer == 'Y':
 #       turtle.screen()
        turtle.pencolor("red")
        turtle.circle(random.randrange(20,100))
        turtle.bgpic("sky.gif")
    else:
        pass