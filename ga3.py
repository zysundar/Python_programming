import pygame,sys
from pygame.locals import*
pygame.init()
canvas=pygame.display.set_mode((500,500))
pygame.display.set_caption("Mouse Motion")
canvas.fill((242,200,200))
while True:
    for event in pygame.event.get():
        canvas.fill((242,200,200))
        pygame.mouse.set_visible(False)
        if event.type == KEYDOWN :
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type == MOUSEBUTTONUP:
            x=event.pos[0]
            y=event.pos[1]
            pygame.draw.circle(canvas,(255,0,0),(x,y),50,20)
        if event.type == MOUSEMOTION:
            x=event.pos[0]
            y=event.pos[1]
            pygame.draw.rect(canvas,(0,255,0),(x,y,50,100),20)


    pygame.display.update()
