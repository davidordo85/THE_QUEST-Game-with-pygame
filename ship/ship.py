import pygame as pg


class Ship(pg.sprite.Sprite):
    vx = 0
    vy = 0
    w = 65
    h = 65
    num_sprites = 17

    def __init__(self, x, y):
        super().__init__()
        self.image = pg.Surface((self.w, self.h), pg.SRCALPHA, 32)
        self.rect = self.image.get_rect()

        self.rect.centerx = x
        self.rect.centery = y

        self.crash = False
        self.game_over = False
        self.image_act = 0
        self.frame = pg.image.load(
            "./resources/images/ship_sprites/Spaceships_0.png"
        ).convert_alpha()
        self.image.blit(self.frame, (0, 0), (0, 0, self.w, self.h))

        self.rect.centerx = 40
        self.rect.centery = 300

    def loadImages(self):
        images = []
        for i in range(self.num_sprites):
            image = pg.image.load(
                "./resources/images/ship_sprites/Spaceships_{}.png".format(i)
            )
            images.append(image)
        return images

    def update(self, limSupX, limSupY):
        self.rect.centerx += self.vx
        self.rect.centery += self.vy
        if self.rect.centerx >= 570:
            self.vx = 0
        if self.rect.centerx <= 40:
            self.vx = 0

        if self.rect.centery < self.rect.h // 2:
            self.rect.centery = self.rect.h // 2

        if self.rect.centery > limSupY - self.rect.h // 2:
            self.rect.centery = limSupY - self.rect.h // 2

    def crashed(self, group):
        list_crash = pg.sprite.spritecollide(self, group, False)
        if len(list_crash) > 0:
            self.crash = True
        else:
            pass

    def collide(self):
        if self.crash == True:
            self.image_act += 1
            self.images = self.loadImages()
            if self.image_act >= self.num_sprites:
                self.image_act = 0
                self.game_over = True
            self.image.blit(self.images[self.image_act], (0, 0))
        else:
            pass
