# Exercise 03 — Shoot Projectiles

## Goal

Make the player shoot projectiles with the arrow keys — up, down, left, and right.

When you run `main.py` you'll see the player moving with WASD as before, but pressing
the arrow keys does nothing yet. Your job is to make bullets fly.

## What's already done for you

- WASD movement from Exercise 02 is wired up and working.
- The `projectile_image` is loaded from `assets/projectile.png`.
- A `projectiles` list is defined to hold all active bullets.
- A helper function `spawn_projectile(x, y, dx, dy)` creates a bullet dict and adds it to the list.
- The draw loop already draws every projectile in the list — you just need to fill the list.

## What you need to do

Start by running the program and finding the bug in the character movement. Fix the bug before proceeding. Once you have done that, there are two `TODO` comments in `main.py`:

**TODO 1 — Shooting**

In the event loop, detect arrow key presses and call `spawn_projectile` to fire a bullet
from the center of the player in that direction.

**TODO 2 — Moving and removing projectiles**

Each frame, move every projectile by its `dx` and `dy`, then remove any that have left the screen.

## Key concepts

- **Dicts**: A `dict` (short for "dictionary") lets you group related values together
  under named keys. Instead of separate variables for a bullet's x, y, dx, and dy, a
  dict keeps them all in one place: `p["rect"]`, `p["dx"]`, `p["dy"]`. Think of it like
  a label maker — each label (key) points to a value.
  [Learn more about dicts on W3Schools](https://www.w3schools.com/python/python_dictionaries.asp)

- **Lists of game objects**: The `projectiles` list holds every bullet currently alive.
  Spawning adds to the list; going off-screen removes from it. This pattern — a list you
  add to and remove from — is how almost every game manages entities.
- **KEYDOWN vs get_pressed**: `get_pressed()` returns `True` every frame the key is held,
  which would spawn hundreds of bullets per second. `KEYDOWN` fires once per press, which
  is what you want for shooting.
- **List rebuilding**: The safe way to remove items while looping is to build a new list
  of the items you want to *keep*, then replace the old list with it.

  ```python
  projectiles = [p for p in projectiles if keep_condition(p)]
  ```

## How to run

```
cd 03_projectiles
python main.py
```

## You're done when...

- Pressing an arrow key fires a small yellow bullet from the player.
- Each bullet travels in a straight line and disappears when it leaves the screen.
- WASD movement still works normally at the same time.

## Optional challenges

1. **Rate limiting**: Add a cooldown so the player can only fire once every 0.3 seconds.
   Keep a `last_shot` timer and compare it to `pygame.time.get_ticks()`.
2. **Diagonal shooting**: Allow holding two arrow keys at once to fire diagonally.
3. **Bullet limit**: Cap the `projectiles` list at 5 bullets so the screen doesn't fill up.
