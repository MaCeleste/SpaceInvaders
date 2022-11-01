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


# Main game class
class MAIN:
    def __init__(self):
        self.player = PLAYER()
        self.bullet = BULLET()

    def draw_elements(self):
        self.player.draw_player()
        self.bullet.draw_bullet(self.player.player_x_pos, self.player.player_y_pos)

    def update(self):
        self.player.move_player()


# Player
class PLAYER:
    def __init__(self):
        self.playerImg = pygame.image.load('spaceship.png')
        self.player_movement = 0
        self.player_x_pos = 370
        self.player_y_pos = 480

    def draw_player(self):
        screen.blit(self.playerImg, (self.player_x_pos, self.player_y_pos))

    def move_player(self):
        self.player_x_pos = self.player_x_pos + self.player_movement
        if self.player_x_pos < 0:
            self.player_x_pos = 0
        elif self.player_x_pos > 736:
            self.player_x_pos = 736


# Bullet
class BULLET:
    def __init__(self):
        self.bulletImg = pygame.image.load('bullet.png')
        self.movement = 0
        self.bullet_fired = False

    def draw_bullet(self, x, y):
        if self.bullet_fired:
            screen.blit(self.bulletImg, (x, y))


# Create instance of a new game

main_game = MAIN()

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
                main_game.player.player_movement = -5
            if event.key == pygame.K_RIGHT:
                main_game.player.player_movement = 5
            if event.key == pygame.K_SPACE:
                main_game.bullet.bullet_fired = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                main_game.player.player_movement = 0

    # Screen and fps
    screen.fill((0, 0, 0))
    clock.tick(fps)

    # Draw elements on the screen and update them
    main_game.draw_elements()
    main_game.update()

    pygame.display.update()
