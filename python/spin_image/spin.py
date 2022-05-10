"""
Code taken from - slight changes added to make picture in the middle of the screen:
https://www.youtube.com/watch?v=_TU6BEyBieE&t=215s =>
    https://pastebin.com/hLGJYzjV

Small program that spins an image in the middle of hte screen in pygames.
"""

# Setup Python ----------------------------------------------- #
import pygame, sys
from pygame.locals import *

def spin(img, angle, screen):

    # Loop ------------------------------------------------------- #
    while True:
        angle += 6
        
        # Background --------------------------------------------- #
        screen.fill((0,0,0))
     
        # Find the middle of the screen, and draw our image there #
        mx, my = pygame.display.get_window_size()
        img_copy = pygame.transform.rotate(img, angle) # spind image copy

        # Draw the image copy at the midpoint of our screen - the offset of the image due to the transformation
        screen.blit(img_copy, (mx/2 - int(img_copy.get_width() / 2), my/2 - int(img_copy.get_height() / 2)))
        
        # Buttons ------------------------------------------------ #
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                    
        # Update ------------------------------------------------- #
        pygame.display.update()
        mainClock.tick(60)


# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((500, 500),0,32)
 
# Make sure you provide your own image
img = pygame.image.load('ss.png').convert()
img.set_colorkey((0,0,0))
angle = 0
spin(img, angle, screen)
