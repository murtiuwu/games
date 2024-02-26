import pygame
from random import randrange

RES = 800
SIZE = 50

x, y = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)

length = 1
snake = [(x, y)]

move_x, move_y = 0, 0
fps = 5

pygame.init()
sc = pygame.display.set_mode([RES, RES])
clock = pygame.time.Clock()


while True:
    sc.fill(pygame.Color('black'))
    [(pygame.draw.rect(sc, pygame.Color('green'), (i, j, SIZE, SIZE))) for i, j in snake]
    (pygame.draw.rect(sc, pygame.Color('red'), (*apple, SIZE, SIZE)))

    snake.append((x, y))

    x += move_x * SIZE
    y += move_y * SIZE
    snake.append((x, y))
    snake = snake[-length:]

    if snake[-1] == apple:
        apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
        length += 1

    pygame.display.flip()
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        move_x, move_y = 0, -1
    if key[pygame.K_s]:
        move_x, move_y = 0, 1
    if key[pygame.K_d]:
        move_x, move_y = 1, 0
    if key[pygame.K_a]:
        move_x, move_y = -1, 0

