import random


class Model:
    def __init__(self, setting):
        self.setting = setting
        self.playing_field = []
        self.create_playing_field()

    def create_playing_field(self):
        for row in range (self.setting.height_bloks):
            cells_row = []
            for col in range(self.setting.width_bloks):
                status = random.randint(0, 3)
                cells_row.append(Cell(row, col, status))
            self.playing_field.append(cells_row)

    def get_cell(self, row, col):
        cell = self.playing_field[row][col]
        return cell.status


class Cell():
    def __init__(self, row, col, status):
        self.row = row
        self.col = col
        self.status = status
        pass