import sys
import pygame as pg

class AllienInvasion:
    "skibidi dopdd dop dop ye ye dabydi neep neep neep neeeep(repeat)"
    def __init__(self):
        pg.init()
        self.g = "g"
        self.screen = pg.display.set_mode((1200,800))
        pg.display.set_caption("Allien Invasion")

        self.bg_color  =(230,230,230)

    def run_game(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
            self.screen.fill(self.bg_color)
            pg.display.flip()

if  __name__ == '__main__':
    ai = AllienInvasion()
    ai.run_game()