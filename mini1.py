import pygame,sys
from pygame.locals import *
pygame.init()
fps =50
speed = 30
font = pygame.font.SysFont(None, 25)
mainClock = pygame.time.Clock()
Canvas = pygame.display.set_mode((1000,1000))
pygame.display.set_caption('Mini Project')
ball_image = pygame.image.load('ball1.jpg')
ball_rect = ball_image.get_rect()
pygame.mixer.music.load('Faded - Alan Walker-freeringtonesdownload.info.mp3')

while True:
    moveup = movedown = moveright = moveleft = False
    ball_rect.centerx = 300
    ball_rect.centery = 200    
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN: 
                if event.key == K_UP:
                    moveup = True                    
                if event.key == K_DOWN:
                    movedown = True
                if event.key == K_LEFT:
                    moveleft = True
                if event.key == K_RIGHT:
                    moveright = True
            if event.type == KEYUP:
                if event.key == K_UP:
                    moveup = False
                    pygame.mixer.music.play(2, 10000)
                if event.key == K_DOWN:
                    movedown = False
                    pygame.mixer.music.stop()
                if event.key == K_LEFT:
                    moveleft = False
                if event.key == K_RIGHT:
                    moveright = False
        if (moveup and (ball_rect.top > 0)):
            ball_rect.top-= speed
        if (movedown and (ball_rect.bottom < 1000)):
            ball_rect.bottom += speed
        if (moveleft and (ball_rect.left > 0)):
            ball_rect.left -= speed
        if (moveright and (ball_rect.right < 1000)):
                ball_rect.right += speed
        x = str(ball_rect.centerx)
        y = str(ball_rect.centery)
        x1 = font.render(x, 1, (0,255,0))
        y1 = font.render(y, 1, (255,0,0))
        rect_x = x1.get_rect()
        rect_y = y1.get_rect()
        rect_x.topleft = (10, 10)
        rect_y.topleft = (50, 10)
        Canvas.fill((255,255,255))
        Canvas.blit(x1, rect_x)
        Canvas.blit(y1, rect_y)
        Canvas.blit(ball_image, ball_rect)
        pygame.display.update()
        mainClock.tick(fps)
