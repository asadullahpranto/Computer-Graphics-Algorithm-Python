
# ASADULLAH PRANTO
# Reg.: 2015331528
# Bresenham's Circle Algorithm

import pygame, sys
from pygame import gfxdraw

pygame.init()
pygame.display.set_caption('Bresenham Line Algorithm')
screen = pygame.display.set_mode((600, 400))
screen.fill((0, 0, 0))
pygame.display.flip()
white = (255, 255, 0)

arrX = []
arrY = []

def octatePoints(xc, yc, x, y):
    print(xc + x, yc + y), arrX.append(xc + x), arrY.append(yc + y)
    print(xc - x, yc + y), arrX.append(xc - x), arrY.append(yc + y)
    print(xc + x, yc - y), arrX.append(xc + x), arrY.append(yc - y)
    print(xc - x, yc - y), arrX.append(xc - x), arrY.append(yc - y)
    print(xc + y, yc + x), arrX.append(xc + y), arrY.append(yc + x)
    print(xc - y, yc + x), arrX.append(xc - y), arrY.append(yc + x)
    print(xc + y, yc - x), arrX.append(xc + y), arrY.append(yc - x)
    print(xc - y, yc - x), arrX.append(xc - y), arrY.append(yc - x)

def bresenhamsCircleAlgo(xc, yc, r):
    x = 0
    y = r
    d = 3 - 2 * r
    print()

    while x <= y:
        x += 1

        if d > 0:
            y -= 1
            d += 4 * (x - y) + 10
        else:
            d += 4 * x + 6
        octatePoints(xc, yc, x, y)

    # Plotting points using pygame
    pygame.init()
    pygame.display.set_caption('Bresenham Circle Algorithm')
    screen = pygame.display.set_mode((600, 400))
    screen.fill((0, 0, 0))
    pygame.display.flip()

    yellow = (255, 255, 0)
    for i in range(len(arrX)):
        gfxdraw.pixel(screen, arrX[i], arrY[i], yellow)

    pygame.display.flip()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

bresenhamsCircleAlgo(50, 50, 30)

pygame.display.flip()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
