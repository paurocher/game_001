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
        # print(self.tmx_maps[0])
        # print(dir(self.tmx_maps[0]))
        # print(help(self.tmx_maps[0]))
        self.import_assets()

        self.current_stage = Level(self.tmx_maps[0], self.level_frames)

    def import_assets(self):
        self.level_frames = {
            "player": import_sub_folders("..", "art", "objects", "Player")
        }
        # print(self.level_frames)

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

            if keys[pg.K_PLUS]:
                SCALE += 0.01
            if keys[pg.K_MINUS]:
                SCALE = max(SCALE - 0.01, 0.5)
            self.current_stage.all_sprites.scaley = SCALE
            print("dd", SCALE)
            if keys[pg.K_c]:
                self.current_stage.all_sprites.center_to_target()

            self.current_stage.run(dt)

            # scale
            print("SCALE", SCALE)
            a = pg.transform.scale_by(self.display_surface, (SCALE, SCALE))
            arect = a.get_rect()
            # print(self.current_stage.player.rect.center)
            # x = self.current_stage.all_sprites.offset[0] * (SCALE ) * -1
            # y = self.current_stage.all_sprites.offset[1] * (SCALE ) * -1
            # arect.move_ip(x, y)
            arect.center = self.current_stage.player.rect.center
            self.display_surface.fill("black")
            self.display_surface.blit(a, arect)


            pg.display.update()

if __name__ == "__main__":
    game = Game()
    game.run()



# make scale grow sprites instead of resizing the canvas ...