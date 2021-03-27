
# ASADULLAH PRANTO
# Reg.: 2015331528
# Bresenham's Line Algorithm

import sys, pygame
from pygame import gfxdraw

def bresenhamLineAlgo(x1, y1, x2, y2):

    arrX = []
    arrY = []

    dx = x2 - x1
    dy = y2 - y1
    x, y = x1, y1

    p = 2 * dy - dx

    print('The Points are: ')
    while x <= x2:
        print(f'({x}, {y})'), arrX.append(x), arrY.append(y)
        x += 1
        if p < 0:
            p += 2 * dy
        else:
            p += 2 * dy - 2 * dx
            y += 1

    # Plotting points using pygame
    pygame.init()
    pygame.display.set_caption('Bresenham Line Algorithm')
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


# Driver Program
bresenhamLineAlgo(9, 18, 280, 440)
