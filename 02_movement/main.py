import os
import pygame

# Setup
pygame.init()

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
PLAYER_SPEED = 1
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Exercise 02 - Move the character")
clock = pygame.time.Clock()

# Load the player sprite
assets_dir = os.path.join(os.path.dirname(__file__), "..", "assets")
player_image = pygame.image.load(os.path.join(assets_dir, "player.png")).convert_alpha()
player_pos = player_image.get_rect()
player_pos.center = screen.get_rect().center

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # TODO: Detect the keypress event and adjust the player's position
        #
        # Hints:
        #   - Use pygame.key.get_pressed() to get an array of all the keys currently pressed
        #   - When the key is down you want to adjust the player_pos by PLAYER_SPEED

    # Drawing
    screen.fill((0, 0, 0)) # clear the screen to black
    screen.blit(player_image, player_pos)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()