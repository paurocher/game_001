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
                if DEBUG:
                    pg.draw.rect(surf, (255, 0, 0), surf.get_rect(), 2, 2)
                Sprite(
                    (x * TILE_SIZE * SCALE, y * TILE_SIZE * SCALE),
                    surf,
                    (self.collision_sprites, self.all_sprites),
                    z=0
                )
            else:
                Sprite(
                    (x * TILE_SIZE * SCALE, y * TILE_SIZE * SCALE), surf,
                    (self.all_sprites),
                    z=0
                )

        # Flowers
        for x, y, surf in tmx_map.get_layer_by_name("Flowers").tiles():
            Sprite((x * TILE_SIZE * SCALE, y * TILE_SIZE * SCALE), surf,
                self.all_sprites, 0)

        # Vegetation
        for obj in tmx_map.get_layer_by_name("Vegetation"):
            Sprite(
                (obj.x * SCALE, obj.y * SCALE),
                obj.image,
                (self.all_sprites),
                z=1
            )

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

        # Buildings
        for obj in tmx_map.get_layer_by_name("Buildings"):
            colliders = obj.properties["colliders"][0]
            BuildingColliders(
                pos=(
                    colliders.x * SCALE + obj.x * SCALE,
                    colliders.y * SCALE + obj.y * SCALE
                ),
                wh=(colliders.width * SCALE, colliders.height * SCALE),
                groups=(self.collision_sprites),
                z=1
            )

            if DEBUG:
                pg.draw.rect(
                    obj.image,
                    (255, 0, 0),
                    (colliders.x * SCALE, colliders.y * SCALE,
                    colliders.width * SCALE,
                    colliders.height * SCALE),
                    2,
                    2
                )
            Sprite(
                (obj.x * SCALE, obj.y * SCALE),
                obj.image,
                self.all_sprites,
                z=1
            )

    def run(self, dt):
        self.display_surface.fill("gray")
        self.all_sprites.update(dt)
        self.all_sprites.draw(self.player.rect)
