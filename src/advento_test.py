# Importacao de pacotes
from FGAme import *
import pygame
from pygame.locals import *

# Contadores e marcadores globais
special_count = 0
turbo_count = 0

# Mundo
world = World()
world.damping=2
# pygame.mixer.pre_init(44100, 16, 2, 4096)
# pygame.init()
# main_sound = pygame.mixer.music.load("main_theme.mp3")
# main_sound = pygame.mixer.music.play()
# pygame.mixer.music.set_volume(0.2);

# Personagem
char1 = AABB(shape=(15, 25), pos=(400, 35), color='blue', mass='150')
char1.inertia /= 2
char1.restitution = 0

# Inimigo
enemy1 = RegularPoly(
    6, length=35, pos=(400, 530), color='red', mass='inf', vel=(300,0), restitution=0)
enemy1.inertia = 'inf'

# Terreno
terrain = AABB(shape=(800, 20), pos=(400, 10), mass='inf', color='green')

# Plataformas
platform1 = world.add.aabb(shape=(115, 10), pos=(67, 452), mass='inf')
platform2 = world.add.aabb(shape=(87, 10), pos=(235, 150), mass='inf')
platform3 = world.add.aabb(shape=(122, 10), pos=(400, 350), mass='inf')
platform4 = world.add.aabb(shape=(115, 10), pos=(650, 75), mass='inf')
platform5 = world.add.aabb(shape=(53, 10), pos=(625, 250), mass='inf')
platform6 = world.add.aabb(shape=(67, 10), pos=(750, 440), mass='inf')

# Comando de movimentacao para a direita
@listen('long-press', 'right')
def move_right():
    char1.vel = (char1.vel.x+25, char1.vel.y)

# Comando de movimentacao para a esquerda
@listen('long-press', 'left')
def move_left():
    char1.vel = (char1.vel.x-25, char1.vel.y)

# Comando de movimentacao para frente
@listen('long-press', 'up')
def move_left():
    char1.vel = (char1.vel.x, char1.vel.y+25)

# Comando de movimentacao para trás
@listen('long-press', 'down')
def move_left():
    char1.vel = (char1.vel.x, char1.vel.y-25)


# Comando de turbo
@listen('key-down', 'w')
def turbo():
    if turbo_count < 10:
        char1.vel = char1.vel*3
        global turbo_count
        turbo_count += 1


# Comando de tiro do jogador
@listen('key-down', 'q')
def player_shot():
    shot = world.add.aabb(
        shape=(2, 3),
        pos=(char1.pos.x, char1.pos.y+20),
        vel=(0, 1000),
        mass='inf')



# Comando de especial
@listen('key-down', 'space')
def special_move():
    if special_count < 2:
        blast_count = 0
        char1.inertia = 'inf'
        while blast_count < 10:
            shot = Circle(5, pos=(char1.pos.x, char1.pos.y+25), mass='inf')
            shot.vel = vel.random()
            world.add(shot)
            blast_count += 1
        char1.inertia /= 2

    elif special_count == 2:
        if enemy1.pos.x < char1.pos.x:
            shot = Circle(50,
                        pos=(char1.pos.x - 35, char1.pos.y),
                        mass='inf')
            shot.vel = ((enemy1.pos.x - char1.pos.x),
                        (enemy1.pos.y - char1.pos.y)) # Ainda meio quebrado

        elif enemy1.pos.x > char1.pos.x:
            shot = Circle(50,
                        pos=(char1.pos.x + 35,
                        char1.pos.y),
                        mass='inf')
            shot.vel = ((enemy1.pos.x - char1.pos.x),
                        (enemy1.pos.y - char1.pos.y)) # Ainda meio quebrado

        else:
            shot = Circle(50,
                        pos=(char1.pos.x, char1.pos.y+35),
                        mass='inf')
            shot.vel = ((enemy1.pos.x - char1.pos.x),
                        (enemy1.pos.y - char1.pos.y)) # Ainda meio quebrado
        world.add(shot)

    else:
        return

    global special_count
    special_count += 1


# Movimentacao do inimigo
@listen('frame-enter')
def enemy_movement():
    if enemy1.x >= 750:
        enemy1.vel = (enemy1.vel.x*(-1), enemy1.vel.y)
    elif enemy1.x <= 50:
        enemy1.vel = (enemy1.vel.x*(-1), enemy1.vel.y)

# Tiro do inimigo
def enemy_shot():
    shot = Circle(3,
        pos=(enemy1.pos.x, enemy1.pos.y-20),
        vel=(0, -1000),
        mass='inf')
    world.add(shot)
    schedule(1,enemy_shot)


# Condicao de fim de jogo
@listen('frame-enter')
def check_player_lose():
    if char1.x < -10 or char1.x > 810 or char1.y < -10 or char1.y > 610:
        world.pause()

# Adiciona elementos ao mundo
world.add(char1)
world.add(enemy1)
world.add(terrain)
world.add.margin(10,0,10,0)

run()
