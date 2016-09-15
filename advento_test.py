from FGAme import *

# Contador de pulos
jump_count = 0

# Mundo
world = World()

# Personagem
char1 = AABB(shape=(15, 25), pos=(35, 35), color='random', mass=80)
char1.inertia /= 2
char1.restitution = 0

# Terreno
terrain = AABB(shape=(800, 20), pos=(400, 10), mass='inf')

# Plataformas
heigh_bar1 = AABB(shape=(115, 2), pos=(300, 75), mass='inf')
heigh_bar2 = AABB(shape=(50, 2), pos=(200, 50), mass='inf')

# Forca de atracao (gravidade)
char1.gravity = 2400

# Adicionando elementos ao mundo
world.add(char1)
world.add(heigh_bar1)
world.add(heigh_bar2)
world.add(terrain)
world.add.margin(0)


# Mecanica de movimentacao pra direita
@listen('long-press', 'right')
def move_right():
    char1.move(6, 0)
    # O personagem pode perder o controle no jogo por causa de impactos,
    # esse sera o metodo do player retoma-lo.
    if char1.vel.x != 0:
        char1.vel = (0, char1.vel.y)


# Mecanica de movimentacao pra esquerda
@listen('long-press', 'left')
def move_left():
    char1.move(-6, 0)
    # O personagem pode perder o controle no jogo por causa de impactos,
    # esse sera o metodo do player retoma-lo.
    if char1.vel.x != 0:
        char1.vel = (0, char1.vel.y)


# Mecanica do pulo
@listen('key-down', 'up')
def jump():
    # Mecanica de pulo duplo pro jogo
    if jump_count < 2:
        char1.vel = (char1.vel.x, 400)
        global jump_count
        jump_count += 1


# Reset de pulos
@listen('frame-enter')
def update():
    if char1.pos.y < 35:
        global jump_count
        jump_count = 0


# @listen('pre-collision')
# def on_collision(col):
#     print('bateu')

world.run()
