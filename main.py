import pygame, sys, random, math
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
        self.alien = ALIEN()

    def draw_elements(self):
        self.player.move_player()
        self.bullet.fire_bullet(self.bullet.bullet_x_pos)
        self.alien.move_alien()

    def check_collision(self):


# Player
class PLAYER:
    def __init__(self):
        self.playerImg = pygame.image.load('spaceship.png')
        self.player_movement = 0
        self.player_x_pos = 370
        self.player_y_pos = 480

    def move_player(self):
        self.player_x_pos = self.player_x_pos + self.player_movement
        if self.player_x_pos < 0:
            self.player_x_pos = 0
        elif self.player_x_pos > 736:
            self.player_x_pos = 736
        screen.blit(self.playerImg, (self.player_x_pos, self.player_y_pos))


# Bullet
class BULLET:
    def __init__(self):
        self.bulletImg = pygame.image.load('bullet.png')
        self.bullet_movement = 0
        self.bullet_fired = False
        self.bullet_y_pos = 448
        self.bullet_x_pos = 0

    def fire_bullet(self, x):
        # Move bullet along the y-axis when it's fired
        if self.bullet_fired:
            screen.blit(self.bulletImg, (x + 16, self.bullet_y_pos))
            self.bullet_y_pos -= self.bullet_movement
        # Reset bullet after it reaches the top of the screen
        if self.bullet_y_pos <= 0:
            self.bullet_fired = False
            self.bullet_y_pos = 448


# Alien
class ALIEN:
    def __init__(self):
        self.alienImg = pygame.image.load('alien.png')
        self.alien_y_pos = 15
        self.alien_x_pos = 0

        self.alien_x_movement = 2

    def move_alien(self):
        self.alien_x_pos += self.alien_x_movement
        if self.alien_x_pos > 736 or self.alien_x_pos < 0:
            self.alien_x_movement *= -1
            self.alien_y_pos += 32
        screen.blit(self.alienImg, (self.alien_x_pos, self.alien_y_pos))


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
                if not main_game.bullet.bullet_fired:
                    main_game.bullet.bullet_fired = True
                    main_game.bullet.bullet_x_pos = main_game.player.player_x_pos
                    main_game.bullet.bullet_movement = 10

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                main_game.player.player_movement = 0

    # Screen and fps
    screen.fill((0, 0, 0))
    clock.tick(fps)

    # Draw elements on the screen and update them
    main_game.draw_elements()

    pygame.display.update()
