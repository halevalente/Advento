from FGAme import *

# Mundo
world = World()

# Personagem
char1 = Circle(20, pos=(35, 35), color='random', mass=80)
char1.inertia /= 2

# Terreno
terrain = AABB(shape=(800, 20), pos=(400, 10), mass='inf')

# Barra de teste
heigh_bar = AABB(shape=(50, 2), pos=(400, 150), mass='inf')

# Forca de atracao (gravidade)
char1.gravity = 1000

# Adicionando elementos
world.add(char1)
world.add(heigh_bar)
world.add(terrain)
world.add.margin(0, 0, 0, 0)


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
@listen('key-down', 'space')
def jump():
    # Já deixando preparado pra uma mecanica de pulo duplo pro jogo
    # if jump_count < 2:\
    char1.vel = (char1.vel.x, 275)


world.run()

# Junk Code
#
# k = char1.mass
# char1.force = lambda t: (0, -10000)
# char1.force = lambda t: -k * vec_gravity.pos
# damping = 0.1
#
# if char1.pos.y > 100:
#       char1.vel = (char1.vel.x, -75)
