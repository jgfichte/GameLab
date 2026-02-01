# Exercise 01 — Display a Sprite

## Goal

Make the player sprite appear at the center of the window.

When you run `main.py` right now you'll see a black screen — the sprite
is loaded but never drawn. Your job is to add the code that draws it.

## What's already done for you

- The window is created (640 x 480 pixels).
- A game loop runs at 60 FPS and clears the screen to black each frame.
- The player image is loaded into a variable called `player_image`.

## What you need to do

Find the `TODO` comment in `main.py` and replace it with code that:

1. Gets a `Rect` for the screen and a `Rect` for the sprite.
2. Sets the sprite rect's center to the screen rect's center.
3. Draws (`blit`) the image onto the screen at that position.

## Key concepts

- **Surface**: Any image or drawable area in Pygame. The screen itself
  is a surface, and so is `player_image`.
- **Rect**: A rectangle that stores position and size. Every surface can
  give you one with `.get_rect()`.
- **blit**: Short for "block image transfer" — it copies one surface
  onto another. `screen.blit(image, rect)` draws `image` at the
  position described by `rect`.

## How to run

```
cd 01_display_sprite
python main.py
```

(Make sure you've already run `python assets/generate_assets.py` from the
GameLab root to create the placeholder sprites.)

## You're done when...

You see a blue square sitting right in the middle of the black window.
