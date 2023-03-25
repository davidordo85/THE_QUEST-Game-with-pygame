import pygame as pg

class Ship(pg.sprite.Sprite):
    vx = 0
    vy = 0
    w = 65
    h = 65


    def __init__(self, x, y):
        super().__init__()
        self.image = pg.Surface((self.w, self.h), pg.SRCALPHA, 32)
        self.rect = self.image.get_rect()


        self.rect.centerx = x
        self.rect.centery = y
        self.frame = pg.image.load('./resources/ship_sprites/Spaceships_0.png').convert_alpha()
        self.image.blit(self.frame, (0, 0), (0, 0, self.w, self.h))

        self.rect.centerx = 40
        self.rect.centery = 300

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
