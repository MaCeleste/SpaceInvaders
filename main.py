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

# Define FPS

clock = pygame.time.Clock()
fps = 60


# Player
class PLAYER:
    def __init__(self):
        self.playerImg = pygame.image.load('spaceship.png')
        self.movement = 0
        self.x_pos = 370
        self.y_pos = 480

    def draw_player(self, x, y):
        screen.blit(self.playerImg, (x, y))

    def move_player(self):
        player.x_pos += player.movement
        if player.x_pos < 0:
            player.x_pos = 0
        elif player.x_pos > 736:
            player.x_pos = 736

# Create instance of a player

player = PLAYER()

# Game loop
running = True
while running:
    # Event listener

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.movement = -5
            if event.key == pygame.K_RIGHT:
                player.movement = 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.movement = 0

    # Screen and fps
    screen.fill((0, 0, 0))
    clock.tick(fps)

    player.draw_player(player.x_pos, player.y_pos)
    player.move_player()

    pygame.display.update()
