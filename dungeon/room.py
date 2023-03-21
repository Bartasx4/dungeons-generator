import pygame

from .point import Point
from .color import Color
from .helpclass import Colors as C
from .helpclass import Settings
from .helpclass import Cell


class Room:
    _point: Point
    _width: int
    _height: int

    def __init__(self, point: Point, width: int, height: int):
        self._point = point
        self._width = width
        self._height = height
        self._surface = None
        self.draw()

    @staticmethod
    def is_overlapping(self, other):
        min1 = Point(self.x, self.y)
        max1 = Point(self.x2, self.y2)
        min2 = Point(other.x, other.y)
        max2 = Point(other.x2, other.y2)
        if (min1.x <= max2.x and max1.x >= min2.x) and (min1.y <= max2.y and max1.y >= min2.y):
            return True
        return False

    def draw(self):
        self._surface = pygame.Surface((self._width * Cell.WIDTH,
                                        self._height * Cell.HEIGHT))
        self._surface.fill(C.WHITE)
        void = pygame.Surface((Cell.WIDTH, Cell.HEIGHT))
        void.fill((57, 105, 114))
        pygame.draw.rect(void, (0, 32, 114), (0, 0, Cell.WIDTH, Cell.HEIGHT), 1)
        for width in range(self.width):
            for height in range(self.height):
                x, y = width, height
                x1 = x * Cell.WIDTH
                x2 = Cell.WIDTH
                y1 = y * Cell.HEIGHT
                y2 = Cell.HEIGHT
                self._surface.blit(void, ((x1, y1), (x2, y2)))
        pygame.draw.rect(self._surface, (0, 107, 157), self._surface.get_rect(), 4)
        return self._surface

    @property
    def surface(self) -> pygame.Surface:
        return self._surface

    @property
    def x(self):
        return self._point.x

    @property
    def y(self):
        return self._point.y

    @property
    def x2(self):
        return self._point.x + self._width

    @property
    def y2(self):
        return self._point.y + self._height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def rect(self):
        return self.x, self.y, self.width, self.height
