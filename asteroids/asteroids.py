import pygame as pg
import random



class Asteroid(pg.sprite.Sprite):
    vx = 0
    vy = 0
    num_sprites = 29

    def __init__(self, x, y):
        self.w = 160
        self.h = 160
        super().__init__()
        self.image = pg.Surface((self.w, self.h), pg.SRCALPHA, 32)
        self.rect = self.image.get_rect()
        self.images = self.load_images()
        self.image_act = 0
        self.image.blit(self.images[self.image_act], [0, 0])
        self.rect.centerx = 1200
        self.rect.centery = random.randint(40, 560)

    def load_images(self):
        images = []
        for i in range(self.num_sprites):
            image = pg.image.load(
                "./resources/images/asteroid_sprites/asteroid_{}.png".format(i)
            )
            images.append(image)
        return images

    def update(self, limSupX, limSupY):
        self.vx = random.randint(3, 20)
        if self.rect.centerx <= 0:
            self.rect.centerx = 1200
            self.rect.centery = random.randint(40, 560)
        else:
            self.rect.centerx -= self.vx

        self.image_act += 1
        if self.image_act >= self.num_sprites:
            self.image_act = 0

        self.image.blit(self.images[self.image_act], (0, 0))
