#подключение библиотек
from pygame import *
mixer.init()
font.init()
font=font.Font(None,35)
from random import*
from time import time as timer
#создание окна
win=display.set_mode((700,500))
display.set_caption('pong')
#создание классов
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,x,y,speed,x_size,y_size):
        super().__init__()
        self.image=transform.scale(image.load(player_image),(x_size,y_size))
        self.speed=speed
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
    def reset(self):
        win.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def going(self):
        keys_pressed=key.get_pressed()
        if keys_pressed[K_DOWN] and self.rect.y >=10:
            self.rect.x-=self.speed
        if keys_pressed[K_UP] and self.rect.x <=650:
            self.rect.x+=self.speed
#создание переменных
backcground=transform.scale(image.load('back.jpg'),(700,500))
game=True
FPS=60
clock=time.Clock()
while game:
    win.blit(backcground,(0,0))
    display.update()
    clock.tick(FPS)