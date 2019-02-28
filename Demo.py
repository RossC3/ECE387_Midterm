import pygame

import math

import TiltControls


TiltControls.setOrientation(0)


screenWidth = 750
screenHeight = 500

win = pygame.display.set_mode((screenWidth,screenHeight))

pygame.display.set_caption("Demo")


x = 375
y = 440
width = 40
height = 40
vel = 5



run = true


while run:

    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type = pygame.QUIT:
            run = False



    if TiltControls.moveRight():

        if

