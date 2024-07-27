"""Add here functions to print text or display stuff for debugging purposes."""

from settings import *
import pygame.freetype as ft
ft.init()

class DebugText():
    def __init__(self, size, position, color, bg_color):
        self.size = size
        self.position = position
        self.color = color
        self.bg_color = bg_color
        self.display_surf = pg.display.get_surface()

        self.font = ft.SysFont("Courier", self.size)
        self.font.bgcolor = (0,0,0)
        self.font.pad = True

    def update(self, text):
        surf, rect = self.font.render(
            str(text),
            (250, 250, 250)
        )
        rect.topleft = self.position

        self.display_surf.blit(surf, rect)
