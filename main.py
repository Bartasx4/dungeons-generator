from engine import Engine

from dungeon.point import Point
from dungeon.room import Room
from dungeon.map import Map
from dungeon.rooms import Rooms

if __name__ == '__main__':
    rooms = Rooms(300, 200)
    engine = Engine(rooms.map, next_step=rooms.create_maze)
    engine.start()
