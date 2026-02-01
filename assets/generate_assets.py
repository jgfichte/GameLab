"""Run this once to create placeholder sprite images for the exercises."""

import pygame
import os

pygame.init()

dir = os.path.dirname(__file__)

# Player: 32x32 blue square with a lighter "face"
player = pygame.Surface((32, 32), pygame.SRCALPHA)
player.fill((50, 100, 220))
pygame.draw.rect(player, (180, 210, 255), (8, 8, 16, 16))  # face
pygame.image.save(player, os.path.join(dir, "player.png"))

# Projectile: 8x8 yellow circle
projectile = pygame.Surface((8, 8), pygame.SRCALPHA)
pygame.draw.circle(projectile, (255, 255, 80), (4, 4), 4)
pygame.image.save(projectile, os.path.join(dir, "projectile.png"))

# Enemy: 32x32 red square with darker "eyes"
enemy = pygame.Surface((32, 32), pygame.SRCALPHA)
enemy.fill((200, 50, 50))
pygame.draw.rect(enemy, (80, 20, 20), (6, 8, 8, 8))
pygame.draw.rect(enemy, (80, 20, 20), (18, 8, 8, 8))
pygame.image.save(enemy, os.path.join(dir, "enemy.png"))

print("Created player.png, projectile.png, enemy.png in assets/")
