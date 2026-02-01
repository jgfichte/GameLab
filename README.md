# GameLab: Learn to Build a Roguelike

A series of exercises that teach game programming with Python and Pygame.
Each exercise builds on skills from the previous one, working toward a
top-down 2D roguelike in the style of *The Binding of Isaac*.

## Prerequisites

- Python 3.12+
- Pygame (`pip install pygame`)

## Folder Structure

```
GameLab/
  SPEC.md
  assets/
    player.png        (32x32 top-down character sprite)
    projectile.png    (8x8 bullet/tear sprite)
    enemy.png         (32x32 enemy sprite)
  01_display_sprite/
  02_movement/
  03_projectiles/
  04_collision/
  05_rooms/
```

Each exercise folder contains:

- `main.py` — starter code with scaffolding and TODO comments
- `README.md` — describes the goal, gives hints, and lists what to learn

Shared art assets live in `assets/` and are loaded via relative paths.

---

## Exercise 01 — Display a Sprite

**Folder:** `01_display_sprite/`

**Provided:** A working game loop that opens a 640x480 window and fills it
with a black background each frame. The player sprite is loaded from
`assets/player.png` into a variable called `player_image`.

**Task:** Draw the sprite so it appears at the center of the window.

**Skills learned:**
- Understanding the game loop (event handling, update, draw)
- Screen coordinates and surfaces
- `surface.blit()` and `rect.center`

---

## Exercise 02 — WASD Movement

**Folder:** `02_movement/`

**Provided:** The sprite is already drawn at the center of the screen.
A `player_pos` list `[x, y]` holds the player's position. The game loop
reads keyboard state with `pygame.key.get_pressed()` and stores it in a
variable called `keys`.

**Task:** Update `player_pos` each frame so the sprite moves up (W),
left (A), down (S), and right (D) at a speed defined by `PLAYER_SPEED`.

**Skills learned:**
- Reading keyboard input
- Updating position over time
- Frame-rate-independent movement (`dt` is provided)

---

## Exercise 03 — Shooting Projectiles

**Folder:** `03_projectiles/`

**Provided:** A moving player from the previous exercise. A `projectiles`
list is defined. A helper function `spawn_projectile(x, y, dx, dy)` creates
a projectile dict and appends it to the list. The draw loop already iterates
over `projectiles` and draws each one.

**Task:**
1. When the arrow keys are pressed, call `spawn_projectile` to fire a
   projectile in that direction from the player's position.
2. In the update section, move each projectile by its `dx`/`dy` each frame.
3. Remove projectiles that leave the screen.

**Skills learned:**
- Working with lists of game objects
- Spawning and destroying entities at runtime
- Separating input (arrows) from movement (WASD)

---

## Exercise 04 — Collision Detection

**Folder:** `04_collision/`

**Provided:** A moving player that shoots projectiles. A list called
`enemies` is pre-populated with enemy dicts, each having an `"x"`, `"y"`,
and `"rect"` key. Enemies are drawn on screen but nothing happens when
projectiles hit them.

**Task:**
1. Check whether any projectile's rect overlaps any enemy's rect
   (use `pygame.Rect.colliderect`).
2. When a hit is detected, remove both the projectile and the enemy.
3. (Bonus) Prevent the player from walking through enemies.

**Skills learned:**
- Rectangle-based collision detection
- Iterating and removing items from lists safely
- Game logic: hit detection and entity removal

---

## Exercise 05 — Room Transitions

**Folder:** `05_rooms/`

**Provided:** Everything from previous exercises. A `rooms` dict maps
room names (`"start"`, `"north"`, `"east"`) to enemy layouts. A variable
`current_room` tracks which room is active. Door rects are drawn at the
top, bottom, left, and right edges of the screen.

**Task:**
1. Detect when the player walks into a door rect.
2. Change `current_room` to the connected room.
3. Reset the player's position to the opposite side of the screen
   (e.g., entering the top door places the player at the bottom).
4. Load the new room's enemies into the `enemies` list.

**Skills learned:**
- Managing game state (rooms, transitions)
- Data-driven design (rooms defined as data, not code)
- Putting all previous skills together

---

## Progression Notes

The exercises are meant to be completed in order. Each one introduces
exactly one new concept while reusing everything learned before. If an
exercise feels too hard, go back and re-read the previous README — the
answer usually builds on something already covered.

After completing all five exercises, the next steps toward a full
roguelike could include:

- Enemy AI (movement, shooting back)
- Health and damage
- Procedural room generation
- Items and power-ups
- A boss fight
