import random
import copy
import pygame

'''
запускайте этот код в таком состоянии чтобы посмотреть как он будет работать.
я подписал комментариями все величины которые можно менять чтобы подстраивать поле 
под себя. для генерации случайного поля по новой достаточно нажать любую кнопку на клавиатуре
(например пробел) не закрывая окно с текущей генерацией
'''

pygame.init()

pool = []
for i in range(90): # размер поля по х (в клетках)
    pool.append(['.'] * 90) # размер поля по у (в клетках)

# этот код случайно генерирует первое поколение если вас не устраивает планер в начале
# for i1 in range(len(pool)):
#     for i2 in range(len(pool[i1])):
#         if random.randrange(0, 2) == 0:
#             pool[i1][i2] = '0'

def dead(Pool, X, Y):
    Life = 0

    list_of_creature = [Pool[Y % (len(Pool) - 1)][(X - 1) % (len(Pool) - 1)]]
    list_of_creature.append(Pool[Y% (len(Pool) - 1)][(X + 1) % (len(Pool) - 1)])
    list_of_creature.append(Pool[(Y + 1) % (len(Pool) - 1)][(X + 1) % (len(Pool) - 1)])
    list_of_creature.append(Pool[(Y + 1) % (len(Pool) - 1)][X % (len(Pool) - 1)])
    list_of_creature.append(Pool[(Y + 1) % (len(Pool) - 1)][(X - 1) % (len(Pool) - 1)])
    list_of_creature.append(Pool[(Y - 1) % (len(Pool) - 1)][(X + 1) % (len(Pool) - 1)])
    list_of_creature.append(Pool[(Y - 1) % (len(Pool) - 1)][X % (len(Pool) - 1)])
    list_of_creature.append(Pool[(Y - 1) % (len(Pool) - 1)][(X - 1) % (len(Pool) - 1)])


    for i in list_of_creature:
        if i != ".":
            Life += 1

    if Life == 3:
        return "0"
    else:
        return "."

def life(Pool, X, Y):
    Life = 0

    list_of_creature = [Pool[Y % (len(Pool) - 1)][(X - 1) % (len(Pool) - 1)]]
    list_of_creature.append(Pool[Y% (len(Pool) - 1)][(X + 1) % (len(Pool) - 1)])
    list_of_creature.append(Pool[(Y + 1) % (len(Pool) - 1)][(X + 1) % (len(Pool) - 1)])
    list_of_creature.append(Pool[(Y + 1) % (len(Pool) - 1)][X % (len(Pool) - 1)])
    list_of_creature.append(Pool[(Y + 1) % (len(Pool) - 1)][(X - 1) % (len(Pool) - 1)])
    list_of_creature.append(Pool[(Y - 1) % (len(Pool) - 1)][(X + 1) % (len(Pool) - 1)])
    list_of_creature.append(Pool[(Y - 1) % (len(Pool) - 1)][X % (len(Pool) - 1)])
    list_of_creature.append(Pool[(Y - 1) % (len(Pool) - 1)][(X - 1) % (len(Pool) - 1)])


    for i in list_of_creature:
        if i == "0":
            Life += 1

    if Life == 3 or Life == 2:
        return "0"
    else:
        return "."
# координаты планера
pool[3][4] = '0'
pool[3][5] = '0'
pool[2][5] = '0'
pool[2][6] = '0'
pool[1][4] = '0'

def play(pool):
    block_size = 10 # это размер одной клетки (в пикселях)
    width = len(pool) * block_size
    height = len(pool[0]) * block_size

    clock = pygame.time.Clock()

    pygame_scene = pygame.display.set_mode((width, height))
    pygame.display.set_caption('live')

    GREEN = (0,255,0)
    BLACK = (0, 0, 0)
    WHITE = (255,255,255)
    EAZY_WHITE = (230,230,230)

    while True:
        r = random.randrange(0, 256)
        g = random.randrange(0, 256)
        b = random.randrange(0, 256)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                for i1 in range(len(pool)):
                    for i2 in range(len(pool[i1])):
                        if random.randrange(0, 2) == 0:
                            pool[i1][i2] = '0'
                play(pool)

        pygame_scene.fill(BLACK)
        poll_res = []
        for i in pool:
            poll_res.append(copy.copy(i))
        cor_y = -1
        for y in pool:
            cor_y += 1
            cor_x = -1
            for x in y:
                cor_x += 1
                if x == ".":
                    poll_res[cor_y][cor_x] = dead(pool, cor_x, cor_y)
                else:
                    poll_res[cor_y][cor_x] = life(pool, cor_x, cor_y)
        pool = []
        for i in poll_res:
            pool.append(copy.copy(i))
        for row in range(len(poll_res)):
            for column in range(len(poll_res[row])):
                if poll_res[row][column] == '0':
                    # r = random.randrange(0, 256)
                    # g = random.randrange(0, 256)
                    # b = random.randrange(0, 256)
                    # RAND_COLOR = (r, g, b) # эта переменная в комбинации с предыдущими тремя задает психоделическую
                    # радужную расцветку всем клеткам, если вы хотите более спокойный цвет то закоментируйте эти четыре строки
                    # и замените переменную под       ЭТИМ           словом на "GREEN"
                    pygame.draw.rect(pygame_scene, EAZY_WHITE, (row*block_size, column*block_size, block_size, block_size))
        pygame.display.update()


        clock.tick(15)


play(pool)
pygame.quit()
quit()