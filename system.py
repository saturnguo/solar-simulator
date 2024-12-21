from body import Body
from sollib_wrapper import compute_acceleration
import math

G = 6.67384e-11

class System:
    def __init__(self, body_list):
        self.body_list = body_list

    def compute_acceleration(self, n):
        n_body = self.body_list[n]
        i_bodies = [m for i, m in enumerate(self.body_list) if i != n]

        i_x = [i.x for i in i_bodies]
        i_y = [i.y for i in i_bodies]
        i_mass = [i.mass for i in i_bodies]

        ax, ay = compute_acceleration(n_body.x, n_body.y, i_mass, i_x, i_y)

        return ax, ay
   
    def update(self, timestep):
        for i in range(len(self.body_list)):
            (ax, ay) = self.compute_acceleration(i)
            self.body_list[i].update_velocity(ax, ay, timestep)
            self.body_list[i].update_position(timestep)

    def draw(self, cx, cy, pixels_per_meter):
        for i in range(len(self.body_list)):
            self.body_list[i].draw(cx, cy, pixels_per_meter)
