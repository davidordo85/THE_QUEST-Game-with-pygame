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
        self.description = pg.font.Font('./resources/fonts/OdibeeSans-Regular.ttf', 30)
        self.displayProduction = self.title.render("GERMEN PRODUCTION", True, (WHITE))
        self.displayOpening = self.title.render("THE QUEST", True, (WHITE))
        self.displayDescription = self.description.render("To avoid colliding with the asteroids use the up or down keys, until the planet to land on appears", True, (WHITE))
        self.startGame = self.description.render("Press space for start", True, (WHITE))
        self.ship = ship.Ship(800, 600)
        self.asteroid = asteroids.Asteroid(800, 600)

    def handleEvent(self): # create the keyboard events
        self.start = False
        for event in pg.event.get():            
            if event.type == pg.QUIT:
                return self.quit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    self.ship.vy = -1
                elif event.key == pg.K_DOWN:
                    self.ship.vy = 1
                elif event.key == pg.K_SPACE:
                    self.start = True             
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
        while not front:
            self.handleEvent()            
            self.screen.fill("black")
            self.ship.update(800, 600)
            self.screen.blit(self.displayOpening, (100, 50))
            self.screen.blit(self.displayDescription, (150, 250))
            self.screen.blit(self.startGame, (150, 500))
            self.screen.blit(self.ship.image, self.ship.rect)
            self.redraw()
            if self.start == True:
                front = True
                
        self.status = 'First_level'

    def firstLevel(self):
        self.handleEvent()
        self.screen.fill("white")
        self.redraw()

        

    def main_loop(self):
        while True:
            if self.status == 'Opening':
                self.opening()
            elif self.status == 'Front':
                self.front()
            elif self.status == 'First_level':
                self.firstLevel()
            

              

    def quit(self):
        pg.quit()
        sys.exit()

if __name__ == '__main__':
    pg.init(), 
    game = Main(600, 1000)
    game.main_loop()
    game.quit()