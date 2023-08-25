import pygame
import screen
import time
import entityManager

pygame.init()

window = screen.screenSetup()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill(screen.BG_COLOR)

    entityManager.tick()
    entityManager.render(window)

    time.sleep(0.05)
    pygame.display.update()