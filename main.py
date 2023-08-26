import pygame
import screen
import time
import entityManager
import sidebar
import graph

pygame.init()

window = screen.screenSetup()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    graph.dataUpdate()
    window.fill(screen.WHITE)

    entityManager.tick()
    entityManager.render(window)

    sidebar.render(window)

    time.sleep(0.05)

    pygame.display.update()

    if entityManager.simOver():
        graph.createGraph()