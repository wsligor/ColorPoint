import pygame
from model import Model

class ColorPointView():
    def __init__(self, model, comtroller):
        self.model = model
        self.controller = comtroller
        self.controller.set_view(self)
        self.create_playing_field()
        pass

    def create_playing_field(self):

        pass