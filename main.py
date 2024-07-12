import pygame

pygame.init()
screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()

game_surface = pygame.Surface((100, 200))
game_surface.fill('red')
game_background = pygame.image.load()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(game_surface, (200, 300))
    pygame.display.update()
    clock.tick(60)
