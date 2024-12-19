from draw_library import *

class Body:
    def __init__(self, name, mass, x, y, v_x, v_y,
                 pixel_radius, r, g, b):
        self.type = "body"
        self.name = name
        self.mass = mass
        self.x = x
        self.y = y
        self.v_x = v_x
        self.v_y = v_y
        self.pixel_radius = pixel_radius
        self.r = r
        self.g = g
        self.b = b

    def update_position(self, timestep):
        self.x = self.x + (self.v_x * timestep)
        self.y = self.y + (self.v_y * timestep)

    def update_velocity(self, ax, ay, timestep):
        self.v_x = self.v_x + (ax * timestep)
        self.v_y = self.v_y + (ay * timestep)

    def draw(self, cx, cy, pixels_per_meter):
        set_fill(self.r, self.g, self.b)

        x_position = cx + (self.x * pixels_per_meter)
        y_position = cy + (self.y * pixels_per_meter)

        draw_circle(self.type, self.name, x_position, y_position, self.pixel_radius)