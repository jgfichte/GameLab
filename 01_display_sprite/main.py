import os
import pygame

# ── Setup ────────────────────────────────────────────────────────────
pygame.init()

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Exercise 01 – Display a Sprite")
clock = pygame.time.Clock()

# Load the player sprite
assets_dir = os.path.join(os.path.dirname(__file__), "..", "assets")
player_image = pygame.image.load(os.path.join(assets_dir, "player.png")).convert_alpha()

# ── Game Loop ────────────────────────────────────────────────────────
running = True
while running:
    # — Event handling —
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # — Drawing —
    screen.fill((0, 0, 0))  # clear the screen to black

    # TODO: Draw player_image so it appears at the center of the screen.
    #
    # Hints:
    #   - screen.get_rect() gives you a Rect the size of the window.
    #   - player_image.get_rect() gives you a Rect the size of the sprite.
    #   - You can set a Rect's .center to another Rect's .center.
    #   - screen.blit(image, rect) draws an image at the rect's position.

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
