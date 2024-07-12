import pygame
from sys import exit
import random

pygame.init()
screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()
game_font = pygame.font.Font(None, 30)

game_surface = pygame.Surface((100, 200))
game_surface.fill('red')
game_background = pygame.image.load('images/sky.png')
game_background = pygame.transform.scale(game_background, (800, 400))
game_goblin = pygame.image.load('images/goblin4x.png')
game_orb = pygame.image.load('images/orb4x.png')
game_heart = pygame.image.load('images/heart4x.png')
game_title = game_font.render('Angry Goblin', False, 'Black')
game_heart_count = game_font.render('Hearts collected: ', False, 'Black')


bgX = 0
bgX2 = game_background.get_width()

gob_pos_x = 50
orb_pos_x = random.randint(800, 1000)
orb_pos_y = random.randint(0, 350)

hrt_pos_x = random.randint(700, 900)
hrt_pos_y = random.randint(0, 350)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    bgX -= 1.4
    bgX2 -= 1.4
    if bgX < game_background.get_width() * -1:
        bgX = game_background.get_width()

    if bgX2 < game_background.get_width() * -1:
        bgX2 = game_background.get_width()

    screen.blit(game_background, (bgX, 0))
    screen.blit(game_background, (bgX2, 0))

    #screen.blit(game_background, (0, 0))
    screen.blit(game_goblin, (gob_pos_x, 250))
    screen.blit(game_orb, (orb_pos_x, orb_pos_y))
    screen.blit(game_heart, (hrt_pos_x, hrt_pos_y))
    screen.blit(game_title, (350, 10))
    screen.blit(game_heart_count, (1, 10))

    # Create rectangles for collision detection
    goblin_rect = game_goblin.get_rect(topleft=(gob_pos_x, 250))
    orb_rect = game_orb.get_rect(topleft=(orb_pos_x, orb_pos_y))

    # Check for collision
    if goblin_rect.colliderect(orb_rect):
        print("Game Over!")
        pygame.quit()
        exit()


    orb_pos_x += -5
    if orb_pos_x < -50:
        orb_pos_x = random.randint(800, 1000)
        orb_pos_y = random.randint(0, 350)

    hrt_pos_x += -5
    if hrt_pos_x < -50:
        hrt_pos_x = random.randint(700, 900)
        hrt_pos_y = random.randint(0, 350)


    #gob_pos_x += 0.4
    #screen.blit(game_surface, (50, 100))

    pygame.display.update()
    clock.tick(60)
