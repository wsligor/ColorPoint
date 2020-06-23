class Setting():
    def __init__(self):
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.BLUE = (0, 0, 255)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)

        self.FPS = 60

        self.width_bloks = 10
        self.height_bloks = 10
        self.margin_playing_field = 1
        self.block_size = 40

        self.width = self.width_bloks * self.block_size + (
                self.width_bloks + 1) * self.margin_playing_field
        self.height = self.height_bloks * self.block_size + (
                self.height_bloks + 1) * self.margin_playing_field
        self.SCREEN_SIZE = (self.width, self.height)
