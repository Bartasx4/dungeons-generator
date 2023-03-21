from random import randint, seed


class Point:
    x: int
    y: int

    def __init__(self, x: int, y: int):
        seed()
        self.x = x
        self.y = y

    def copy(self):
        return Point(self.x, self.y)

    @staticmethod
    def random(width=None, height=None):
        x = None
        y = None
        if isinstance(width, int) and isinstance(height, int):
            x = randint(0, width - 1)
            y = randint(0, height - 1)
        elif isinstance(width, tuple) and isinstance(height, tuple):
            x = randint(width[0], width[1]-1)
            y = randint(height[0], height[1]-1)
        elif isinstance(width, tuple) and height is None:
            x = isinstance(width[0], width[1]-1)
            y = isinstance(width[0], width[1]-1)
        elif isinstance(width, int) and height is None:
            x = randint(0, width-1)
            y = randint(0, width-1)
        elif width is None and height is None:
            x = randint(0, 100)
            y = randint(0, 100)
        else:
            raise TypeError()
        return Point(x, y)

    def __add__(self, other: tuple):
        point = self.copy()
        if isinstance(other, Point):
            point.x += other.x
            point.y += other.y
        if isinstance(other, tuple):
            point.x += other[0]
            point.y += other[1]
        if isinstance(other, int):
            point.x += other
            point.y += other
        return point

    def __call__(self, *args, **kwargs):
        return self

    def __iter__(self):
        return iter((self.x, self.y))

    def __repr__(self):
        return f'(x: {self.x}, y: {self.y})'

    def __str__(self):
        return f'(x: {self.x}, y: {self.y})'
