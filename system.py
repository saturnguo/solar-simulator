from body import Body
import math

G = 6.67384e-11

class System:
    def __init__(self, body_list):
        self.body_list = body_list

    def compute_acceleration(self, n):
        ax = 0
        ay = 0

        for i in range(len(self.body_list)):

            if i != n:

                x_distance = self.body_list[i].x - self.body_list[n].x
                y_distance = self.body_list[i].y - self.body_list[n].y
                distance = math.sqrt(x_distance * x_distance + y_distance * y_distance)

                a = G * (self.body_list[i].mass / (distance * distance))

                ax = ax + a * (x_distance/distance)
                ay = ay + a * (y_distance/distance)

        return ax, ay

    def large(self):
        for i in range(len(self.body_list)):
            if i != 0:
                self.body_list[i].grow_larger()
   
    def update(self, timestep):
        for i in range(len(self.body_list)):
            (ax, ay) = self.compute_acceleration(i)
            self.body_list[i].update_velocity(ax, ay, timestep)
            self.body_list[i].update_position(timestep)

    def draw(self, cx, cy, pixels_per_meter):
        for i in range(len(self.body_list)):
            self.body_list[i].draw(cx, cy, pixels_per_meter)
