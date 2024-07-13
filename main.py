import pygame
from sys import exit
import random

pygame.init()
screen = pygame.display.set_mode((1200, 600))  # Increased screen size
clock = pygame.time.Clock()
game_font = pygame.font.Font(None, 30)

jump_sound = pygame.mixer.Sound('sounds/BounceYoFrankie.flac')
death_sound = pygame.mixer.Sound('sounds/death_bell_sound_effect.wav')


pygame.mixer.music.load('sounds/background.mp3')
pygame.mixer.music.play(-1)




game_background = pygame.image.load('images/sky.png')
game_background = pygame.transform.scale(game_background, (1200, 600))  # Adjust background size
game_goblin = pygame.image.load('images/goblin4x.png')
game_orb = pygame.image.load('images/orb4x.png')
game_heart = pygame.image.load('images/heart4x.png')
game_title = game_font.render('Angry Goblin', False, 'Black')
game_heart_count = game_font.render('Hearts collected: ', False, 'Black')

bgX = 0
bgX2 = game_background.get_width()

gob_pos_x = 50
gob_pos_y = 250
gob_vel_y = 0
gravity = 1
jump_power = -15
game_started = False

orb_pos_x = random.randint(1200, 1400)  # Adjust initial position for larger screen
orb_pos_y = random.randint(0, 550)
hrt_pos_x = random.randint(1000, 1300)  # Adjust initial position for larger screen
hrt_pos_y = random.randint(0, 550)

while True:
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
            print("game over")
            #pygame.time.delay(2000)
            pygame.quit()
            exit()

        # Check if goblin goes too high
        if gob_pos_y <= 0:
            gob_pos_y = 0
            gob_vel_y = 0

        # Move the orb and heart
        orb_pos_x -= 5
        if orb_pos_x < -50:
            orb_pos_x = random.randint(1200, 1400)  # Adjust respawn position for larger screen
            orb_pos_y = random.randint(0, 550)

        hrt_pos_x -= 5
        if hrt_pos_x < -50:
            hrt_pos_x = random.randint(1000, 1300)  # Adjust respawn position for larger screen
            hrt_pos_y = random.randint(0, 550)

    # Draw the background
    screen.blit(game_background, (bgX, 0))
    screen.blit(game_background, (bgX2, 0))

    # Draw the goblin, orb, and heart
    screen.blit(game_goblin, (gob_pos_x, gob_pos_y))
    screen.blit(game_orb, (orb_pos_x, orb_pos_y))
    screen.blit(game_heart, (hrt_pos_x, hrt_pos_y))
    screen.blit(game_title, (500, 10))  # Adjust title position for larger screen
    screen.blit(game_heart_count, (10, 10))

    # Create rectangles for collision detection
    goblin_rect = game_goblin.get_rect(topleft=(gob_pos_x, gob_pos_y))
    orb_rect = game_orb.get_rect(topleft=(orb_pos_x, orb_pos_y))

    # Check for collision if the game has started
    if game_started and goblin_rect.colliderect(orb_rect):
        print("Game Over!")
        pygame.quit()
        exit()

    pygame.display.update()
    clock.tick(60)
