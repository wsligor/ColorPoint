import pygame, random
from model import Model
from setting import Setting
from cell import Cell


class ColorPointView():
    setting: Setting
    cells: pygame.sprite.Group

    def __init__(self, setting, comtroller=None):
        self.setting = setting
        self.controller = comtroller
        # self.controller.set_view(self)
        self.model = Model(self.setting)
        self.row_count = self.setting.height_bloks
        self.col_count = self.setting.width_bloks
        self.cells = pygame.sprite.Group()
        self.create_playing_field()
        pass

    def create_playing_field(self):
        for row in range(self.row_count):
            for col in range(self.col_count):
                status = self.model.get_cell(row, col)
                print(status)
                x = col * self.setting.block_size + (col + 1) * self.setting.margin_playing_field
                y = row * self.setting.block_size + (row + 1) * self.setting.margin_playing_field
                cell = Cell(x, y, row, col, status, self.setting)
                self.cells.add(cell)
