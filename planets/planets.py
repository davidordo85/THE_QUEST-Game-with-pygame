import pygame as pg

class Planet(pg.sprite.Sprite):
    vx = 0
    vy = 0
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.image.load("./resources/images/planets/arid_planet.png")
        self.rect = self.image.get_rect()

        self.rect.centerx = 1100
        self.rect.centery = 300

    def update(self, limSupX, limSupY):
        self.vx = 1.1
        if self.rect.centerx <= 800:
            self.vx = 0
        self.rect.centerx -= self.vx

        