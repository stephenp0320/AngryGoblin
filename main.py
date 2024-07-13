import pygame
from sys import exit
import random

pygame.init()
screen = pygame.display.set_mode((1200, 600))  # Increased screen size
clock = pygame.time.Clock()
game_font = pygame.font.Font(None, 30)

jump_sound = pygame.mixer.Sound('sounds/BounceYoFrankie.flac')
death_sound = pygame.mixer.Sound('sounds/death_bell_sound_effect.wav')
scream_sound = pygame.mixer.Sound('sounds/scream_horror1.mp3')
pygame.mixer.music.load('sounds/background.mp3')
pygame.mixer.music.play(-1)

game_background = pygame.image.load('images/sky.png')
game_background = pygame.transform.scale(game_background, (1200, 600))  # Adjust background size
game_enemy_background = pygame.transform.scale(pygame.image.load('images/JWDLx5AZBtI.jpg'), (1200, 600))
game_goblin = pygame.image.load('images/goblin4x.png')
game_orb = pygame.image.load('images/orb4x.png')
game_enemy = pygame.image.load('images/minotaur4x.png')
game_heart = pygame.image.load('images/heart4x.png')
game_title = game_font.render('Angry Goblin', False, 'Black')
# game_heart_count = game_font.render('Hearts collected: ', False, 'Black')

bgX = 0
bgX2 = game_background.get_width()

gob_pos_x = 50
gob_pos_y = 250
gob_vel_y = 0
gravity = 1
jump_power = -15
game_started = False
hearts_collected = 0

orb_pos_x = random.randint(1200, 1400)  # Adjust initial position for larger screen
orb_pos_y = random.randint(0, 550)
enemy_pos_x = random.randint(1400, 1600)  # Adjust initial position for larger screen
enemy_pos_y = random.randint(0, 550)
hrt_pos_x = random.randint(1000, 1300)  # Adjust initial position for larger screen
hrt_pos_y = random.randint(0, 550)
hrt_is_orb = False  # State variable to track if the heart is an orb

dark_poison = False
dark_poison_start = 0
blackout_duration = 3000  # 3 seconds

while True:
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not game_started:
                    game_started = True
                gob_vel_y = jump_power
                jump_sound.play()

    if game_started:
        if dark_poison:
            if current_time - dark_poison_start < blackout_duration:  # Draw the enemy background
                pygame.display.update()
                continue
            else:
                dark_poison = False

        bgX -= 1.4
        bgX2 -= 1.4
        if bgX < game_background.get_width() * -1:
            bgX = game_background.get_width()

        if bgX2 < game_background.get_width() * -1:
            bgX2 = game_background.get_width()

        # Apply gravity
        gob_vel_y += gravity
        gob_pos_y += gob_vel_y

        # Check if goblin hits the ground
        if gob_pos_y >= 550:
            gob_pos_y = 550
            print("Game Over!")
            death_sound.play()
            pygame.time.delay(2000)  # Wait for 2 seconds to allow the sound to play
            pygame.quit()
            exit()

        # Check if goblin goes too high
        if gob_pos_y <= 0:
            gob_pos_y = 0
            gob_vel_y = 0

        # Randomly change heart to orb
        if not hrt_is_orb and random.randint(0, 500) == 0:
            hrt_is_orb = True

        # Move the orb and heart
        orb_pos_x -= 10
        if orb_pos_x < -50:
            orb_pos_x = random.randint(1200, 1400)  # Adjust respawn position for larger screen
            orb_pos_y = random.randint(0, 550)

        hrt_pos_x -= 5
        if hrt_pos_x < -50:
            hrt_pos_x = random.randint(1000, 1300)  # Adjust respawn position for larger screen
            hrt_pos_y = random.randint(0, 550)
            hrt_is_orb = False  # Reset state when repositioning

        enemy_pos_x -= 4  # Adjust enemy speed
        if enemy_pos_x < -50:
            enemy_pos_x = random.randint(1400, 1600)  # Adjust respawn position for larger screen
            enemy_pos_y = random.randint(0, 550)

    # Draw the background
    screen.blit(game_background, (bgX, 0))
    screen.blit(game_background, (bgX2, 0))

    # Draw the goblin, orb, and heart
    screen.blit(game_goblin, (gob_pos_x, gob_pos_y))
    screen.blit(game_enemy, (enemy_pos_x, enemy_pos_y))
    screen.blit(game_orb, (orb_pos_x, orb_pos_y))
    if hrt_is_orb:
        screen.blit(game_orb, (hrt_pos_x, hrt_pos_y))
    else:
        screen.blit(game_heart, (hrt_pos_x, hrt_pos_y))
    screen.blit(game_title, (500, 10))  # Adjust title position for larger screen

    game_heart_count = game_font.render(f'Hearts collected: {hearts_collected}', False, 'Black')
    screen.blit(game_heart_count, (10, 10))

    # Create rectangles for collision detection
    goblin_rect = game_goblin.get_rect(topleft=(gob_pos_x, gob_pos_y))
    enemy_rect = game_enemy.get_rect(topleft=(enemy_pos_x, enemy_pos_y))
    orb_rect = game_orb.get_rect(topleft=(orb_pos_x, orb_pos_y))
    heart_orb_rect = game_orb.get_rect(topleft=(hrt_pos_x, hrt_pos_y)) if hrt_is_orb else game_heart.get_rect(
        topleft=(hrt_pos_x, hrt_pos_y))

    # Check for collision if the game has started
    if game_started:
        if goblin_rect.colliderect(orb_rect):
            print("Hit an orb!")
            death_sound.play()
            pygame.time.delay(500)  # Wait for 0.5 seconds to allow the sound to play
            hearts_collected -= 1
            orb_pos_x = random.randint(1200, 1400)
            orb_pos_y = random.randint(0, 550)
            if hearts_collected <= 0:
                print("Game Over!")
                pygame.quit()
                exit()

        if goblin_rect.colliderect(enemy_rect):
            print("Poisoned!")
            scream_sound.play()
            pygame.time.delay(500)  # Wait for 0.5 seconds to allow the sound to play
            dark_poison = True
            dark_poison_start = current_time
            enemy_pos_x = random.randint(1200, 1400)
            enemy_pos_y = random.randint(0, 550)

        if goblin_rect.colliderect(heart_orb_rect):
            if hrt_is_orb:
                print("Game Over!")
                death_sound.play()
                pygame.time.delay(2000)  # Wait for 2 seconds to allow the sound to play
                pygame.quit()
                exit()
            else:
                hearts_collected += 1
                print(f"Collected Hearts: {hearts_collected}")
                hrt_pos_x = random.randint(1000, 1300)
                hrt_pos_y = random.randint(0, 550)
                hrt_is_orb = False  # Reset state when collected

    pygame.display.update()
    clock.tick(60)
