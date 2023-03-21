from enum import Enum
from typing import List

from .color import Color


class Settings:
    DIRECTION: List[tuple[int, int]] = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    WINDOW_WIDTH_PX: int = 900
    WINDOW_HEIGHT_PX: int = 600


class Colors:
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 200)
    BORDER = (200, 200, 200)
    DARK = (33, 33, 33)
    DARK_BLUE = (25, 32, 114)
    GREEN = (0, 200, 0)
    PATH = (20, 150, 30)
    RED = (200, 0, 0)
    SKY_BLUE = (35, 85, 225)
    VOID = (150, 150, 150)
    WHITE = (255, 255, 255)


class Cell:
    WIDTH: int = 16
    HEIGHT: int = 16
