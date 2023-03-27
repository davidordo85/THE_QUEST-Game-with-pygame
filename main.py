import pygame as pg
from ship import ship
from asteroids import asteroids
import sys
import time

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Main():
    clock = pg.time.Clock()
    def __init__(self, w, h):
        #create the screen with its size
        self.screen = pg.display.set_mode((h, w))
        #name the window
        pg.display.set_caption("THE QUEST")

        # added fonts and images
        self.description = pg.font.Font('./resources/fonts/OdibeeSans-Regular.ttf', 30)
        self.title = pg.font.Font('./resources/fonts/OdibeeSans-Regular.ttf', 100)
        self.fontScore = pg.font.Font('./resources/fonts/OdibeeSans-Regular.ttf', 50)
        self.background = pg.image.load("./resources/images/backgrounds/background_game.png")

        self.score = 0
        self.status = 'Opening'

        # create the screen texts and objects
        self.displayProduction = self.title.render("GERMEN PRODUCTION", True, (WHITE))
        self.displayOpening = self.title.render("THE QUEST", True, (WHITE))
        self.displayDescription = self.description.render("To avoid colliding with the asteroids use the up or down keys, until the planet to land on appears", True, (WHITE))
        self.startGame = self.description.render("Press space for start", True, (WHITE))
        self.displayScore = self.fontScore.render(str(self.score), True, WHITE)
        self.ship = ship.Ship(800, 600)
        self.asteroid = asteroids.Asteroid(800, 600)

        

    # create the keyboard events
    def handleEvent(self): 
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
        key_pressed = pg.key.get_pressed()
        if key_pressed[pg.K_UP]:
            self.ship.vy -= 1
                
        elif key_pressed[pg.K_DOWN]:
            self.ship.vy += 1
        else:
            self.ship.vy = 0   

        return False

    def backgroundMove(self):
        self.x -= 0.5
        if self.x <= -2400:
            self.x = 0
        

    def redraw(self):
        pg.display.flip()
    
    def opening(self):
        displayOpening = False
        while not displayOpening:
            self.handleEvent()
            self.screen.fill("black")
            self.screen.blit(self.displayProduction, (150, 200))
            self.redraw()
            time.sleep(4)
            displayOpening = True
        
        self.status = 'Front'

    def front(self):
        front = False
        while not front:
            self.handleEvent()            
            self.screen.fill("black")
            self.screen.blit(self.displayOpening, (100, 50))
            self.screen.blit(self.displayDescription, (150, 250))
            self.screen.blit(self.startGame, (150, 500))
            self.redraw()
            if self.start == True:
                front = True
                
        self.status = 'First_level'

    def firstLevel(self):
        first = False
        self.x = 0
        

        while not first:
            self.handleEvent()
            self.backgroundMove()
            self.ship.update(800, 600)
            self.asteroid.update(800, 600)
            self.screen.blit(self.background, (self.x, 0))
            self.screen.blit(self.background, (self.x+2400, 0))
            self.screen.blit(self.displayScore, (950, 30))
            self.screen.blit(self.ship.image, self.ship.rect)
            self.screen.blit(self.asteroid.image, self.asteroid.rect)
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