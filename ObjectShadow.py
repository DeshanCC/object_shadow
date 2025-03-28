import pygame, math, sys

pygame.init()
clock = pygame.time.Clock()
SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Load images
king = pygame.image.load('./assets/king.png').convert_alpha()
king = pygame.transform.scale(king, (80, 130))
sky = pygame.image.load('./assets/sky.png').convert_alpha()
sky = pygame.transform.scale(sky, (SCREEN_WIDTH, SCREEN_HEIGHT))
grass = pygame.image.load('./assets/grass.png').convert_alpha()
grass = pygame.transform.scale(grass, (SCREEN_WIDTH, SCREEN_HEIGHT - 400))
sun_img = pygame.image.load('./assets/sun.png').convert_alpha()
sun_img = pygame.transform.scale(sun_img, (200, 200))

# shadow
king_mask = pygame.mask.from_surface(king).outline()
king_mask = [(x + SCREEN_WIDTH / 2, y + (SCREEN_HEIGHT / 2) - 20) for x, y in king_mask]

sun_target = pygame.Vector2(SCREEN_WIDTH / 2, 386)

# Define sun positions for top left, middle, and right
options = {"Top Left": pygame.Vector2(0, 15),
           "Top Middle": pygame.Vector2(SCREEN_WIDTH / 2, 15),
           "Top Right": pygame.Vector2(SCREEN_WIDTH - 150, 0)}
selected = "Top Right"
sun_pos = options[selected]


def get_shadows():
    angle = math.atan2(sun_pos.x - sun_target.x, sun_pos.y - sun_target.y)
    points = []
    for x, y in king_mask:
        shadow_height = (500 - y) * 1.3
        shadow_width = shadow_height * math.tan(angle)
        points.append((x + shadow_width, y + shadow_height))
    return points


shadows = get_shadows()

# Dropdown UI variables
dropdown_rect = pygame.Rect(10, 10, 120, 30)
font = pygame.font.SysFont(None, 24)
dropdown_active = False

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if dropdown_rect.collidepoint(event.pos):
                dropdown_active = not dropdown_active
            elif dropdown_active:
                for i, key in enumerate(options.keys()):
                    opt_rect = pygame.Rect(10, 10 + 30 * (i + 1), 120, 30)
                    if opt_rect.collidepoint(event.pos):
                        selected = key
                        sun_pos = options[selected]
                        shadows = get_shadows()
                        dropdown_active = False

    screen.fill((0, 0, 0))
    screen.blit(sky, (0, 0))
    screen.blit(grass, (0, 500))
    screen.blit(king, (600, 386))
    pygame.draw.polygon(screen, (0, 0, 0), shadows)
    pygame.draw.rect(screen, (200, 200, 200), dropdown_rect)
    txt = font.render(selected, True, (0, 0, 0))
    screen.blit(txt, (dropdown_rect.x + 5, dropdown_rect.y + 5))

    # Adjust sun position to center the sun image
    screen.blit(sun_img, (sun_pos.x, sun_pos.y))

    if dropdown_active:
        for i, key in enumerate(options.keys()):
            opt_rect = pygame.Rect(10, 10 + 30 * (i + 1), 120, 30)
            pygame.draw.rect(screen, (200, 200, 200), opt_rect)
            txt = font.render(key, True, (0, 0, 0))
            screen.blit(txt, (opt_rect.x + 5, opt_rect.y + 5))
    pygame.display.flip()
