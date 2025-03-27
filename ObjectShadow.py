import pygame
import math
import sys

pygame.init()

clock = pygame.time.Clock()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # screen

# Read files
king = pygame.image.load('./assets/king.png').convert_alpha()
king = pygame.transform.scale(king, (80, 130))
sky = pygame.image.load('./assets/sky.png').convert_alpha()
sky = pygame.transform.scale(sky, (SCREEN_WIDTH, SCREEN_HEIGHT))
grass = pygame.image.load('./assets/grass.png').convert_alpha()
grass = pygame.transform.scale(grass, (SCREEN_WIDTH, SCREEN_HEIGHT - 400))

# shadow
king_mask = pygame.mask.from_surface(king).outline()
king_mask = [(x + (SCREEN_WIDTH / 2), y + ((SCREEN_HEIGHT / 2) - 20)) for x, y in king_mask]

# sun
sun_pos = pygame.Vector2(SCREEN_WIDTH, 0)
sun_target_pos = pygame.Vector2(SCREEN_WIDTH / 2, 386)
sun_angle = math.atan2((sun_pos.x - sun_target_pos.x), (sun_pos.y - sun_target_pos.y))

shadows = []

for x, y in king_mask:
    shadow_height = (500 - y) * 1.3
    shadow_width = shadow_height * math.tan(sun_angle)
    shadow_point = (x + shadow_width, y + shadow_height)
    shadows.append(shadow_point)

run = True
while run:  # game loop
    clock.tick(60)
    for event in pygame.event.get():  # event handling
        if event.type == pygame.QUIT:
            run = False
    # Draw images into screen
    screen.fill((0, 0, 0))
    screen.blit(sky, (0, 0))
    screen.blit(grass, (0, 500))
    screen.blit(king, (600, 386))
    pygame.draw.polygon(screen, (0, 0, 0), shadows)
    pygame.display.flip()

pygame.quit()
sys.exit()
