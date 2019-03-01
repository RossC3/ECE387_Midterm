import pygame

import math

import TiltControls


TiltControls.setOrientation(0)

TiltControls.setSensitivity(1,1)
screenWidth = 750
screenHeight = 500

win = pygame.display.set_mode((screenWidth,screenHeight))

pygame.display.set_caption("Demo")


x = 375
y = 440
width = 40
height = 40
vel = 5



run = True


while run:

    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False



    if TiltControls.Right():
        x += vel


    elif TiltControls.Left():
        x -= vel


    if TiltControls.Up():
        y -= vel

    elif TiltControls.Down():
        y += vel

    win.fill((0,0,0))
    pygame.draw.rect(win,(255,0,0), (x,y,width,height))


    pygame.display.update()

pygame.quit()
