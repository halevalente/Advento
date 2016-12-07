from FGAme import *
from advento.sfx import SFX
from pygame.locals import *
import os
_ROOT = os.path.abspath(os.path.dirname(__file__))


class Enemy(AABB):
    def __init__(self, armor_health, *args, **kwargs):
        self.armor_health = armor_health
        create_enemy_shots_event(self)
        super(Character, self).__init__(inertia = 'inf', restitution=0, *args, **kwargs)
        # on('pre-collision').do(sound_hit)

    def enemy_movement(self, vel):
        if self.x >= 750:
            self.vel = (vel.x*(-1), vel.y)
        elif self.x <= 50:
            self.vel = (vel.x*(-1), vel.y)
        else:
            pass

    def create_enemy_shots_event(self):
        ENEMYSHOT = USEREVENT + 1
        pygame.time.set_timer(ENEMYSHOT, 500)

    def enemy_shot_listener(self, world):
        if pygame.event.get(ENEMYSHOT):
            enemy_shot(self, world)

    def enemy_shot(self, world):
        shot = Circle(3,
            pos=(self.pos.x, self.pos.y-40),
            vel=(0, -500),
            mass='inf',
            color='red')
        world.add(shot)


    # def sound_hit(self, col, dx):
    #     sound_hit = os.path.join(_ROOT, 'sfx/hit.wav')
    #     SFX.play_sound(sound_hit)

    def check_defeat(self):
        if self.x < 0 or self.x > 800 or self.y < 0 or self.y > 600:
            print("VITORIA! O inimigo foi destruido.")
            exit()
        elif self.health <= 0:
            print("VITORIA! O inimigo foi destruido.")
            exit()

    @listen('post-collision')
    def detect_hit(arena, col):
        A, B = col
        if isinstance(A, Enemy) and isinstance(B, AABB):
            A.deal_damage()
        elif isinstance(A, AABB) and isinstance(B, ENEMY):
            B.deal_damage()
        elif isinstance(A, Enemy) and isinstance(B, RegularPoly):
            multi_damage = 0
            while(multi_damage < 3):
                A.deal_damage()
        elif isinstance(A, RegularPoly) and isinstance(B, Enemy):
            multi_damage = 0
            while(multi_damage < 3):
                B.deal_damage()
