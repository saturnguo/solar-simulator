from draw_library import *
from system import System
from body import Body
import random

MOUSE_PRESS = False
MOUSE_PRESS_TWO = False

NEW_PLANET_X = 0
NEW_PLANET_Y = 0
NEW_PLANET_COUNT = 0

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

TIME_SCALE = 3.0e6
PIXELS_PER_METER = 7 / 1e10 

FRAMERATE = 30
TIMESTEP = 1.0 / FRAMERATE


def mouse_press(mouse_x, mouse_y):
    global MOUSE_PRESS, MOUSE_PRESS_TWO, NEW_PLANET_X, NEW_PLANET_Y
    MOUSE_PRESS = True
    MOUSE_PRESS_TWO = True

    NEW_PLANET_X = mouse_x
    NEW_PLANET_Y = mouse_y


def mouse_release():
    global MOUSE_PRESS
    MOUSE_PRESS = False


def create_new_planet():
    global NEW_PLANET_X, NEW_PLANET_Y, NEW_PLANET_COUNT, MOUSE_PRESS_TWO

    new_planet = NEW_PLANET_COUNT
    x = (NEW_PLANET_X - WINDOW_WIDTH / 2) / PIXELS_PER_METER
    y = (NEW_PLANET_Y - WINDOW_HEIGHT / 2) / PIXELS_PER_METER
    v_x = 0
    r = int(random.uniform(0, 255))
    g = int(random.uniform(0, 255))
    b = int(random.uniform(0, 255))

    pixel_radius = random.uniform(1, 8)
    if 1 < pixel_radius <= 2:
        mass = random.uniform(0.33e24, 1.5e24)
        v_y = random.uniform(0, 12500)
    elif 2 < pixel_radius <= 4:
        mass = random.uniform(1.5e24, 3.0e24)
        v_y = random.uniform(12500, 25000)
    elif 4 < pixel_radius <= 6:
        mass = random.uniform(3.0e24, 4.5e24)
        v_y = random.uniform(25000, 37500)
    elif 6 < pixel_radius <= 8:
        mass = random.uniform(4.5e24, 5.97e24)
        v_y = random.uniform(37500, 49890)

    new_planet = Body(mass, x, y, v_x, v_y, pixel_radius, r, g, b)
    NEW_PLANET_COUNT = NEW_PLANET_COUNT + 1
    solar.body_list.append(new_planet)


def main():
    global MOUSE_PRESS_TWO

    set_background()

    solar.draw(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, PIXELS_PER_METER)
    solar.update(TIMESTEP * TIME_SCALE)

    if MOUSE_PRESS:
        solar.large()
    if MOUSE_PRESS_TWO:
        create_new_planet()
        MOUSE_PRESS_TWO = False


sun = Body(1.98892e30, 0, 0, 0, 0, 24, 255, 255, 0)
mercury = Body(0.33e24, -57.9e9, 0, 0, 47890, 4, 0.349 * 255, 0.129 * 255, 0.086 * 255)
venus = Body(4.87e24, -108.2e9, 0, 0, 35040, 8, 0, 255, 0)
earth = Body(5.97e24, -149.6e9, 0, 0, 29790, 6, 0, 0, 255)
mars = Body(0.642e24,-227.9e9, 0, 0, 24140, 4, 255, 0, 0)

planet_list = [sun, mercury, venus, earth, mars]
solar = System(planet_list)

start_graphics(main, framerate=FRAMERATE, width=WINDOW_WIDTH, height=WINDOW_HEIGHT,
               mouse_press=mouse_press, mouse_release=mouse_release)
