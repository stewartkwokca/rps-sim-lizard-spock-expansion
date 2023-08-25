import pygame

WHITE = (255, 255, 255)
BLACK = (0,0,0)
LIGHT_GRAY = (211, 211, 211)

WIDTH = 800
SIDEBAR_WIDTH = 200
HEIGHT = 800
def screenSetup():
    screen = pygame.display.set_mode((WIDTH+SIDEBAR_WIDTH, HEIGHT))
    screen.fill(WHITE)

    pygame.display.set_caption('Rock Paper Scissors Simulator: Lizard-Spock Expansion')
    pygame.display.flip()

    return screen

