from settings import *


class Sprite(pg.sprite.Sprite):
    def __init__(self, pos, surf, groups, z):
        super().__init__(groups)
        self.image = pg.transform.scale_by(surf, (SCALE, SCALE))

        # rects
        self.rect = self.image.get_frect(topleft=pos)
        self.old_rect = self.rect.copy()
        self.z = z


class BuildingColliders(pg.sprite.Sprite):
    def __init__(self, pos, wh, groups, z):
        super().__init__(groups)

        # rects
        self.rect = pg.Rect((pos), (wh))
        self.old_rect = self.rect.copy()

        self.image = pg.Surface((0, 0))
        self.image = pg.Surface(wh)
        self.image.fill("blue")

        self.z = z