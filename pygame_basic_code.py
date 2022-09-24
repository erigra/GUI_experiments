import pygame
import sys

pygame.init()
screen= pygame.display.set_mode(500,500)
pygame.display.set_caption("Basic pygame mal")
clock= pygame.time.Clock()
gui_font= pygame.font.Font(None,30)

background_color = (255,255,255)

# Main loop

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT():
            pygame.quit()
            sys.exit()

    screen.fill(background_color)

    pygame.display.update()
    clock.tick(60)
