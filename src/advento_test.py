# importando o FGame
from FGAme import *
# pygame
import pygame
from pygame.locals import *

# Contadores e marcadores globais
special_count = 0
jump_count = 0

# Mundo
world = World()

# Personagem
char1 = AABB(shape=(15, 25), pos=(400, 35), color='blue', mass='150')
char1.inertia /= 2
char1.restitution = 0

# Inimigo
enemy_body = RegularPoly(
    6, length=35, pos=(400, 470), color='red', mass='inf', vel=(0,0), restitution=0)
enemy_body.inertia = 'inf'
enemy_wings = AABB(shape=(150, 20), pos=(400, 492), color='red', mass='inf', vel=(0,0), restitution=0)
enemy_wings.inertia = 'inf'
enemy_tail = AABB(shape=(20, 150), pos=(400, 515), color='red', mass='inf', vel=(0,0), restitution=0)
enemy_tail.inertia = 'inf'

# Terreno
terrain = AABB(shape=(800, 20), pos=(400, 10), mass='inf', color='green')

# Plataformas
platform1 = AABB(shape=(115, 2), pos=(300, 75), mass='inf')
platform2 = AABB(shape=(50, 2), pos=(200, 50), mass='inf')
platform3 = AABB(shape=(50, 2), pos=(400, 50), mass='inf')
platform4 = AABB(shape=(115, 2), pos=(650, 75), mass='inf')
platform5 = AABB(shape=(50, 2), pos=(550, 50), mass='inf')
platform6 = AABB(shape=(50, 2), pos=(750, 50), mass='inf')

# # Forca de atracao (gravidade)
# char1.gravity = 2400

# Adiciona elementos ao mundo
world.add(char1)
world.add(enemy_body)
world.add(enemy_wings)
world.add(enemy_tail)
world.add(platform1)
world.add(platform2)
world.add(platform3)
world.add(platform4)
world.add(platform5)
world.add(platform6)
world.add(terrain)
world.add.margin(0)


# Comando de movimentacao para a direita
@listen('long-press', 'right')
def move_right():
    char1.vel = (char1.vel.x+10, char1.vel.y)

# Comando de movimentacao para a esquerda
@listen('long-press', 'left')
def move_left():
    char1.vel = (char1.vel.x-10, char1.vel.y)

# Comando de movimentacao para frente
@listen('long-press', 'up')
def move_left():
    char1.vel = (char1.vel.x, char1.vel.y+10)

# Comando de movimentacao para trás
@listen('long-press', 'down')
def move_left():
    char1.vel = (char1.vel.x, char1.vel.y-10)


# # Comando de pulo
# @listen('key-down', 'up')
# def jump():
#     if jump_count < 2:
#         char1.vel = (char1.vel.x, 400)
#         global jump_count
#         jump_count += 1


# Comando de tiro para cima
@listen('long-press', 'w')
def shot_left():
    shot = world.add.aabb(
        shape=(2, 3),
        pos=(char1.pos.x, char1.pos.y+20),
        vel=(0, 1000),
        mass='inf')


# # Comando de tiro para a esquerda
# @listen('key-down', 'a')
# def shot_left():
#     shot = world.add.aabb(
#         shape=(3, 2),
#         pos=(char1.pos.x-10, char1.pos.y),
#         vel=(-600, 0),
#         mass='inf')


# # Comando de tiro para a direita
# @listen('key-down', 'd')
# def shot_right():
#     shot = world.add.aabb(
#         shape=(3, 2),
#         pos=(char1.pos.x+10, char1.pos.y),
#         vel=(600, 0),
#         mass='inf')


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
        if enemy_body.pos.x < char1.pos.x:
            shot = Circle(50,
                        pos=(char1.pos.x - 35, char1.pos.y),
                        mass='inf')
            shot.vel = ((enemy_body.pos.x - char1.pos.x),
                        (enemy_body.pos.y - char1.pos.y)) # Ainda meio quebrado

        elif enemy_body.pos.x > char1.pos.x:
            shot = Circle(50,
                        pos=(char1.pos.x + 35,
                        char1.pos.y),
                        mass='inf')
            shot.vel = ((enemy_body.pos.x - char1.pos.x),
                        (enemy_body.pos.y - char1.pos.y)) # Ainda meio quebrado

        else:
            shot = Circle(50,
                        pos=(char1.pos.x, char1.pos.y+35),
                        mass='inf')
            shot.vel = ((enemy_body.pos.x - char1.pos.x),
                        (enemy_body.pos.y - char1.pos.y)) # Ainda meio quebrado
        world.add(shot)

    else:
        return

    global special_count
    special_count += 1


# # Reset de pulos
# @listen('frame-enter')
# def update():
#     if char1.pos.y < 35:
#         global jump_count
#         jump_count = 0


# # Altura do inimigo
# @listen('frame-enter')
# def enemy_heigh():
#     if abs(enemy_body.y - char1.y) < 20:
#         pass
#     elif enemy_body.y > char1.y:
#         enemy_body.move(0, -10)
#     else:
#         enemy_body.move(0, 10)

#     if enemy_body.y >= 450:
#         enemy_body.vel += (0,-enemy_body.vel.y-150)


# Movimentacao do inimigo
@listen('frame-enter')
def enemy_movement():
    if abs(enemy_body.x - char1.x) < 30:
        pass
    elif enemy_body.x > char1.x:
        enemy_body.move(-10, 0)
        enemy_wings.move(-10, 0)
        enemy_tail.move(-10, 0)
    else:
        enemy_body.move(10, 0)
        enemy_wings.move(10, 0)
        enemy_tail.move(10, 0)


# Condicao de fim de jogo
@listen('frame-enter')
def check_player_lose():
    if char1.x < -10 or char1.x > 810 or char1.y < -10 or char1.y > 610:
        world.pause()


# @listen('pre-collision')
# def on_collision(col):
#     print('bateu')

world.run()
