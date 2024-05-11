from pygame import *
import sys
from random import *  
from time import time as timer

font.init()

clock = time.Clock()
FPS = 60

score = 0
lost = 0

win_width = 700
win_height = 500
window = display.set_mode((win_width,win_height))
display.set_caption('Ping Pong')
background = transform.scale(image.load('images/tennis_kort(1)(1).png'),(win_width, win_height))


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 360:
            self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed 
        if keys[K_DOWN] and self.rect.y < 360:
            self.rect.y += self.speed    

racket1 = Player('images/racket.png', 0, 300, 39, 136, 10)
racket2 = Player('images/racket.png', 660, 300, 39, 136, 10) 
ball = GameSprite('images/tenis_ball.png', 0, 0, 50, 50, 3) 

speed_x = 3
speed_y = 3

font1 = font.Font(None, 35)
lose1 = font1.render('PLAYER1 LOSE!', True, (180, 0, 0))
lose2 = font1.render('PLAYER2 LOSE!', True, (180, 0, 0))

game = True
finish = False
while game:
    window.blit(background, (0, 0))

    for e in event.get():
        if e.type == QUIT:
            game = False
            quit()
            sys.exit()

    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
    
    if ball.rect.y > win_height-50 or ball.rect.y < 0:
        speed_y *= -1
    
    if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
        speed_x *= -1

    if ball.rect.x < 0:
        finish = True
        window.blit(lose1, (250, 250))
    if ball.rect.x > 650:
        finish = True
        window.blit(lose2, (250, 250))

    racket1.update_l()
    racket1.draw()

    racket2.update_r()
    racket2.draw()

    ball.draw()

    display.update()
    clock.tick(FPS)
