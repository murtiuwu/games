import pygame

pygame.init()

pygame_scene = pygame.display.set_mode((400, 800))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()