import pygame as pg
from ship import ship
import sys

class Main():
    def __init__(self, w, h):
        self.display = pg.display.set_mode((h, w))
        pg.display.set_caption("THE QUEST")
        running = True
        self.ship = ship.Ship(800, 600)

    def handleEvent(self): # create the keyboard events
        for event in pg.event.get():            
            if event.type == pg.QUIT:
                return self.quit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    self.ship.vy = -1                            

                elif event.key == pg.K_DOWN:
                    self.ship.vy = 1
            elif event.type == pg.KEYUP:
                self.ship.vy = 0
            
            else:
                pass
                
        

        return False

    def main_loop(self):
        while True:
            self.handleEvent()
            self.ship.update(800, 600)
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