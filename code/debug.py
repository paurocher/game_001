"""Add here functions to print text or display stuff for debugging purposes."""

from settings import *
import pygame.freetype as ft
ft.init()

class DebugText():
    def __init__(self, text, size, position, color, bg_color):
        self.text = text
        self.size = size
        self.position = position
        self.color = color
        self.bg_color = bg_color
        self.display_surf = pg.display.get_surface()

        self.font = ft.SysFont("Courier", 12)
        self.font.bgcolor = (0,0,0)
        self.font.pad = True

        self.update(self.text)

    def update(self, new_text):
        self.text = str(new_text)

        surf, rect = self.font.render(
            self.text,
            (250, 250, 250)
        )
        rect.topleft = self.position

        self.display_surf.blit(surf, rect)
