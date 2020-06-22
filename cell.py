import pygame
from enum import Enum

class Cell(pygame.sprite.Sprite):
    def __init__(self, row, col, status):
        super().__init__()
        self.status = status
        self.row = row
        self.col = col


class CellStatus(Enum):
    cl_empty = 0
    cl_blue = 1
    cl_red = 2
    cl_green = 3