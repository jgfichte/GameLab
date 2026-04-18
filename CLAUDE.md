# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Purpose

This is an educational project where a 13-year-old is learning to code by building a top-down 2D roguelike in the style of *The Binding of Isaac*. Each exercise introduces exactly one new concept while reusing everything learned before. Exercises are completed in order: 01 → 02 → 03 → 04 → 05.

Keep explanations and code appropriate for a beginner. Prefer clarity over cleverness. Avoid abstractions or patterns not yet introduced in prior exercises.

## Running Exercises

```bash
# Install dependencies (one-time)
pip install -r requirements.txt

# Run an exercise (from its folder or with a path)
python 01_display_sprite/main.py
python 02_movement/main.py
```

Each `main.py` is a standalone script — no build step, no test suite.

## Exercise Structure

Every exercise folder contains:
- `main.py` — starter code with scaffolding and `# TODO` comments marking what the student implements
- `README.md` — goal, hints, key concepts, and success criteria

Shared sprite assets live in `assets/` and are loaded via relative path `../assets` so exercises work regardless of working directory.

## Code Patterns

All exercises share the same skeleton:

```
Setup (pygame.init, screen, clock, asset loading)
  └─ Game Loop
       ├─ Event handling  (pygame.event.get)
       ├─ Update          (input reading, position math)
       └─ Draw            (screen.fill, blit, display.flip)
```

Constants (`SCREEN_WIDTH`, `SCREEN_HEIGHT`, `PLAYER_SPEED`, etc.) are defined at the top. The clock runs at 60 FPS. Delta time (`dt`) is provided for frame-rate-independent movement starting in exercise 02.

## Planned Exercise Progression

| # | Folder | New Concept |
|---|--------|-------------|
| 01 | `01_display_sprite/` | `blit`, `Rect`, game loop |
| 02 | `02_movement/` | keyboard input, `dt` |
| 03 | `03_projectiles/` | lists of game objects, spawn/destroy |
| 04 | `04_collision/` | `colliderect`, safe list removal |
| 05 | `05_rooms/` | game state, data-driven design |

Exercises 03–05 are not yet implemented. When adding a new exercise, follow the established pattern: one `main.py` with TODO scaffolding and one `README.md` explaining the goal and hints.
