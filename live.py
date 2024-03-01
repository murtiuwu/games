import random
import copy
import pygame

'''
запускайте этот код в таком состоянии чтобы посмотреть как он будет работать.
я подписал комментариями все величины которые можно менять чтобы подстраивать поле под себя.

пробел - режим строительства
r - случайная генерация
d - очистка всего поля (не работает во время режима строительства)
s (во время режима строительства) - сохранение текущего поля в ячейку которую ты указываешь (1 символ)
l (во время режима строительства) - загружает поле из указанной ячейки

во время режима строительства 
ЛКМ - поставить клетку
ПКМ - удалить клетку
'''

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
EAZY_WHITE = (230, 230, 230)

BG_COLOR = BLACK

# block_size = 10 # это размер одной клетки (в пикселях)

pygame.init()

pool = []
for i in range(150): # размер поля по х (в клетках)
    pool.append(['.'] * 90) # размер поля по у (в клетках)

# этот код случайно генерирует первое поколение если вас не устраивает планер в начале
# for i1 in range(len(pool)):
#     for i2 in range(len(pool[i1])):
#         if random.randrange(0, 2) == 0:
#             pool[i1][i2] = '0'

def dead(Pool, X, Y):
    Life = 0

    list_of_creature = [Pool[Y % (len(Pool) - 1)][(X - 1) % (len(Pool[0]) - 1)]]
    list_of_creature.append(Pool[Y% (len(Pool) - 1)][(X + 1) % (len(Pool[0]) - 1)])
    list_of_creature.append(Pool[(Y + 1) % (len(Pool) - 1)][(X + 1) % (len(Pool[0]) - 1)])
    list_of_creature.append(Pool[(Y + 1) % (len(Pool) - 1)][X % (len(Pool[0]) - 1)])
    list_of_creature.append(Pool[(Y + 1) % (len(Pool) - 1)][(X - 1) % (len(Pool[0]) - 1)])
    list_of_creature.append(Pool[(Y - 1) % (len(Pool) - 1)][(X + 1) % (len(Pool[0]) - 1)])
    list_of_creature.append(Pool[(Y - 1) % (len(Pool) - 1)][X % (len(Pool[0]) - 1)])
    list_of_creature.append(Pool[(Y - 1) % (len(Pool) - 1)][(X - 1) % (len(Pool[0]) - 1)])


    for i in list_of_creature:
        if i != ".":
            Life += 1

    if Life == 3:
        return "0"
    else:
        return "."

def life(Pool, X, Y):
    Life = 0

    list_of_creature = [Pool[Y % (len(Pool) - 1)][(X - 1) % (len(Pool[0]) - 1)]]
    list_of_creature.append(Pool[Y% (len(Pool) - 1)][(X + 1) % (len(Pool[0]) - 1)])
    list_of_creature.append(Pool[(Y + 1) % (len(Pool) - 1)][(X + 1) % (len(Pool[0]) - 1)])
    list_of_creature.append(Pool[(Y + 1) % (len(Pool) - 1)][X % (len(Pool[0]) - 1)])
    list_of_creature.append(Pool[(Y + 1) % (len(Pool) - 1)][(X - 1) % (len(Pool[0]) - 1)])
    list_of_creature.append(Pool[(Y - 1) % (len(Pool) - 1)][(X + 1) % (len(Pool[0]) - 1)])
    list_of_creature.append(Pool[(Y - 1) % (len(Pool) - 1)][X % (len(Pool[0]) - 1)])
    list_of_creature.append(Pool[(Y - 1) % (len(Pool) - 1)][(X - 1) % (len(Pool[0]) - 1)])


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


def convert_To_Matrix(test_str, K):
    temp = [test_str[idx: idx + K] for idx in range(0, len(test_str), K)]
    res = [list(ele) for ele in temp]
    return res

def play(pool):
    block_size = 10  # это размер одной клетки (в пикселях)
    width = len(pool) * block_size
    height = len(pool[0]) * block_size

    # gun = pygame.image.load('/Users/timur/desktop/sprites/gun.jpg')

    clock = pygame.time.Clock()

    pygame_scene = pygame.display.set_mode((width, height))
    pygame.display.set_caption('live')

    pause = False
    save = False
    load = False
    setting = False

    in_del, out_del = "", ""

    text = pygame.font.Font(None, 30)

    give_me_save = text.render('введите номер файла сохранения', False, WHITE)

    while True:
        # r = random.randrange(0, 256)
        # g = random.randrange(0, 256)
        # b = random.randrange(0, 256)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    for i1 in range(len(pool)):
                        for i2 in range(len(pool[i1])):
                            if random.randrange(0, 2) == 0:
                                pool[i1][i2] = '0'
                if event.key == pygame.K_d:
                    for i1 in range(len(pool)):
                        for i2 in range(len(pool[i1])):
                            pool[i1][i2] = '.'
                    play(pool)
                if event.key == pygame.K_SPACE:
                    pause = True
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame_scene.fill(BG_COLOR)
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


        while pause:

            pygame_scene.fill(BG_COLOR)
            mouse_pos = pygame.mouse.get_pos()
            hes_a_live = pygame.mouse.get_pressed()
            pygame_scene.blit(gun, (100, 100))

            while setting:
                pass

            while load:
                pygame_scene.blit(give_me_save, (10, 10))
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if event.type == pygame.KEYDOWN:
                        with open(f'save_slot{event.unicode}', 'r') as save_slot:
                            poll_res = convert_To_Matrix(save_slot.read(), len(poll_res[0]))
                            load = False


            while save:
                pygame_scene.blit(give_me_save, (10,10))
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if event.type == pygame.KEYDOWN:
                        with open(f'save_slot{event.unicode}', 'w') as save_slot:
                            text = out_del.join([in_del.join([str(ele) for ele in sub]) for sub in poll_res])
                            save_slot.write(str(text))
                            save = False


            if hes_a_live[0]:
                x = int(mouse_pos[0] / block_size)
                y = int(mouse_pos[1] / block_size)
                poll_res[x][y] = '0'
            elif hes_a_live[2]:
                x = int(mouse_pos[0] / block_size)
                y = int(mouse_pos[1] / block_size)
                poll_res[x][y] = '.'

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_l:
                        load = True
                    if event.key == pygame.K_s:
                        save = True
                    if event.key == pygame.K_SPACE:
                        pause = False

            for row in range(len(poll_res)):
                for column in range(len(poll_res[row])):
                    if poll_res[row][column] == '0':
                        # r = random.randrange(0, 256)
                        # g = random.randrange(0, 256)
                        # b = random.randrange(0, 256)
                        # RAND_COLOR = (r, g, b) # эта переменная в комбинации с предыдущими тремя задает психоделическую
                        # радужную расцветку всем клеткам, если вы хотите более спокойный цвет то закоментируйте эти четыре строки
                        # и замените переменную под       ЭТИМ           словом на "GREEN"
                        pygame.draw.rect(pygame_scene, EAZY_WHITE,
                                         (row * block_size, column * block_size, block_size, block_size))
            pygame.display.update()


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
                    pygame.draw.rect(pygame_scene, EAZY_WHITE,
                                     (row*block_size, column*block_size, block_size, block_size))
        pygame.display.update()

        clock.tick(15)


play(pool)
pygame.quit()
quit()
