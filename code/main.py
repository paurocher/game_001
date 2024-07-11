import sys
from os import path

from pytmx.util_pygame import load_pygame

from settings import *
from level import Level
from support import *

class Game:
    def __init__(self):
        pg.init()
        self.display_surface = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pg.display.set_caption("El gatet")

        self.clock = pg.Clock()

        self.tmx_maps = {
            0: load_pygame(
                path.join("..", "art", "tiled_projects", "map_prova_001.tmx")
            )
        }
        self.import_assets()

        self.current_stage = Level(self.tmx_maps[0], self.level_frames)

    def import_assets(self):
        self.level_frames = {
            "player": import_sub_folders("..", "art", "objects", "Player")
        }

    def run(self):
        global SCALE
        while True:
            dt = self.clock.tick() / 1000
            # print(dt)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

            keys = pg.key.get_pressed()

            if keys[pg.K_q]:
                pg.quit()
                sys.exit()

            self.current_stage.run(dt)

            pg.display.update()

if __name__ == "__main__":
    game = Game()
    game.run()



# make scale grow sprites instead of resizing the canvas ...