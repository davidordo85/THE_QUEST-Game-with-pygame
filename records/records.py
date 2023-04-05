import pygame as pg

class Record():
    valor = 0
    character = ""
    w = 133
    h = 28
    position = [0, 0]

    def __init__(self, valor = ""):
        super().__init__()
        self.font = pg.font.SysFont("Arial", 25)
        self.character = (valor)        

    def render(self):
        textBlock = self.font.render(self.character, True, (74, 74, 74))
        rect = textBlock.get_rect()
        rect.left = self.position[0]
        rect.top = self.position[1]
        rect.size = (self.w, self.h)

        return (rect, textBlock)

    def posX(self, val=None):
        if val == None:
            return self.position[0]
        else:
            try:
                self.position[0] = int(val)
            except:
                pass

    def posY(self, val=None):
        if val == None:
            return self.position[1]
        else:
            try:
                self.position[1] = int(val)
            except:
                pass

    def pos(self, val=None):
        if val == None:
            return self.position
        else:
            try:
                self.position = [int(val[0]), int(val[1])]
            except:
                pass