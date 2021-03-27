
# ASADULLAH PRANTO
# Reg.: 2015331528
# DDA Algorithm

import sys, pygame
from pygame import gfxdraw

# DDA Algorithm
def ddaAlgo(x1, y1, x2, y2):

    arrX = []
    arrY = []

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    step = max(dx, dy)

    xinc = dx / float(step)
    yinc = dy / float(step)

    x, y = x1, y1

    arrX.append(round(x))
    arrY.append(round(y))

    print(f'The points are:\n({round(x)}, {round(y)})')

    while x <= step:
        x += xinc
        y += yinc
        print(f"({round(x)}, {round(y)})")

        arrX.append(round(x))
        arrY.append(round(y))

    # Plotting points using pygame
    pygame.init()
    pygame.display.set_caption('DDA Algorithm')
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
#x1, y1 = map(int, input('Enter the value of x1 and y1 and press Enter: ').split())
#x2, y2 = map(int, input('Enter the value of x2 and y2 and press Enter: ').split())

ddaAlgo(50, 50, 350, 350)

