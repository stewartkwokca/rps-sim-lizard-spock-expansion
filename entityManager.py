import entity
import screen
from random import randint

START_COUNT = 100

entities = []
for i in range(5):
    for j in range(START_COUNT):
        entities.append(entity.Entity(randint(20, screen.WIDTH - 20), randint(20, screen.HEIGHT - 20), i))

def tick():
    for e in entities:
        e.tick()
        for j in range(entities.index(e), len(entities)):
            if e.collision(entities[j]):
                e.resolveMatch(entities[j])

def render(window):
    for e in entities:
        e.render(window)