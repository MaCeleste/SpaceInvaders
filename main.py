import pygame, sys, random
from pygame.math import Vector2

# Initialise pygame

pygame.init()

# Set caption and icon

pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# Create the screen

screen = pygame.display.set_mode((800, 600))


# Player
class PLAYER:
    def __init__(self):
        self.playerImg = pygame.image.load('spaceship.png')
        self.playerX = 370
        self.playerY = 480

    def draw_player(self):
        screen.blit(self.playerImg, (self.playerX, self.playerY))


# Game loop

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    player = PLAYER()
    player.draw_player()
    pygame.display.update()
