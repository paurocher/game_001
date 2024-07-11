from settings import *

class CollisionSprite(pg.sprite.Group):
    """THis one is not that necessary. I just created it to draw boxes around
    the sprite in this group (for now ...). I am not sure if I will find a
    usage to it. Otherwise it is just a 'debug' class"""
    def __init__(self):
        super().__init__()
        self.display_surface = pg.display.get_surface()

    # def draw(self, surf):
    #     for sprite in self:
    #         pg.draw.rect(surf, "red", sprite.rect, 1)


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
            "left": 250, "right": 250, "top": 100, "bottom": 250
        }
        left = self.camera_borders["left"] / SCALE
        width = (self.display_surface.get_size()[0] - (
            self.camera_borders["right"] + self.camera_borders["left"]
        )) / SCALE
        top = self.camera_borders["top"] / SCALE
        height = (self.display_surface.get_size()[1] - (
            self.camera_borders["top"] + self.camera_borders["bottom"]
        )) / SCALE
        self.camera_rect = pg.Rect(left, top, width, height)

        self.scaley = None

    def center_to_target(self):
        # self.center_offset.x -= self.offset.x
        # self.center_offset.y -= self.offset.y
        pass


    def scale_camera_rect(self):

        print(self.scaley)
        self.camera_rect.scale_by(self.scaley)

    def box_target_camera(self, target):
        # print("target.left:", target, "self.camera_rect.left",
        #     self.camera_rect, end="\n\r\r", flush=True)
        self.scale_camera_rect()
        print(self.camera_rect, SCALE)
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

        # self.offset.x = self.offset.x - self.offset.x * (SCALE - 1)

        # print("self.offset:", self.offset, "self.camera_rect:",
        #     self.camera_rect.center)
        # self.offset.x = self.offset.x - self.offset.x * SCALE


    def draw(self, target_pos):
        self.box_target_camera(target_pos)

        """
        This solution woks for camera with player cenetered.
        (Put the 2 blits at the bottom in substractive though)
        self.offset.x = -(target_pos.center[0] - WINDOW_WIDTH / (2 * SCALE))
        self.offset.y = -(target_pos.center[1] - WINDOW_HEIGHT / (2 * SCALE))
        """
        for sprite in sorted(self, key=lambda sprite: sprite.z):
            if sprite.z == 0:
                self.display_surface.blit(sprite.image, sprite.rect.topleft -
                                                        self.offset)

        for sprite in sorted(self, key=lambda sprite: sprite.rect.bottom):
            if sprite.z == 1:
                self.display_surface.blit(sprite.image, sprite.rect.topleft -
                                                        self.offset)

        # pg.draw.rect(self.display_surface, "yellow", self.camera_rect, 4)
