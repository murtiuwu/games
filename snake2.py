import pygame
import time
import random


pygame.init()

BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)
WHITE = (255,255,255)

dis_width = 800
dis_height = 600

snake_block = 10
FPS = 10


dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('зьмейка')

clock = pygame.time.Clock()

font_stile = pygame.font.SysFont("bahnschrift", 30)
score_font = pygame.font.SysFont("comicsansms", 35)

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, GREEN, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_stile.render(msg, True, color)
    dis.blit(mesg, [dis_width / 2 - len(msg)*4, dis_height / 2])

def message_score(msg, color):
    mesg = score_font.render(msg, True, color)
    dis.blit(mesg, [dis_width / 18, dis_height / 18])

def game_loop():
    score = 0

    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    length_of_snake = 1

    food_x = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block
    food_y = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block

    while not game_over:

        while game_close:
            dis.fill(BLACK)
            message('you lose! press Q to quit, R to replay', RED)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    elif event.key == pygame.K_r:
                        game_loop()

        for event in pygame.event.get():
            #print(event)  выводит все что регистрирует окно
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    y1_change = 0
                    x1_change = -snake_block
                elif event.key == pygame.K_RIGHT:
                    y1_change = 0
                    x1_change = snake_block
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
                elif event.type == pygame.QUIT:
                    exit()

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change

        dis.fill(BLACK)

        message_score(f'score:{score}', WHITE)

        pygame.draw.rect(dis, RED, [food_x, food_y, snake_block, snake_block])

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)

        # pygame.draw.rect(dis, GREEN, [x1, y1, snake_block, snake_block])
        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block
            food_y = round(random.randrange(0, dis_height - snake_block) / snake_block) * snake_block
            length_of_snake += 1
            score += 1

        clock.tick(FPS)

game_loop()

pygame.quit()
quit()
