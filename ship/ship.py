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


        self.rect.centerx = 40
        self.rect.centery = 300
        self.frame = pg.image.load('./resources/ship_sprites/Spaceships_0.png').convert_alpha()
        self.image.blit(self.frame, (0, 0), (0, 0, self.w, self.h))
