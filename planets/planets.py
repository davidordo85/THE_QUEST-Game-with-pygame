import pygame as pg


class Planet(pg.sprite.Sprite):
    vx = 0
    vy = 0
    w = 74
    h = 90
    num_sprites = 28

    def __init__(self, x, y):
        super().__init__()
        self.image = pg.Surface((self.w, self.h), pg.SRCALPHA, 32)
        self.rect = self.image.get_rect()
        self.state = False
        self.image_act = 0
        self.frame = pg.image.load(
            "./resources/images/planets/planet_0.png"
        ).convert_alpha()
        self.image.blit(self.frame, (0, 0), (0, 0, self.w, self.h))

        self.rect.centerx = 1100
        self.rect.centery = 300

    def load_images(self):
        images = []
        for i in range(self.num_sprites):
            image = pg.image.load("./resources/images/planets/planet_{}.png".format(i))
            images.append(image)
        return images

    def what_planet(self):
        self.images = self.load_images()
        if self.state == True:
            self.image_act = 1
            self.image.blit(self.images[self.image_act], (0, 0))
        else:
            self.image_act = 0
            self.image.blit(self.images[self.image_act], (0, 0))

    def update(self, limSupX, limSupY):
        self.vx = 1.1
        if self.rect.centerx <= 800:
            self.vx = 0
        self.rect.centerx -= self.vx

    def take_offPlanet(self, limSupX, limSupY):
        self.vx = 1.1
        if self.rect.centerx >= 1010:
            self.vx = 0

        self.rect.centerx += self.vx
