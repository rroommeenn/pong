#подключение библиотек
from pygame import *
font.init()
font=font.Font(None,70)
mixer.init()
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
background=transform.scale(image.load("back.jpg"),(700,500))
game=True
FPS=60
clock=time.Clock()
player1=Player("bat.png",20,100,5,25,100)
player2=Player("bat.png",650,100,5,25,100)
ball=GameSprite("ball.png",310,210,5,40,40)
finish=False
ball_speed_x=3
ball_speed_y=3
p1_win=font.render('player1 win',1,(0,255,255))
p2_win=font.render('player2 win',1,(0,255,255))
r1sound=mixer.Sound('rsound1.ogg')
r2sound=mixer.Sound('rsound2.ogg')
wlsound=mixer.Sound('wlsound.ogg')
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        win.blit(background,(0,0))
        player1.reset()
        player2.reset()
        ball.reset()
        if not finish:
            ball.rect.x+=ball_speed_x
            ball.rect.y+=ball_speed_y
        if ball.rect.y>=460 or ball.rect.y<=0:
            ball_speed_y*=-1
            r1sound.play()
        if sprite.collide_rect(player1,ball) or sprite.collide_rect(player2,ball):
            ball_speed_x*=-1
            r2sound.play()
        if ball.rect.x<=0:
            win.blit(p2_win,(350,250))
            finish=True
            wlsound.play()
        if ball.rect.x>=700:
            win.blit(p1_win,(50,250))
            finish=True
            wlsound.play()
        player1.going_l()
        player2.going_r()
        display.update()
        clock.tick(FPS)
    else:
        time.delay(5000)
        player1=Player("bat.png",20,100,5,25,100)
        player2=Player("bat.png",650,100,5,25,100)
        ball=GameSprite("ball.png",310,210,5,40,40)
        finish=False
