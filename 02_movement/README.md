# Exercise 02 - Move a Sprite Character

## Goal

Make the player sprite move left, right, up, and down based on keyboard entry (WASD). 

When you run `main.py` right now you'll see a black screen with the character (the blue square) at the center of the screen. Your job is to add the code that moves the character when the player presses W, A, S, or D, at the speed determined by `PLAYER_SPEED`. 

## What's already done for you

- The window is created (640 x 480 pixels). 
- A game loop runs at 60 FPS. 
- The player sprite is loaded and painted on the screen at position `player_pos`. 

## What you need to do

Find the `TODO` comment in `main.py` and replace it with code that:

1. Determines what key(s) are pressed. 
2. Update the `player_pos` rect according to the corresponding key and the `PLAYER_SPEED`. 

### Optional elements you could add

1. Use `rect.clamp_ip(screen.get_rect())` to keep the player on the screen. 
2. Hold Shift to move faster (check `keys[pygame.K_LSHIFT]` and multiple the players speed)
3. Place a target sprite (you can use `enemy.png`) at a random position. When the player reaches it (`player_pos.colliderect(target_pos)`) move the target somewhere new. 

## Key concepts

- **Event handling**: Inside the game loop you are looking for events (like keys being pressed). 
- **Key press vs key down**: In this exercise you want to look at the array of keys being pressed. If you use the KEYDOWN event you would only move once per key press. 
- **Constraints**: You need to constrain the character to the screen rect or else the player could move it off the screen into the infinite void. 

## How to run

```
cd 02_movement
python main.py
```

## You're done when...

Your blue square character responds to the W, A, S, and D keys and moves around the screen. 