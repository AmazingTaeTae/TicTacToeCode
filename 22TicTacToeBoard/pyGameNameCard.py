import pygame, sys
from pygame.locals import *

# Set up pygame.
pygame.init()
# Set up the window.
windowSurface = pygame.display.set_mode((500, 400), 0, 32)


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (111, 0, 225)
YELLOW = (242, 216, 48)

shift_x = 200
shift_y = 100

windowSurface.fill(BLUE)
pygame.draw.polygon(windowSurface, YELLOW, ((0, 0),(0, 25),(25, 0)))
pygame.draw.polygon(windowSurface, GREEN, ((500, 400),(475, 400),(500, 375)))
pygame.draw.polygon(windowSurface, RED, ((500, 0),(500, 25),(475, 0)))
pygame.draw.polygon(windowSurface, WHITE, ((0, 400),(25, 400),(0, 375)))
pygame.draw.rect(windowSurface, PURPLE, (50, 0, 400, 400))
pygame.draw.ellipse(windowSurface, BLACK, (0, 140, 500, 140), 100)


basicFont = pygame.font.SysFont(None, 48)
text = basicFont.render('TAEYOUNG', True, WHITE, BLUE)
windowSurface.blit(text, (160, 200))

pygame.display.update()

# Run the game loop.
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()