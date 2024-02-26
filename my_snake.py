import pygame
import time
import random

pygame.init()

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BACKGROUND = (0,170,200)
BLACK = (0,0,0)
WHITE = (255,255,255)

text = pygame.font.Font(None, 30)

# def message(pos_x, pos_y, font_type):


def game_loop():
    clock = pygame.time.Clock()

    snake_body = []

    my_score = 0

    # snake_head = pygame.image.load('/Users/timur/desktop/sprites/snake_sprite_head.png')
    # snake_body = pygame.image.load('/Users/timur/desktop/sprites/snake_sprite_body.png')
    # apple = pygame.image.load('/Users/timur/desktop/sprites/apple.png')

    game_over = False
    game_loose = False

    width = 800
    height = 800

    snake_pos_x = width/2
    snake_pos_y = height/2

    move_x = 0
    move_y = 0

    block_size = 20
    pygame_scene = pygame.display.set_mode((width, height))
    pygame.display.set_caption('snuk')

    food_x = round(random.randrange(0, width - block_size) / block_size) * block_size
    food_y = round(random.randrange(0, height - block_size) / block_size) * block_size

    lose = text.render(f'you loose, press R to restart', False, WHITE)

    while not game_over:
        pygame_scene.fill(BACKGROUND)

        if snake_pos_x > width or snake_pos_x < 0 or snake_pos_y > height or snake_pos_y < 0:
            game_loose = True
        while game_loose:
            pygame_scene.fill(BLACK)
            pygame_scene.blit(lose, (width/2 - 120, height/2))
            pygame.display.update()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_r] == 1:
                game_loop()

            for event in pygame.event.get():
                # if event.type == pygame.KEYDOWN:
                #     if event.key == pygame.K_w:
                #         move_x = 0
                #         move_y = -block_size
                #     elif event.key == pygame.K_s:
                #         move_x = 0
                #         move_y = block_size
                #     elif event.key == pygame.K_d:
                #         move_x = block_size
                #         move_y = 0
                #     elif event.key == pygame.K_a:
                #         move_x = -block_size
                #         move_y = 0

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

        score = text.render(f'score:{my_score}', False, WHITE)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] == 1:
            move_x = 0
            move_y = -block_size
        elif keys[pygame.K_s] == 1:
            move_x = 0
            move_y = block_size
        elif keys[pygame.K_d] == 1:
            move_x = block_size
            move_y = 0
        elif keys[pygame.K_a] == 1:
            move_x = -block_size
            move_y = 0

        snake_body.append((snake_pos_x + 1 - 1, snake_pos_y + 1 - 1))

        for i in snake_body:
            pygame.draw.rect(pygame_scene, GREEN, (i[0], i[1], block_size, block_size))

        snake_body.pop(0)

        snake_pos_x += move_x
        snake_pos_y += move_y

        # food_x = round(random.randrange(0, width - block_size) / block_size) * block_size
        # food_y = round(random.randrange(0, height - block_size) / block_size) * block_size

        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        for i in snake_body[:-1]:
            if i[0] == snake_pos_x and i[1] == snake_pos_y:
                game_loose = True

        pygame.draw.rect(pygame_scene, GREEN, (snake_pos_x, snake_pos_y, block_size, block_size))
        pygame.draw.rect(pygame_scene, RED, (food_x, food_y, block_size, block_size))

        if snake_pos_x == food_x and food_y == snake_pos_y:
            snake_body.append((snake_pos_x+1-1, snake_pos_y+1-1))
            my_score += 1
            food_x = round(random.randrange(0, width - block_size) / block_size) * block_size
            food_y = round(random.randrange(0, height - block_size) / block_size) * block_size



        # pygame_scene.blit(snake_head, (snake_pos_x, snake_pos_y))
        # pygame_scene.blit(apple, (food_x, food_y))
        pygame_scene.blit(score, (0,0))

        pygame.display.update()

        clock.tick(30) # FPS программы
game_loop()

pygame.quit()
quit()

