from FGAme import *

# Contadores globais
special_count = 0
jump_count = 0

# Mundo
world = World()

# Personagem
char1 = AABB(shape=(15, 25), pos=(35, 35), color='random', mass='150')
char1.inertia /= 2
char1.restitution = 0

# Inimigo
enemy1 = RegularPoly(
    3, length=75, pos=(750, 35), color='random', mass='inf')
enemy1.inertia /= 2
enemy1.restitution = 0
enemy1.omega += 15

# Terreno
terrain = AABB(shape=(800, 20), pos=(400, 10), mass='inf')

# Plataformas
platform1 = AABB(shape=(115, 2), pos=(300, 75), mass='inf')
platform2 = AABB(shape=(50, 2), pos=(200, 50), mass='inf')

# Forca de atracao (gravidade)
char1.gravity = 2400

# Adiciona elementos ao mundo
world.add(char1)
world.add(enemy1)
world.add(platform1)
world.add(platform2)
world.add(terrain)
world.add.margin(0)


# Comando de movimentacao pra direita
@listen('long-press', 'right')
def move_right():
    char1.move(6, 0)
    # O personagem pode perder o controle no jogo por causa de impactos,
    # esse sera o metodo do player retoma-lo.
    if char1.vel.x != 0:
        char1.vel = (0, char1.vel.y)


# Comando de movimentacao pra esquerda
@listen('long-press', 'left')
def move_left():
    char1.move(-6, 0)
    # O personagem pode perder o controle no jogo por causa de impactos,
    # esse sera o metodo do player retoma-lo.
    if char1.vel.x != 0:
        char1.vel = (0, char1.vel.y)


# Comando de pulo
@listen('key-down', 'up')
def jump():
    if jump_count < 2:
        char1.vel = (char1.vel.x, 400)
        global jump_count
        jump_count += 1


# Comando de tiro para a esquerda
@listen('key-down', 'a')
def shot_left():
    shot = world.add.aabb(
        shape=(3, 2), pos=(char1.pos.x, char1.pos.y), vel=(-400, 0), mass='inf')


# Comando de tiro para a direita
@listen('key-down', 'd')
def shot_right():
    shot = world.add.aabb(
        shape=(3, 2), pos=(char1.pos.x, char1.pos.y), vel=(400, 0), mass='inf')


# Comando de especial
@listen('key-down', 'space')
def special_move():
    if special_count < 2:
        blast_count = 0
        while blast_count < 10:
            shot = Circle(5, pos=(char1.pos.x, char1.pos.y), mass='inf')
            shot.vel = vel.random()
            world.add(shot)
            blast_count += 1

    elif special_count == 2:
        if enemy1.pos.x < char1.pos.x:
            shot = Circle(50, pos=(char1.pos.x - 35, char1.pos.y), mass='inf')
            shot.vel = ((enemy1.pos.x - char1.pos.x), (enemy1.pos.y - char1.pos.y))  # |
        elif enemy1.pos.x > char1.pos.x:
            shot = Circle(50, pos=(char1.pos.x + 35, char1.pos.y), mass='inf')
            shot.vel = ((enemy1.pos.x - char1.pos.x), (enemy1.pos.y - char1.pos.y))  # |
        else:
            shot = Circle(50, pos=(char1.pos.x, char1.pos.y+35), mass='inf')
            shot.vel = ((enemy1.pos.x - char1.pos.x), (enemy1.pos.y - char1.pos.y))  # |______ Ainda estão quebrados
        world.add(shot)

    else:
        return

    global special_count
    special_count += 1


# Reset de pulos
@listen('frame-enter')
def update():
    if char1.pos.y < 35:
        global jump_count
        jump_count = 0


# Altura do inimigo
@listen('frame-enter')
def enemy_heigh():
    if abs(enemy1.y - char1.y) < 20:
        pass
    elif enemy1.y > char1.y:
        enemy1.move(0, -10)
    else:
        enemy1.move(0, 10)


# Movimentacao do inimigo
@listen('frame-enter')
def enemy_movement():
    if abs(enemy1.x - char1.x) < 10:
        pass
    elif enemy1.x > char1.x:
        enemy1.move(-1, 10)
    else:
        enemy1.move(1, 10)


# @listen('pre-collision')
# def on_collision(col):
#     print('bateu')

world.run()
