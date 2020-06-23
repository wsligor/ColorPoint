import pygame, os
from enum import Enum
from setting import Setting

class Cell(pygame.sprite.Sprite):
    setting: Setting
    images = []
    def __init__(self, x, y, row, col, status, setting) -> None:
        super().__init__()
        self.setting = setting
        self.row = row
        self.col = col
        self.status = status
        self.load_images()
        self.image = self.images[status]
        self.rect: pygame.Rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def load_images(self):
        current_path = os.path.dirname(__file__)  # Where your .py file is located
        image_path = os.path.join(current_path, 'img')  # The image folder path
        image = pygame.image.load(os.path.join(image_path, 'white.png'))
        image = pygame.transform.scale(image, (self.setting.block_size, self.setting.block_size))
        self.images.append(image)
        image = pygame.image.load(os.path.join(image_path,'blue.png'))
        image = pygame.transform.scale(image, (self.setting.block_size, self.setting.block_size))
        self.images.append(image)
        image = pygame.image.load(os.path.join(image_path,'red.png'))
        image = pygame.transform.scale(image, (self.setting.block_size, self.setting.block_size))
        self.images.append(image)
        image = pygame.image.load(os.path.join(image_path,'green.png'))
        image = pygame.transform.scale(image, (self.setting.block_size, self.setting.block_size))
        self.images.append(image)



class CellStatus(Enum):
    cl_white = 0
    cl_blue = 1
    cl_red = 2
    cl_green = 3