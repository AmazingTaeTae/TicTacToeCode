import pygame, sys
from pygame.locals import *


# Set up pygame.
pygame.init()
# Set up the window.
windowSurface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Hello world!')




# Set up the colors.
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (111, 0, 225)
YELLOW = (242, 216, 48)





# Draw the white background onto the surface.
windowSurface.fill(PURPLE)

# Draw a green polygon onto the surface.
shift_x = 200
shift_y = 100
pygame.draw.polygon(windowSurface, GREEN, ((146 + shift_x, 0 + shift_y), (291 + shift_x, 106 + shift_y), (236 + shift_x, 277 + shift_y), (56 + shift_x, 277 + shift_y), (0 + shift_x, 106 + shift_y)))

# Draw some blue lines onto the surface.
pygame.draw.line(windowSurface, BLUE, (60, 60), (120, 60), 4)
pygame.draw.line(windowSurface, BLUE, (120, 60), (60, 120))
pygame.draw.line(windowSurface, BLUE, (60, 120), (120, 120), 4)

# Draw a blue circle onto the surface.
pygame.draw.circle(windowSurface, BLUE, (300, 50), 20, 0)

# Draw a red ellipse onto the surface.
pygame.draw.ellipse(windowSurface, RED, (300, 250, 40, 80), 1)



# Set up the fonts.
basicFont = pygame.font.SysFont(None, 48)

# # Set up the text.
text = basicFont.render('Hello world!', True, WHITE, BLUE)
textRect = text.get_rect()
textRect.centerx = 500 / 2
textRect.centery = 400 / 2

# # Draw the text's background rectangle onto the surface.
pygame.draw.rect(windowSurface, RED, (textRect.left - 20,
  textRect.top - 20, textRect.width + 40, textRect.height + 40))
print(textRect)
# Draw the text onto the surface.
windowSurface.blit(text, textRect)



# Get a pixel array of the surface.
pixArray = pygame.PixelArray(windowSurface)
pixArray[100][100] = RED
del pixArray




# Draw the window onto the screen.
pygame.display.update()



# Run the game loop.
while True:


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
