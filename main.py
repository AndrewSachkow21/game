import sys
import pygame

class AllienInvasion:
    "skibidi dop dop dop ye ye dabydi neep neep neep neeeep(repeat)"
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Allien Invasion")

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.flip()

if  __name__ == '__main__':
    ai = AllienInvasion()
    ai.run_game()