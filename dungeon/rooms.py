from random import seed, randint

from .point import Point
from .map import Map
from .helpclass import Settings
from .room import Room


class Rooms:

    def __init__(self,
                 map_width: int,
                 map_height: int,
                 rooms_count: tuple = (3, 7),
                 room_width: tuple = (5, 15),
                 room_height: tuple = (6, 11)):
        seed()
        self._width = map_width
        self._height = map_height
        self._rooms_count = rooms_count
        self._map = Map(map_width, map_height)
        self._room_width = room_width
        self._room_height = room_height

    def create_maze(self):
        return self.__create_rooms()

    @property
    def map(self):
        return self._map

    def random_center(self) -> Point:
        x = int(self._width / 2)
        y = int(self._height / 2)
        r = int(min([x / 3, y / 3]))
        return Point(randint(x-r, x+r), randint(y-r, y+r))

    def __create_rooms(self):
        self._rooms = []
        rooms_count = randint(self._rooms_count[0], self._rooms_count[1])
        for index in range(rooms_count):
            x, y = self.random_center()
            point = Point(x, y)
            width = randint(self._room_width[0], self._room_width[1])
            height = randint(self._room_height[0], self._room_height[1])
            self._map.add_room(Room(point, width, height))
            yield
