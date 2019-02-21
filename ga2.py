import pygame,sys
from pygame.locals import*
pygame.init()
canvas=pygame.display.set_mode((1000,1000))
pygame.display.set_caption("Game_start")
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
pink=(242,200,200)
canvas.fill(pink)
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_TAB:
                pygame.quit()
                sys.exit()
    
    
