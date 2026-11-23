from pico2d import *
import game_world
import game_framework
from boy import Boy
from grass import Grass
from ball import Ball
from zombie import Zombie
import random

boy = None


def handle_events():


    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            game_framework.quit()
            return
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            boy.handle_event(event)


def init():
    global boy

    boy = Boy()
    game_world.add_oject(boy)

    grass = Grass()
    game_world.add_oject(grass, 0)
    game_world.add_collision_pair('ball:grass', None, grass)

    pickup_positions = random.sample(range(100, 1501, 50), 9)
    for x in pickup_positions:
        ball = Ball(x, 70, 0)
        game_world.add_oject(ball)
        game_world.add_collision_pair('boy:ball', boy, ball)

    zombies = [Zombie() for _ in range(4)]
    game_world.add_objects(zombies, 1)
    for zombie in zombies:
        game_world.add_collision_pair('ball:zombie', None, zombie)

def pause():
    boy.pause()


def resume():
    pass


def finish():
    global boy
    game_world.clear()
    boy = None


def update():
    game_world.update()

def render():
    clear_canvas()
    game_world.render()
    update_canvas()








