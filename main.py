import pygame
import screen
import time
import entityManager
import sidebar

pygame.init()

window = screen.screenSetup()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill(screen.WHITE)

    entityManager.tick()
    entityManager.render(window)

    sidebar.render(window)

    time.sleep(0.05)
    pygame.display.update()