from typing import List
import pygame
from random import seed, randint

from .point import Point
from .helpclass import Settings
from .room import Room
from .helpclass import Colors as C
from .helpclass import Cell


class Map:
    # RGBA
    BACKGROUND_COLOR = (200, 50, 10)
    VOID = (150, 150, 150)
    PATH = (20, 150, 30)
    BORDER = (200, 200, 200)

    def __init__(self, columns: int, rows: int):
        seed()
        self._columns = columns
        self._rows = rows
        self._surf = pygame.Surface((columns * Cell.WIDTH, rows * Cell.HEIGHT))
        self._surf.fill(self.BACKGROUND_COLOR)
        self._rect = self._surf.get_rect()
        self._map = {}
        self._rooms = []
        self.clear()

    def add_room(self, room: Room):
        self._rooms.append(room)

    def change_cell(self, point: Point, status: int):
        if not self.in_range(point):
            raise IndexError
        self._map[point.x, point.y] = status

    def clear(self, status=0):
        self._map = {}
        for x in range(self._columns):
            for y in range(self._rows):
                self._map[x, y] = status

    def draw(self):
        self._surf.fill(C.DARK)
        self.draw_grid()
        for room in self._rooms:
            self._surf.blit(room.surface, room.rect)
        pygame.draw.rect(self._surf, 'white', (0, 0, self._columns * Cell.WIDTH-2, self._rows * Cell.HEIGHT-2), 1)
        return self._surf

    def draw_grid(self):
        void = pygame.Surface((Cell.WIDTH, Cell.HEIGHT))
        path = pygame.Surface((Cell.WIDTH, Cell.HEIGHT))
        void.fill(self.VOID)
        path.fill(self.PATH)
        pygame.draw.rect(void, self.BORDER, void.get_rect(), 1)
        pygame.draw.rect(path, self.BORDER, path.get_rect(), 1)
        self._surf.fill(self.BACKGROUND_COLOR)
        for cell in self._map:
            x, y = cell
            x1 = x * Cell.WIDTH
            x2 = Cell.WIDTH
            y1 = y * Cell.HEIGHT
            y2 = Cell.HEIGHT
            if self._map[cell] == 0:
                self._surf.blit(void, ((x1, y1), (x2, y2)))
            else:
                self._surf.blit(path, ((x1, y1), (x2, y2)))
        return self._surf

    @property
    def rect(self):
        return self._rect

    @property
    def surf(self):
        return self._surf

    @property
    def map(self):
        return self._map

    def in_range(self, point: Point):
        height = self._rows
        width = self._columns
        return point.x in range(width) and point.y in range(height)

    def __init_surf(self):
        width = self._columns * Cell.WIDTH
        height = self._rows * Cell.HEIGHT
        self._surf = pygame.Surface((width, height))
        self._surf.fill((200, 50, 10))
        self._rect = self._surf.get_rect()
