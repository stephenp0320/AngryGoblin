import pygame
from sys import exit
pygame.init()
screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()

game_surface = pygame.Surface((100, 200))
game_surface.fill('red')
game_background = pygame.image.load('images/sky.png')
game_background = pygame.transform.scale(game_background, (800, 400))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(game_background, (0, 0))
    screen.blit(game_surface, (50, 100))

    pygame.display.update()
    clock.tick(60)
