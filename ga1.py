import pygame
pygame.init()
canvas=pygame.display.set_mode((1000,1000))
pygame.display.set_caption('Sundaram')
color=(242,200,200)
red=(255,0,0)
black =(0,0,0)
white =(255,255,255)
green =(0,255,0)
canvas.fill(color)  
pygame.draw.polygon(canvas,red,((100,10),(100,100),(10,100),(10,10),(50,50)),12)
#pygame.draw.line(canvas,green,(600,600),(500,500),10)
pygame.draw.lines(canvas,green,(60,60),((500,400),(300,500),(1000,300)),10)
pygame.draw.circle(canvas,green,(600,60),20,10)
pygame.draw.ellipse(canvas,green,((300,300),(300,500)),10)
pygame.draw.arc(canvas,green,((400,60),(500,500)),15,20,10)
pygame.draw.rect(canvas,green,((600,600),(500,50)),10)
pygame.display.update()
