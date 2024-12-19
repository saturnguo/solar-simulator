from draw_library import *
from system import System
from body import Body
from starscape import Starscape, WINDOW_WIDTH, WINDOW_HEIGHT
import random

MOUSE_PRESS = False

NEW_PLANET_X = 0
NEW_PLANET_Y = 0
NEW_PLANET_COUNT = 0
new_planet_name = "x"

TIME_SCALE = 3.0e6
PIXELS_PER_METER = 7 / 1e10 

FRAMERATE = 30
TIMESTEP = 1.0 / FRAMERATE


def mouse_press(mouse_x, mouse_y):
    global MOUSE_PRESS, MOUSE_PRESS_TWO, NEW_PLANET_X, NEW_PLANET_Y
    MOUSE_PRESS = True

    NEW_PLANET_X = mouse_x
    NEW_PLANET_Y = mouse_y

def mouse_release():
    return

def create_new_planet():
    global NEW_PLANET_X, NEW_PLANET_Y, NEW_PLANET_COUNT, MOUSE_PRESS, new_planet_name

    new_planet = NEW_PLANET_COUNT
    new_planet_name = new_planet_name + "x"
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

    new_planet = Body(new_planet_name, mass, x, y, v_x, v_y, pixel_radius, r, g, b)
    NEW_PLANET_COUNT = NEW_PLANET_COUNT + 1
    solar.body_list.append(new_planet)

def main():
    global MOUSE_PRESS

    solar.draw(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, PIXELS_PER_METER)
    solar.update(TIMESTEP * TIME_SCALE)

    starscape.maintain_list()

    if MOUSE_PRESS:
        create_new_planet()
        MOUSE_PRESS = False

sun = Body("sun", 1.98892e30, 0, 0, 0, 0, 24, 255, 255, 0)
mercury = Body("mercury", 0.33e24, -57.9e9, 0, 0, 47890, 4, 89, 35, 25)
venus = Body("venus", 4.87e24, -108.2e9, 0, 0, 35040, 5.5, 0, 255, 0)
earth = Body("earth", 5.97e24, -149.6e9, 0, 0, 29790, 6, 0, 0, 255)
mars = Body("mars", 0.642e24, -227.9e9, 0, 0, 24140, 4, 255, 0, 0)
jupiter = Body("jupiter", 1898e24, -778.5e9, 0, 0, 13140, 9, 255, 255, 0)
saturn = Body("saturn", 568e24, -1432.0e9, 0, 0, 9710, 7, 255, 100, 100)
uranus = Body("uranus", 86.8e24, -2867.0e9, 0, 0, 6840, 7, 183, 201, 226)
neptune = Body("neptune", 102e24, -4515.0e9, 0, 0, 5410, 6, 0, 0, 230)

planet_list = [sun, mercury, venus, earth, mars, 
               jupiter, saturn, uranus, neptune]
solar = System(planet_list)
starscape = Starscape()

start_graphics(main, framerate=FRAMERATE, width=WINDOW_WIDTH, height=WINDOW_HEIGHT,
               mouse_press=mouse_press, mouse_release=mouse_release)
