import pygame
from enum import Enum

class Cell(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.status = CellStatus


class CellStatus(Enum):
    cl_empty = 0
    cl_blue = 1
    cl_red = 2
    cl_green = 3