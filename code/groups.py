from settings import *


class CollisionSprite(pg.sprite.Group):
    """THis one is not that necessary. I just created it to draw boxes around
    the sprite in this group (for now ...). I am not sure if I will find a
    usage to it. Otherwise it is just a 'debug' class"""
    def __init__(self):
        super().__init__()
        self.display_surface = pg.display.get_surface()


class MainSprites(pg.sprite.Group):
    """Sorts sprites in y."""
    def __init__(self):
        super().__init__()
        self.display_surface = pg.display.get_surface()

    def draw(self, surf):
        for sprite in sorted(self, key=lambda sprite: sprite.rect.bottom):
            self.display_surface.blit(sprite.image, sprite.rect)


class AllSprites(pg.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pg.display.get_surface()
        self.offset = vector()

        # camera
        self.camera_borders = {
            "left": 200, "right": 200, "top": 200, "bottom": 200
        }
        left = self.camera_borders["left"]
        width = (self.display_surface.get_size()[0] - (
            self.camera_borders["right"] + self.camera_borders["left"]
        ))
        top = self.camera_borders["top"]
        height = (self.display_surface.get_size()[1] - (
            self.camera_borders["top"] + self.camera_borders["bottom"]
        ))
        self.camera_rect = pg.Rect(left, top, width, height)

    def box_target_camera(self, target):
        if target.left < self.camera_rect.left:
            self.camera_rect.left = target.left
        if target.right > self.camera_rect.right:
            self.camera_rect.right = target.right
        if target.top < self.camera_rect.top:
            self.camera_rect.top = target.top
        if target.bottom > self.camera_rect.bottom:
            self.camera_rect.bottom = target.bottom

        self.offset.x = (self.camera_rect.left - self.camera_borders["left"])
        self.offset.y = (self.camera_rect.top - self.camera_borders["top"])

    def draw(self, target_pos):
        self.box_target_camera(target_pos)

        # sort by z
        for sprite in sorted(self, key=lambda sprite: sprite.z):
            if sprite.z == 0:
                self.display_surface.blit(sprite.image, sprite.rect.topleft -
                                                        self.offset)

        # sort in y
        for sprite in sorted(self, key=lambda sprite: sprite.rect.bottom):
            if sprite.z == 1:
                self.display_surface.blit(sprite.image, sprite.rect.topleft -
                                                        self.offset)


        # pg.draw.rect(self.display_surface, "orange", self.camera_rect, 2)
