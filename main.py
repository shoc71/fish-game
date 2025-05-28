import pygame 
import os

from draw_class import *

# init
pygame.init()

os.environ['SDL_VIDEO_CENTERED'] = "1" # called before pygame.init()
info = pygame.display.Info() # called before set_mode()

# constant
SCREEN_WIDTH, SCREEN_HEIGHT = info.current_w, info.current_h
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE) # Example size

running = True
rect = Rectangle(screen, 'red', 100, 100, 100, 100)

while running:
    rect.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()