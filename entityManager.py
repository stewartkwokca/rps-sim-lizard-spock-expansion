import entity
import screen
from random import randint

START_COUNT_PER_TYPE = 125

entities = []
counts = [START_COUNT_PER_TYPE for i in range(len(entity.types))]
for i in range(len(entity.types)):
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
    if simOver():
        winner = entity.types[entities[0].type_id].capitalize()
        text_size = screen.GAME_OVER_FONT.size(f"{winner} Wins.")
        screen.renderText(f"{winner} Wins.", screen.GAME_OVER_FONT, screen.BLACK, (screen.WIDTH-text_size[0])/2, (screen.HEIGHT-text_size[1])/2, window)

def simOver():
    return (len(entity.types)*START_COUNT_PER_TYPE) in counts