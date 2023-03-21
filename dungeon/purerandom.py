from random import randint, seed
from typing import List

from .helpclass import Settings
from .point import Point
from .map import Map


class Purerandom:

    def __init__(self, width: int, height: int):
        seed()
        self._height = height  # Cells rows
        self._width = width  # Cell columns
        self._map = Map(width, height)

    def create_maze(self,
                    start_point: Point = None,
                    steps: int = 200,
                    visited_status: int = 1,
                    skip_overrange: int = False,
                    step_by_step: bool = False):

        def make_step():
            step = 0
            nonlocal point
            while step < steps:
                new_point = point + Settings.DIRECTION[randint(0, 3)]
                if self._map.in_range(new_point):
                    point = new_point
                    self._map.change_cell(point, visited_status)
                elif not skip_overrange:
                    continue
                step += 1
                yield point

        point = start_point if start_point else Point.random(self._width, self._height)
        self._map.change_cell(point, visited_status)
        if step_by_step:
            return make_step
        for _ in make_step():
            continue

    @property
    def map(self):
        return self._map

    @staticmethod
    def __make_step(point: Point):
        return point + Settings.DIRECTION[randint(0, 4)]
