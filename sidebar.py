import pygame
import screen
import entity
import entityManager

Y_BUFFER_BTWN_ICONS = (screen.HEIGHT - (entity.ICON_DIMS[1] * len(entity.imgs))) / (len(entity.imgs) + 1)

def render(window):
    index = 0
    pygame.draw.rect(window, screen.LIGHT_GRAY, (screen.WIDTH, 0, screen.SIDEBAR_WIDTH, screen.HEIGHT))
    pygame.draw.rect(window, screen.BLACK, (screen.WIDTH, 0, 3, screen.HEIGHT))
    for icon in entity.icons:
        window.blit(icon, (screen.WIDTH + (screen.SIDEBAR_WIDTH-entity.ICON_DIMS[0])/2, Y_BUFFER_BTWN_ICONS * (index+1) + entity.ICON_DIMS[1] * index))
        text = f"{entityManager.counts[index]}"
        text_size = screen.SIDEBAR_FONT.size(text)
        text_buffer_y = (screen.HEIGHT - (text_size[1] * len(entity.imgs))) / (len(entity.imgs) + 1)
        screen.renderText(text, screen.SIDEBAR_FONT, screen.WHITE, screen.WIDTH + (screen.SIDEBAR_WIDTH-text_size[0])/2, text_buffer_y * (index+1) + text_size[1] * index, window)
        index += 1