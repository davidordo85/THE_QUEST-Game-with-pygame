import pygame as pg
from ship import ship
from asteroids import asteroids
import sys
import time

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

""" self.handleEvent()
            self.ship.update(800, 600)
            self.asteroid.update(800, 600)
            self.display.fill("black")
            self.display.blit(self.ship.image, self.ship.rect)
            self.display.blit(self.asteroid.image, self.asteroid.rect) """

class Main():
    clock = pg.time.Clock()
    def __init__(self, w, h):
        self.screen = pg.display.set_mode((h, w))
        self.status = 'Opening'
        pg.display.set_caption("THE QUEST")

        self.title = pg.font.Font('./resources/fonts/OdibeeSans-Regular.ttf', 100)
        self.displayProduction = self.title.render("GERMEN PRODUCTION", True, (WHITE))
        self.displayOpening = self.title.render("THE QUEST", True, (WHITE))
        self.ship = ship.Ship(800, 600)
        self.asteroid = asteroids.Asteroid(800, 600)

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

    def redraw(self):
        pg.display.flip()
    
    def opening(self):
        displayOpening = False
        while not displayOpening:
            self.handleEvent()
            self.screen.fill("black")
            self.screen.blit(self.displayProduction, (150, 200))
            self.ship.update(800, 600)
            self.redraw()
            time.sleep(4)
            displayOpening = True
        
        self.status = 'Front'

    def front(self):
        front = False
        self.status = 'Front'
        while not front:
            self.handleEvent()
            self.screen.fill("black")
            self.screen.blit(self.displayOpening, (150, 200))            
            pg.display.flip()        

    def main_loop(self):
        while True:
            if self.status == 'Opening':
                self.opening()
            if self.status == 'Front':
                self.front()
            self.redraw()
            

              

    def quit(self):
        pg.quit()
        sys.exit()

if __name__ == '__main__':
    pg.init(), 
    game = Main(600, 1000)
    game.main_loop()
    game.quit()