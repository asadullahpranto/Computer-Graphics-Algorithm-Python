
# ASADULLAH PRANTO
# Reg.: 2015331528
# Z-Buffer Algorithm

import json
import sys
from pprint import pprint

class Color:
    def __init__(self, r=0, g=0, b=0):
        self.r = self._checkValue(r)
        self.g = self._checkValue(g)
        self.b = self._checkValue(b)

    def get(self):
        return (self.r, self.g, self.b)

    def _checkValue(self, val):
        return 0 if val < 0 else 255 if val > 255 else val

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"Color (r={self.r}, g={self.g}, b={self.b})"


class Vector3:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def isCloserThan(self, z):
        return self.z < z

    def getXY(self):
        return (self.x, self.y)

    @staticmethod
    def subdivideRegion(begin, end):
        return [
            (
                Vector3(begin.x, begin.y, begin.z),
                Vector3(end.x // 2, end.y // 2, end.z),
            ),
            (
                Vector3((begin.x + end.x) // 2 + 1, begin.y, begin.z),
                Vector3(end.x, end.y // 2, end.z),
            ),
            (
                Vector3(begin.x, (begin.y + end.y) // 2 + 1, begin.z),
                Vector3(end.x // 2, end.y, end.z),
            ),
            (
                Vector3(
                    (begin.x + end.x) // 2 + 1, (begin.y + end.y) // 2 + 1, begin.z
                ),
                Vector3(end.x, end.y, end.z),
            ),
        ]

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"Vector3: (x={self.x}, y={self.y}, z={self.z})"


def zbuffer(polygons, screen):
    for polygon in polygons:
        for pixel in polygon["pixels"]:
            position = Vector3(*pixel["position"])
            if position.isCloserThan(screen[position.x][position.y][1]):
                screen[position.x][position.y] = (
                    Color(*pixel["color"]),
                    position.z,
                    screen[position.x][position.y][2],
                )

    return screen


WIDTH = 5  # for testing purposes
HEIGHT = 5

DEFAULT_COLOR = Color()  # default is black (0, 0, 0)
DEFAULT_DEPTH = float("Inf")


def loadPolygons():
    with open("polygons.json", "r") as file:
        data = json.load(file)

    return data["polygons"]


screen = [
    [(DEFAULT_COLOR, DEFAULT_DEPTH, f"x={row}, y={column}") for column in range(WIDTH)]
    for row in range(HEIGHT)
]


def printScreen():
    print("current screen:")
    pprint(screen)
    print("-------------------------------------------")


polygons = loadPolygons()
printScreen()


def render(renderFunction, polygons, screen):
    return renderFunction(polygons, screen)


screen = render(zbuffer, polygons, screen)

printScreen()