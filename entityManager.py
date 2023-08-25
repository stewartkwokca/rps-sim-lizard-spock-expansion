import entity
import screen
from random import randint

START_COUNT_PER_TYPE = 125

entities = []
counts = [125 for i in range(5)]
for i in range(5):
    for j in range(START_COUNT_PER_TYPE):
        entities.append(entity.Entity(randint(20, screen.WIDTH - 20), randint(20, screen.HEIGHT - 20), i))

def tick():
    for e in entities:
        e.tick()
        for j in range(entities.index(e), len(entities)):
            if e.collision(entities[j]):
                e.resolveMatch(entities[j])
    global counts
    counts = [len([e for e in entities if e.type_id == i]) for i in range(5)]

def render(window):
    for e in entities:
        e.render(window)