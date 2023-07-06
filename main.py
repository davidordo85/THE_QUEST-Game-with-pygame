import pygame as pg
from ship import ship
from asteroids import asteroids
from planets import planets
from records import records
import sys, time

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# points to win by levels
WIN_FIRST_LEVEL = 900
WIN_SECOND_LEVEL = 4900
WIN_THIRD_LEVEL = 14100

# Clock and frames per second (FPS) configuration
clock = pg.time.Clock()
FPS = 60


class Main:
    def __init__(self, w, h):
        # Create the screen with its size
        self.screen = pg.display.set_mode((w, h))
        # Name the window
        pg.display.set_caption("THE QUEST")

        # Added fonts and images
        self.description = pg.font.Font("./resources/fonts/OdibeeSans-Regular.ttf", 20)
        self.title = pg.font.Font("./resources/fonts/OdibeeSans-Regular.ttf", 100)
        self.fontScore = pg.font.Font("./resources/fonts/OdibeeSans-Regular.ttf", 50)
        self.background = pg.image.load(
            "./resources/images/backgrounds/background_game.png"
        )

        self.score = 0
        self.max_scores = [
            {"name": "Viciado", "score": 14014},
            {"name": "Dangerous", "score": 12001},
            {"name": "Aburrido", "score": 300},
            {"name": "Curious", "score": 10},
        ]

        self.whatLevel = 0
        self.status = "Opening"

        # create the screen texts and objects
        self.displayProduction = self.title.render("DAVID PRODUCTION", True, (WHITE))
        self.displayOpening = self.title.render("THE QUEST", True, (WHITE))
        self.displayDescription = self.description.render(
            "To avoid colliding with the asteroids use the up or down keys, until the planet to land on appears",
            True,
            (WHITE),
        )
        self.startGame = self.description.render("Press space for start", True, (WHITE))
        self.startingLevel = self.description.render(
            "Press enter for start", True, (WHITE)
        )
        self.theEnd = self.title.render("Game Over", True, (WHITE))
        self.scoring = self.fontScore.render(str(self.score), True, WHITE)
        self.ship = ship.Ship(800, 600)
        self.planet = planets.Planet(800, 600)
        self.writing = records.Record("")
        self.writing.pos((325, 300))

        self.asteroid_0 = asteroids.Asteroid(800, 600)
        self.asteroid_1 = asteroids.Asteroid(800, 600)
        self.asteroid_2 = asteroids.Asteroid(800, 600)
        self.asteroid_3 = asteroids.Asteroid(800, 600)
        self.asteroid_4 = asteroids.Asteroid(800, 600)
        self.asteroid_5 = asteroids.Asteroid(800, 600)
        self.asteroid_6 = asteroids.Asteroid(800, 600)
        self.asteroid_7 = asteroids.Asteroid(800, 600)

        self.asteroidLevel1 = pg.sprite.Group()
        self.asteroidLevel2 = pg.sprite.Group()
        self.asteroidLevel3 = pg.sprite.Group()
        self.asteroidLevel1.add(self.asteroid_0, self.asteroid_1, self.asteroid_2)
        self.asteroidLevel2.add(
            self.asteroid_0,
            self.asteroid_1,
            self.asteroid_2,
            self.asteroid_3,
            self.asteroid_4,
        )
        self.asteroidLevel3.add(
            self.asteroid_0,
            self.asteroid_1,
            self.asteroid_2,
            self.asteroid_3,
            self.asteroid_4,
            self.asteroid_5,
            self.asteroid_6,
            self.asteroid_7,
        )

    # Create the keyboard events
    def handleEvent(self):
        self.startLevel = False
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
                elif event.key == pg.K_RETURN:
                    self.startLevel = True
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

    # Background movement
    def background_move(self):
        self.x -= 0.5
        if self.x <= -2400:
            self.x = 0

    # Update the screen
    def redraw(self):
        pg.display.flip()

    # Scoring conditions
    def scoring_conditions(self, asteroidForLevel):
        for entity in asteroidForLevel:
            if entity.rect.centerx <= 0:
                self.score += 20
                self.scoring = self.fontScore.render(str(self.score), True, WHITE)
            else:
                self.score = int(self.score)

    # Win conditions
    def win_conditions(self, winLevel, asteroidForLevel):
        if self.status == "Third_level":
            self.planet.state = True
        if self.score >= winLevel:
            self.ship.land = True
            self.planet.what_planet()
            self.planet.update(800, 600)
            if self.planet.rect.centerx <= 1000 and self.ship.angle % 180 <= 0:
                self.ship.land = False
                self.ship.rect.centerx += self.ship.vx
                if self.ship.rect.centery > 300:
                    self.ship.rect.centery -= self.ship.vx
                elif self.ship.rect.centery < 300:
                    self.ship.rect.centery += self.ship.vx
                else:
                    pass

            for entity in asteroidForLevel:
                if entity.rect.centerx >= 1200:
                    pg.sprite.Group.empty(asteroidForLevel)
        else:
            pass

    def render_ranking(self):
        max_scores_sorted = sorted(
            self.max_scores, key=lambda x: x["score"], reverse=True
        )
        max_scores_top_10 = max_scores_sorted[:10]
        y_position = 75

        # Encabezado de la tabla
        header_text = " <----- Max Scores ------->"
        header_render = self.fontScore.render(header_text, True, WHITE)
        self.screen.blit(header_render, (100, y_position))
        y_position += 50

        # Encabezados de las columnas
        column_rank_text = "Rank"
        column_name_text = "Name"
        column_score_text = "Score"
        column_rank_render = self.fontScore.render(column_rank_text, True, WHITE)
        column_name_render = self.fontScore.render(column_name_text, True, WHITE)
        column_score_render = self.fontScore.render(column_score_text, True, WHITE)
        self.screen.blit(column_rank_render, (100, y_position))
        self.screen.blit(column_name_render, (250, y_position))
        self.screen.blit(column_score_render, (450, y_position))
        y_position += 50

        # Puntuaciones ordenadas
        for i, player_info in enumerate(max_scores_top_10):
            position = i + 1
            name = player_info["name"]
            score = player_info["score"]
            rank_text = f"{position}"
            name_text = f"{name}"
            score_text = f"{score}"
            rank_render = self.fontScore.render(rank_text, True, WHITE)
            name_render = self.fontScore.render(name_text, True, WHITE)
            score_render = self.fontScore.render(score_text, True, WHITE)

            rank_x = 100
            name_x = 250
            score_x = 550 - self.fontScore.size(score_text)[0]

            self.screen.blit(rank_render, (rank_x, y_position))
            self.screen.blit(name_render, (name_x, y_position))
            self.screen.blit(score_render, (score_x, y_position))
            y_position += 50

    # First loop
    def opening(self):
        displayOpening = False
        while not displayOpening:
            self.handleEvent()
            self.screen.fill("black")
            self.screen.blit(self.displayProduction, (50, 200))
            self.redraw()
            time.sleep(4)
            displayOpening = True

        self.status = "Max scores"

    def ranking(self):
        ranking = False
        while not ranking:
            self.handleEvent()
            self.screen.fill("black")
            self.render_ranking()
            self.redraw()
            time.sleep(4)
            ranking = True

        self.status = "Front"

    # front loop
    def front(self):
        front = False
        while not front:
            self.handleEvent()
            self.screen.fill("black")
            self.screen.blit(self.displayOpening, (100, 50))
            self.screen.blit(self.displayDescription, (10, 250))
            self.screen.blit(self.startGame, (150, 500))
            self.redraw()
            if self.start == True:
                front = True

        self.status = "First_level"

    # Game levels loop
    def levels(self, asteroidForLevel, Win):
        level = False
        self.x = 0
        self.scoring = self.fontScore.render(str(self.score), True, WHITE)

        while not level:
            clock.tick(FPS)
            self.handleEvent()
            self.background_move()
            self.scoring_conditions(asteroidForLevel)
            self.ship.update(800, 600)
            asteroidForLevel.update(800, 600)

            self.ship.collide()
            self.ship.crashed(asteroidForLevel)
            self.ship.rotate()
            self.win_conditions(Win, asteroidForLevel)

            self.screen.blit(self.background, (self.x, 0))
            self.screen.blit(self.background, (self.x + 2400, 0))
            self.screen.blit(self.scoring, (700, 30))
            self.screen.blit(self.ship.image, self.ship.rect)
            self.screen.blit(self.planet.image, self.planet.rect)
            asteroidForLevel.draw(self.screen)

            if self.ship.rect.centerx >= 570 and self.status == "First_level":
                self.score += 1000
                level = True
                self.whatLevel += 1
                self.notFirstLevel = True
                self.status = "Take_off"

            if self.ship.rect.centerx >= 570 and self.status == "Second_level":
                self.score += 2000
                level = True
                self.whatLevel += 1
                self.status = "Take_off"

            if self.ship.rect.centerx >= 570 and self.status == "Third_level":
                self.score += 5000
                level = True
                self.status = "Game_over"

            if self.ship.game_over == True:
                time.sleep(4)
                level = True
                self.status = "Game_over"

            self.redraw()

    # take off loop
    def take_off(self):
        clock.tick(FPS)
        take_off = False
        self.scoring = self.fontScore.render(str(self.score), True, WHITE)
        self.ship.land = True

        while not take_off:
            self.handleEvent()
            self.background_move()
            self.ship.update(800, 600)

            self.ship.rotate()
            self.screen.blit(self.background, (self.x, 0))
            self.screen.blit(self.background, (self.x + 2400, 0))
            self.screen.blit(self.scoring, (700, 30))
            self.screen.blit(self.ship.image, self.ship.rect)
            self.screen.blit(self.planet.image, self.planet.rect)

            if self.ship.rect.centerx == 570 and self.ship.angle % 180 >= 0:
                self.ship.land = False
                self.ship.vx -= 1

            if self.ship.rect.centerx <= 40:
                self.planet.take_offPlanet(800, 600)
                self.ship.vx = 0
                self.screen.blit(self.startingLevel, (150, 500))

            if (
                self.startLevel == True
                and self.whatLevel == 1
                and self.planet.rect.centerx >= 1010
            ):
                self.startLevel = False
                take_off = True
                self.status = "Second_level"
            elif (
                self.startLevel == True
                and self.whatLevel == 2
                and self.planet.rect.centerx >= 1010
            ):
                self.startLevel = False
                take_off = True
                self.status = "Third_level"
            else:
                pass

            self.redraw()

    # game over loop
    def game_over(self):
        over = False
        self.scoring = self.fontScore.render(
            "Your final score... {}".format(str(self.score)), True, WHITE
        )

        while not over:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return self.quit()
                if event.type == pg.KEYDOWN:
                    if (
                        event.unicode in "abcdefghijklmnñopqrstuvwyz"
                        and len(self.writing.character) <= 10
                    ):
                        self.writing.character += event.unicode
                        self.writing.valor += 1
                    elif event.key == pg.K_BACKSPACE:
                        self.writing.character = self.writing.character[:-1]
                        self.writing.valor -= 1
                        if self.writing.valor < 0:
                            self.writing.valor = 0
                    elif event.key == pg.K_RETURN and self.writing.valor >= 3:
                        player_info = {
                            "name": self.writing.character,
                            "score": self.score,
                        }
                        self.max_scores.append(player_info)
                        over = True

            self.handleEvent()
            self.screen.fill("blue")
            self.screen.blit(self.scoring, (100, 150))
            self.screen.blit(self.theEnd, (30, 30))
            self.text = self.writing.render()
            pg.draw.rect(self.screen, (WHITE), self.text[0])
            self.screen.blit(self.text[1], self.writing.pos())
            self.redraw()
        self.status = "Opening"

    # Control loops
    def main_loop(self):
        while True:
            if self.status == "Opening":
                self.opening()
            elif self.status == "Max scores":
                self.ranking()
            elif self.status == "Front":
                self.front()
            elif self.status == "First_level":
                self.levels(self.asteroidLevel1, WIN_FIRST_LEVEL)
            elif self.status == "Second_level":
                self.levels(self.asteroidLevel2, WIN_SECOND_LEVEL)
            elif self.status == "Third_level":
                self.levels(self.asteroidLevel3, WIN_THIRD_LEVEL)
            elif self.status == "Take_off":
                self.take_off()
            elif self.status == "Game_over":
                self.game_over()

    def quit(self):
        pg.quit()
        sys.exit()


if __name__ == "__main__":
    pg.init(),
    game = Main(800, 600)
    game.main_loop()
    game.quit()
