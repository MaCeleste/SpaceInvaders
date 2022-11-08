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
        self.aliens = pygame.sprite.Group()
        self.create_aliens()

    def create_aliens(self):
        for alien in range(10):
            new_alien = ALIEN(random.randrange(0, 700), random.randrange(0, 250))
            self.aliens.add(new_alien)

    def run(self):
        self.player.move_player()
        self.bullet.fire_bullet(self.bullet.rect.x)
        self.aliens.draw(screen)
        # If statement added to check if there are any aliens on the screen left
        if self.aliens:
            self.aliens.update()
        self.check_collision()

    def check_collision(self):
        if pygame.sprite.spritecollide(self.bullet, self.aliens, True):
            self.bullet.kill()


#     if self.alien.alienRect.colliderect(self.bullet.bulletRect):
#        print('hey')

# Player
class PLAYER:
    def __init__(self):
        self.player_x_pos = 370
        self.player_y_pos = 480
        self.playerImg = pygame.image.load('spaceship.png')
        self.playerRect = self.playerImg.get_rect(topleft=[self.player_x_pos, self.player_y_pos])
        self.player_movement = 0

    def move_player(self):
        self.playerRect.x = self.playerRect.x + self.player_movement
        if self.playerRect.x < 0:
            self.playerRect.x = 0
        elif self.playerRect.x > 736:
            self.playerRect.x = 736
        screen.blit(self.playerImg, self.playerRect)


# Bullet
class BULLET(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.bullet_y_pos = 448
        self.bullet_x_pos = 100
        self.image = pygame.image.load('bullet.png')
        self.rect = self.image.get_rect(topleft=[self.bullet_x_pos, self.bullet_y_pos])
        self.bullet_movement = 0
        self.bullet_fired = False

    def fire_bullet(self, x):
        # Move bullet along the y-axis when it's fired
        if self.bullet_fired:
            screen.blit(self.image, self.rect)
            self.rect.y -= self.bullet_movement
        # Reset bullet after it reaches the top of the screen
        if self.rect.y <= 0:
            self.bullet_fired = False
            self.rect.y = 448


# Alien
class ALIEN(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.image = pygame.image.load('alien.png')
        self.rect = self.image.get_rect(topleft=[x_pos, y_pos])
        # self.alien_y_pos = 15
        # self.alien_x_pos = 0
        self.alien_x_movement = 2

    def update(self):
        self.rect.x += self.alien_x_movement
        if self.rect.x > 736 or self.rect.x < 0:
            self.alien_x_movement *= -1
            self.rect.y += 32


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
                    main_game.bullet.rect.x = main_game.player.playerRect.x + 16
                    main_game.bullet.bullet_movement = 10

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                main_game.player.player_movement = 0

    # Screen and fps
    screen.fill((0, 0, 0))
    clock.tick(fps)

    main_game.run()

    pygame.display.update()
