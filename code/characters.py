from settings import *

class Character(pg.sprite.Sprite):
    def __init__(self, pos, groups, collision_sprites, frames, z):
        super().__init__(self, groups)

        self.frames, self.frame_index = frames, 1
        self.state, self.facing_right = "walk_down", True
        self.image = pg.transform.scale_by(
            self.frames[self.state][self.frame_index], (SCALE, SCALE)
        )
        self.z = z

        # rects
        self.rect = self.image.get_frect(topleft=pos)
        self.rect = self.rect.inflate(0, -3)
        self.hit_box = pg.rect.FRect(0, 0 , 5, 10)
        self.hit_box.move_ip(pos)
        self.old_rect = self.hit_box.copy()

        # movement
        self.direction = vector()
        self.speed = 100

        # collision
        self.collision_sprites = collision_sprites

    def move(self):
        """"""
        pass

    def collision(self, axis):
        for sprite in self.collision_sprites:
            if sprite.rect.colliderect(self.hit_box):
                if axis == "horizontal":
                    if (int(self.hit_box.left) <= int(sprite.rect.right) and
                        int(self.old_rect.left) >= int(sprite.old_rect.right)):
                        self.hit_box.left = int(sprite.rect.right)

                    if (int(self.hit_box.right) >= int(sprite.rect.left) and
                        int(self.old_rect.right) <= int(sprite.old_rect.left)):
                        self.hit_box.right = int(sprite.rect.left)

                else:
                    if (int(self.hit_box.top) <= int(sprite.rect.bottom) and
                        int(self.old_rect.top) >= int(sprite.old_rect.bottom)):
                        self.hit_box.top = int(sprite.rect.bottom)

                    if (int(self.hit_box.bottom) >= int(sprite.rect.top) and
                        int(self.old_rect.bottom) <= int(sprite.old_rect.top)):
                        self.hit_box.bottom = int(sprite.rect.top)

    def animate(self, dt):
        pass
        # if self.animation:
        #     self.frame_index += ANIMATION_SPEED * dt
        #     self.image = pg.transform.scale_by(
        #         self.frames[self.state][int(
        #             self.frame_index % len(self.frames[self.state])
        #         )],
        #         (SCALE, SCALE)
        #     )

    def update(self, dt):
        self.old_rect = self.hit_box.copy()
        self.move(dt)
        self.animate(dt)