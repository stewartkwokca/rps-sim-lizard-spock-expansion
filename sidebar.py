import pygame
import screen
import entity
import entityManager

pygame.init()
font = pygame.font.SysFont("arialblack", 50)

Y_BUFFER_BTWN_ICONS = (screen.HEIGHT - (entity.ICON_DIMS[1] * len(entity.imgs))) / (len(entity.imgs) + 1)

def render(window):
    index = 0
    pygame.draw.rect(window, screen.LIGHT_GRAY, (screen.WIDTH, 0, screen.SIDEBAR_WIDTH, screen.HEIGHT))
    for icon in entity.icons:
        window.blit(icon, (screen.WIDTH + (screen.SIDEBAR_WIDTH-entity.ICON_DIMS[0])/2, Y_BUFFER_BTWN_ICONS * (index+1) + entity.ICON_DIMS[1] * index))
        renderText(f"{entityManager.counts[index]}", font, screen.WHITE, screen.WIDTH + (screen.SIDEBAR_WIDTH-entity.ICON_DIMS[0])/2 + 50, Y_BUFFER_BTWN_ICONS * (index+1) + entity.ICON_DIMS[1] * index + 50, window)
        index += 1
def renderText(text, font, text_col, x, y, window):
    img = font.render(text, True, text_col)
    window.blit(img, (x, y))