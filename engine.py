import pygame
from dungeon.helpclass import Settings
from dungeon.map import Map

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    MOUSEBUTTONDOWN,
    BUTTON_LEFT
)

pygame.init()
clock = pygame.time.Clock()
clock.tick(30)


class Engine:
    NEXT_STEP = pygame.USEREVENT

    def __init__(self, map_: Map, next_step=None):
        self._grid = map_
        self.next_step = next_step
        if not pygame.get_init():
            exit(1)
        self._window = None
        self._running = False

    def set_timer(self):
        pygame.time.set_timer(self.NEXT_STEP, 1000, 5)

    def start(self):
        self.__init()
        self._running = True
        self.set_timer()
        self.__loop()

    def __check_event(self):
        mouse = pygame.mouse
        for event in pygame.event.get():
            if self.__is_exit(event):
                return
            if mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
            if event.type == self.NEXT_STEP:
                next(self.next_step())

    def __init(self):
        self._window = pygame.display.set_mode((Settings.WINDOW_WIDTH_PX, Settings.WINDOW_HEIGHT_PX))
        pygame.display.set_caption('Purerandom!')
        # pygame.image.load()
        # pygame.display.set_icon()

    def __is_exit(self, event):
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                self._running = False
        elif event.type == QUIT:
            self._running = False
        return False if self._running else True

    def __loop(self):
        while self._running:
            self.__check_event()
            self._window.fill('white')
            self._window.blit(self._grid.draw(), self._grid.rect)
            pygame.display.flip()
