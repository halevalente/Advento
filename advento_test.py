from FGAme import *

world = World()

char1 = Circle(20, pos=(35, 35), color='random', mass=10)

terrain = AABB(shape=(800, 20), pos=(400, 10), mass='inf')

vec_gravity = AABB(shape=(800, 20), pos=(0, 500), mass='inf')

# char1.force = lambda t: (0, -10000)
# k = char1.mass
# char1.force = lambda t: -k * vec_gravity.pos
# damping = 0.1

world.add(char1)
world.add(terrain)

world.add.margin(0, 0, 3, 0)


@listen('long-press', 'right')
def move_right():
    char1.move(6, 0)


@listen('long-press', 'left')
def move_left():
    char1.move(-6, 0)


@listen('key-down', 'space')
def jump():
    char1.vel = (char1.vel.x, 75)
    if char1.pos.y > 50:
        char1.vel = (char1.vel.x, -75)


world.run()
