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
    def going_r(self):
        keys_pressed=key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y >=10:
            self.rect.y-=self.speed
        if keys_pressed[K_DOWN] and self.rect.y <=400:
            self.rect.y+=self.speed
    def going_l(self):
        keys_pressed=key.get_pressed()
        if keys_pressed[K_w] and self.rect.y >=10:
            self.rect.y-=self.speed
        if keys_pressed[K_s] and self.rect.y <=400:
            self.rect.y+=self.speed
#создание переменных
backcground=transform.scale(image.load('back.jpg'),(700,500))
game=True
FPS=60
clock=time.Clock()
player1=Player("bat.png",20,100,5,25,100)
player2=Player("bat.png",650,100,5,25,100)
ball=GameSprite("ball.png",310,210,5,40,40)
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    win.blit(backcground,(0,0))
    player1.reset()
    player2.reset()
    ball.reset()
    player1.going_l()
    player2.going_r()
    display.update()
    clock.tick(FPS)
