from draw_library import *

class Star:
    def __init__(self, x, y, name):
        self.type = "star"
        self.x = x
        self.y = y
        self.name = name
        self.pixel_radius = 1.25
        self.r = 255
        self.g = 255
        self.b = 255

    def draw(self):
        set_fill(self.r, self.b, self.g)
        draw_circle(self.type, self.name, self.x, self.y, self.pixel_radius)

    def delete(self):
        delete_circle(self.name)
