from turtle import Screen
import pygame
import sys

WIDTH, HEIGHT = 500, 500

pygame.init()
screen= pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Basic pygame mal")
clock= pygame.time.Clock()
gui_font= pygame.font.Font(None,30)

BLACK = (255,255,255)
RED = (255,0,0)




# Main loop ::::::::::::::::::::::::::::::::::::::::::::::::::::

firkant = pygame.Rect((10,10),(50,50))




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BLACK)
    pygame.draw.rect(screen, RED, firkant)
    pygame.display.update()
    clock.tick(60)


