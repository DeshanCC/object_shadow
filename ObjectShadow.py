import pygame
import sys

pygame.init()

clock = pygame.time.Clock()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # screen

# Read files
king = pygame.image.load('./assets/king.png').convert_alpha()
king = pygame.transform.scale(king, (80, 130))
sky = pygame.image.load('./assets/sky.png').convert_alpha()
sky = pygame.transform.scale(sky, (SCREEN_WIDTH, SCREEN_HEIGHT))
grass = pygame.image.load('./assets/grass.png').convert_alpha()
grass = pygame.transform.scale(grass, (SCREEN_WIDTH, SCREEN_HEIGHT - 400))
king_mask = pygame.mask.from_surface(king).outline()

run = True
while run:  # game loop
    clock.tick(60)
    for event in pygame.event.get():  # event handling
        if event.type == pygame.QUIT:
            run = False
    # Draw images into screen
    screen.fill((0, 0, 0))
    screen.blit(sky, (0, 0))
    screen.blit(grass, (0, 400))
    screen.blit(king, (SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 2) - 20))
    pygame.draw.polygon(screen, (0, 0, 0), king_mask)
    pygame.display.flip()

pygame.quit()
sys.exit()
