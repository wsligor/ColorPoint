import random
from cell import Cell

class Model:
    def __init__(self, setting):
        self.setting = setting
        self.playing_field = []
        self.create_playing_field()

    def create_playing_field(self):
        for row in range (self.setting.height_playing_field):
            cells_row = []
            for col in range(self.setting.width_playing_field):
                status = random.randint(0, 3)
                cells_row.append(Cell(row, col, status))
            self.playing_field.append(cells_row)
