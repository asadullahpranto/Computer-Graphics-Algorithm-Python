
# ASADULLAH PRANTO
# Reg.: 2015331528
# Midpoint Ellipse Algorithm

import sys, pygame
from pygame import gfxdraw

def midPointEllipseAlgo(rx, ry, xc, yc):

    arrX = [] # for storing x coordinates
    arrY = [] # for storing y coordinates

    x = 0
    y = ry

    d1 = (ry * ry) - (rx * rx *ry) + (0.25 * rx * rx)

    dx = 2 * ry * ry * x
    dy = 2 * rx * rx * y

    while dx < dy:
        print(f'({x + xc}, {y + yc})'), arrX.append(x + xc), arrY.append(y + yc)
        print(f'({-x + xc}, {y + yc})'), arrX.append(-x + xc), arrY.append(y + yc)
        print(f'({x + xc}, {-y + yc})'), arrX.append(x + xc), arrY.append(-y + yc)
        print(f'({-x + xc}, {-y + yc})'), arrX.append(-x + xc), arrY.append(-y + yc)

        if d1 < 0:
            x += 1
            dx = dx + 2 * ry * ry
            d1 = d1 + dx + ry * ry
        else:
            x += 1
            y -= 1
            dx = dx + 2 * ry * ry
            dy = dy - 2 * rx * rx
            d1 = d1 + dx - dy + ry * ry

    d2 = (ry * ry) * (x + 0.5) * ( x + 0.5) + (rx * rx) * (y - 1) * (y - 1) - (rx * rx * ry * ry)

    while y >= 0:
        print(f'({x + xc}, {y + yc})'), arrX.append(x + xc), arrY.append(y + yc)
        print(f'({-x + xc}, {y + yc})'), arrX.append(-x + xc), arrY.append(y + yc)
        print(f'({x + xc}, {-y + yc})'), arrX.append(x + xc), arrY.append(-y + yc)
        print(f'({-x + xc}, {-y + yc})'), arrX.append(-x + xc), arrY.append(-y + yc)

        if d2 > 0:
            y -= 1
            dy -= 2 * rx * rx
            d2 += rx * rx - dy
        else:
            y -= 1
            x += 1
            dx += 2 * ry * ry
            dy -= 2 * rx * rx
            d2 += dx - dy + rx * rx;


    # Plotting points using pygame
    pygame.init()
    pygame.display.set_caption('Midpoint Ellipse Algorithm')
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
print('The coordinates are: ')

midPointEllipseAlgo(35, 60, 80, 100)