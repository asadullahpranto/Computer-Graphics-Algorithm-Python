
# ASADULLAH PRANTO
# Reg.: 2015331528
# Midpoint Circle Algorithm

import sys, pygame
from pygame import gfxdraw

def midPointCircle(xc, yc, r):

    arrX = [] # for storing x coordinates
    arrY = [] # for storing y coordinates

    x = r
    y = 0
    print(f'({x + xc}, {y + yc})', end=', '), arrX.append(x + xc), arrY.append(y + yc)

    if r > 0:
        print(f'({x + xc}, {-y + yc})', end=', '), arrX.append(x + xc), arrY.append(-y + yc)
        print(f'({y + xc}, {x + yc})', end=', '), arrX.append(y + xc), arrY.append(x + yc)
        print(f'({-y + xc}, {x + yc})', end='\n'), arrX.append(-y + xc), arrY.append(x + yc)

    p = 1 - r

    while x > y:
        y += 1
        if p <= 0:
            p += 2 * y + 1
        else:
            x -= 1
            p += 2 * y - 2 * x + 1

        print(f'({x + xc}, {y + yc})', end=', '), arrX.append(x + xc), arrY.append(y + yc)
        print(f'({-x + xc}, {y + yc})', end=', '), arrX.append(-x + xc), arrY.append(y + yc)
        print(f'({x + xc}, {-y + yc})', end=', '), arrX.append(x + xc), arrY.append(-y + yc)
        print(f'({-x + xc}, {-y + yc})', end='\n'), arrX.append(-x + xc), arrY.append(-y + yc)

        if x!= y:
            print(f'({y + xc}, {x + yc})', end=''), arrX.append(y + xc), arrY.append(x + yc)
            print(f'({-y + xc}, {x + yc})', end=', '), arrX.append(-y + xc), arrY.append(x + yc)
            print(f'({y + xc}, {-x + yc})', end=', '), arrX.append(y + xc), arrY.append(-x + yc)
            print(f'({-y + xc}, {-x + yc})', end=',\n'), arrX.append(-y + xc), arrY.append(-x + yc)

    # Plotting points using pygame
    pygame.init()
    pygame.display.set_caption('Midpoint Circle Algorithm')
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

print('The coordinates are: ')
midPointCircle(60, 60, 50)