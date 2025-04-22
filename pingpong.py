from pygame import *
from random import *

run = True


window = display.set_mode((700,500))#Создание окна приложения
display.set_caption('Пингпонг')#Заголовок
window.fill((12,211,242))

while run:#Игровойцикл
    for e in event.get():
        if e.type == QUIT:
            run == False
        elif e.type == KEYDOWN:
            if e.key == K_r:
                reset_game()

        
    display.update()

