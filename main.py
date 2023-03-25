import pygame as pg
from ship import ship
import sys

class Main():
    def __init__(self, w, h):
        self.display = pg.display.set_mode((h, w))
        pg.display.set_caption("THE QUEST")
        running = True
        self.ship = ship.Ship(800, 600)

    def main_loop(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return self.quit()
            self.display.fill("black")
            self.display.blit(self.ship.image, self.ship.rect)
            pg.display.flip()
    

    def quit(self):
        pg.quit()
        sys.exit()

if __name__ == '__main__':
    pg.init(), 
    game = Main(600, 1000)
    game.main_loop()
    game.quit()