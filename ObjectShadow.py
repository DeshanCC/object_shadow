import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) #screen

run = True
while run: #game loop
    for event in pygame.event.get(): #event handling
       if event.type == pygame.QUIT:
           run = False
pygame.quit()


