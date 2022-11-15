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
        self.aliens = pygame.sprite.Group()
        self.create_aliens()
        self.bullets = pygame.sprite.Group()
        self.aliens_direction = 1

    def create_aliens(self):
        for row_index, row in enumerate(range(4)):
            for col_index, col in enumerate(range(5)):
                x = col_index * 80
                y = row_index * 80
                new_alien = ALIEN(x, y)
                self.aliens.add(new_alien)

    def move_aliens(self):
        all_aliens = self.aliens.sprites()
        for alien in all_aliens:
            if alien.rect.right >= 800 or alien.rect.left <= 0:
                self.aliens_direction = self.aliens_direction * -1
                self.move_aliens_down()
                break

    def move_aliens_down(self):
        all_aliens = self.aliens.sprites()
        for alien in all_aliens:
            alien.rect.y += 10

    def run(self):
        self.player.move_player()
        self.aliens.draw(screen)
        # If statement added to check if there are any aliens on the screen left
        if self.aliens:
            self.aliens.update(self.aliens_direction)
        self.move_aliens()
        self.bullets.draw(screen)
        self.bullets.update()
        self.check_collision()


    def fire_bullet(self):
        self.bullets.add(BULLET(self.player.playerRect.center))

    def check_collision(self):
        for bullet in self.bullets:
            if pygame.sprite.spritecollide(bullet, self.aliens, True):
                bullet.kill()


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
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((4, 20))
        self.image.fill('white')
        self.rect = self.image.get_rect(center=pos)

        self.bullet_movement = 2
        self.bullet_fired = False

    def update(self):
        self.rect.y -= 10
        if self.rect.y <= 10:
            self.kill()


# Alien
class ALIEN(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.image = pygame.image.load('alien.png')
        self.rect = self.image.get_rect(topleft=[x_pos, y_pos])
        self.speed = 2

    def update(self, direction):
        self.rect.x += direction



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
                main_game.fire_bullet()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                main_game.player.player_movement = 0

    # Screen and fps
    screen.fill((0, 0, 0))
    clock.tick(fps)

    main_game.run()

    pygame.display.update()
