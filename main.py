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
screen = display.set_mode((win_width,win_height))
display.set_caption('Ping Pong')
bg_color = (28, 193, 235)
screen.fill(bg_color)


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 495:
            self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed 
        if keys[K_DOWN] and self.rect.y < 495:
            self.rect.y += self.speed

class Ball(GameSprite):
    def update(self):
        pass

rocket1 = Player('images/racket.png', 0, 400, 39, 136, 10)
rocket2 = Player('images/racket.png', 660, 400, 39, 136, 10) 
# ball = 

game = True
while game:
    screen.fill(bg_color)

    for e in event.get():
        if e.type == QUIT:
            game = False
            quit()
            sys.exit()

    rocket1.update_l()
    rocket1.draw()

    rocket2.update_r()
    rocket2.draw()

    display.update()
    clock.tick(FPS)