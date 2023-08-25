import pygame

BG_COLOR = (255, 255, 255)
WIDTH = 800
HEIGHT = 800
def screenSetup():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill(BG_COLOR)

    pygame.display.set_caption('Rock Paper Scissors Simulator: Lizard-Spock Expansion')
    pygame.display.flip()

    return screen

