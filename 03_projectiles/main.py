import os
import pygame

# ── Setup ────────────────────────────────────────────────────────────
pygame.init()

SCREEN_WIDTH  = 640
SCREEN_HEIGHT = 480
PLAYER_SPEED  = 200
BULLET_SPEED  = 400

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Exercise 03 - Shoot Projectiles")
clock = pygame.time.Clock()

assets_dir = os.path.join(os.path.dirname(__file__), "..", "assets")
player_image     = pygame.image.load(os.path.join(assets_dir, "player.png")).convert_alpha()
projectile_image = pygame.image.load(os.path.join(assets_dir, "projectile.png")).convert_alpha()

player_pos = player_image.get_rect()
player_pos.center = screen.get_rect().center

# Each projectile is a dict with keys: "rect" and "dx", "dy"
projectiles = []

def spawn_projectile(x, y, dx, dy):
    # Get a Rect the same size as the projectile image.
    # We'll use this rect to track where the bullet is on screen.
    rect = projectile_image.get_rect()

    # Place the bullet so its center starts at (x, y) — usually the player's center.
    rect.center = (x, y)

    # Add a new bullet to the list as a dict so we can store multiple pieces of
    # information together: where it is (rect) and how fast it moves (dx, dy).
    # dx is the horizontal speed (negative = left, positive = right).
    # dy is the vertical speed  (negative = up,   positive = down).
    projectiles.append({"rect": rect, "dx": dx, "dy": dy})

# ── Game Loop ────────────────────────────────────────────────────────
running = True
while running:
    dt = clock.tick(60) / 1000  # seconds since last frame

    # — Event handling —
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # — Update: player movement (WASD) —
    if keys[pygame.K_w]:
        player_pos.y += PLAYER_SPEED * dt
    if keys[pygame.K_s]:
        player_pos.y += PLAYER_SPEED * dt
    if keys[pygame.K_a]:
        player_pos.x -= PLAYER_SPEED * dt
    if keys[pygame.K_d]:
        player_pos.x += PLAYER_SPEED * dt
    player_pos.clamp_ip(screen.get_rect())

    # — Update: shooting (arrow keys) —
    # TODO: When an arrow key is pressed, call spawn_projectile() to fire
    #       a bullet from the center of the player in that direction.
    #
    # Hints:
    #   - pygame.K_UP, K_DOWN, K_LEFT, K_RIGHT are the arrow key constants.
    #   - spawn_projectile takes (x, y, dx, dy).
    #     x, y  → starting position (use player_pos.centerx / .centery)
    #     dx, dy → direction and speed. For example, shooting right means
    #              dx = BULLET_SPEED, dy = 0. Shooting up means dy = -BULLET_SPEED.
    #   - Only spawn one bullet per key press, not one per frame.
    #     Use a KEYDOWN event in the event loop above instead of get_pressed().

    # — Update: move projectiles —
    # TODO: Loop over the projectiles list and move each one.
    #
    # Hints:
    #   - Each projectile is a dict. Access its rect with p["rect"].
    #   - Move it by adding p["dx"] * dt to rect.x and p["dy"] * dt to rect.y.
    #   - Build a new list that keeps only the projectiles still on screen.
    #     A projectile is off screen when its rect no longer overlaps the
    #     screen rect. Use screen.get_rect().colliderect(p["rect"]) to check.

    # — Draw —
    screen.fill((0, 0, 0))
    screen.blit(player_image, player_pos)

    for p in projectiles:
        screen.blit(projectile_image, p["rect"])

    pygame.display.flip()

pygame.quit()
