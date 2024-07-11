from settings import *
from sprites import Sprite, BuildingColliders
from groups import CollisionSprite, MainSprites, AllSprites
from player import Player

class Level:
    def __init__(self, tmx_map, level_frames):
        self.display_surface = pg.display.get_surface()

        # groups
        self.all_sprites = AllSprites()
        self.collision_sprites = CollisionSprite()
        # self.main_sprites = MainSprites()

        self.level_frames = level_frames

        self.setup(tmx_map, level_frames)

    def setup(self, tmx_map, level_frames):
        # Terrain
        for x, y, surf in tmx_map.get_layer_by_name("Terrain").tiles():
            properties = tmx_map.get_tile_properties(x, y,
                tmx_map.get_layer_by_name("Terrain").id - 1)
            if properties and properties["collide"]:
                # red_square = pg.surface.Surface((TILE_SIZE, TILE_SIZE))
                # pg.draw.rect(red_square, "red", red_square.get_rect(), 0)
                Sprite(
                    (x * TILE_SIZE, y * TILE_SIZE),
                    surf,
                    (self.collision_sprites, self.all_sprites),
                    z=0
                )
            else:
                Sprite(
                    (x * TILE_SIZE, y * TILE_SIZE), surf,
                    (self.all_sprites),
                    z=0
                )

        # # Flowers
        # for x, y, surf in tmx_map.get_layer_by_name("Flowers").tiles():
        #     Sprite((x * TILE_SIZE, y * TILE_SIZE), surf, bg.all_sprites)

        # # Vegetation
        # for obj in tmx_map.get_layer_by_name("Vegetation"):
        #     Sprite(
        #         (obj.x, obj.y),
        #         obj.image,
        #         (self.all_sprites),
        #         z=1
        #     )

        # characters
        for obj in tmx_map.get_layer_by_name("Characters"):
            if obj.name == "Player":
                self.player = Player(
                    pos=(obj.x, obj.y),
                    groups=(self.all_sprites),
                    collision_sprites=self.collision_sprites,
                    frames=self.level_frames["player"],
                    z=1
                )

        # # Buildings
        # for obj in tmx_map.get_layer_by_name("Buildings"):
        #     Sprite((obj.x, obj.y), obj.image, (self.all_sprites,
        #     self.world_sprites))
        #     colliders = obj.properties["colliders"][0]
        #     BuildingColliders(
        #         (colliders.x + obj.x, colliders.y + obj.y),
        #         (colliders.width, colliders.height),
        #         (self.collision_sprites, self.all_sprites),
        #     )

        # self.all_sprites.center_to_target()

    def run(self, dt):
        self.display_surface.fill("gray")
        # self.collision_sprites.draw(self.display_surface)
        self.all_sprites.update(dt)
        self.all_sprites.draw(self.player.rect)
        # self.main_sprites.update(dt)
        # self.main_sprites.draw(self.display_surface)
