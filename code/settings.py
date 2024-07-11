import sys
import pygame as pg

from pygame.math import Vector2 as vector


WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
SURF = pg.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
SCALE = 1.0

TILE_SIZE = 12

ANIMATION_SPEED = 6

Z_LAYERS = {
    "a": 0,
    "b": 1,
}