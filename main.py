import pygame as pg
import sys

class Main():
    def __init__(self, w, h):
        self.display = pg.display.set_mode((h, w))
        pg.display.set_caption("THE QUEST")
        running = True

    def main_loop(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return self.quit()
            self.display.fill("red")
            pg.display.flip()
    

    def quit(self):
        pg.quit()
        sys.exit()

if __name__ == '__main__':
    pg.init(), 
    game = Main(600, 1000)
    game.main_loop()
    game.quit()