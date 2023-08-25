import screen
import random
import pygame

DEFAULT_IMAGE_SIZE = (20, 20)
ICON_DIMS = (150, 150)

imgsPath = "./assets/images/"
types = ["rock", "paper", "scissors", "lizard", "spock"]
imgs = [pygame.transform.scale(pygame.image.load(f"{imgsPath}{t}.png"), DEFAULT_IMAGE_SIZE) for t in types]
icons = [pygame.transform.scale(pygame.image.load(f"{imgsPath}{t}.png"), ICON_DIMS) for t in types]

matchups_won = [[2, 3], [0, 4], [1, 3], [1, 4], [0, 2]]

class Entity():
    def __init__(self, x, y, type_id):
        self.x = x
        self.y = y

        self.WIDTH = 20
        self.HEIGHT = 20
        self.SPEED = 10

        self.type_id = type_id

    def tick(self):
        self.move()
        self.stayInBounds()

    def move(self):
        self.x += random.randint(-1*self.SPEED, self.SPEED)
        self.y += random.randint(-1*self.SPEED, self.SPEED)

    def stayInBounds(self):
        self.x = max(min(self.x, screen.WIDTH-20), 20)
        self.y = max(min(self.y, screen.HEIGHT-20), 20)

    def render(self, window):
        window.blit(imgs[self.type_id], (self.x-self.WIDTH/2, self.y-self.HEIGHT/2))

    def collision(self, other):
        return abs(self.x - other.x) <= self.WIDTH and abs(self.y - other.y) <= self.HEIGHT

    def resolveMatch(self, other):
        if other.type_id in matchups_won[self.type_id]:
            other.type_id = self.type_id
        else:
            self.type_id = other.type_id


