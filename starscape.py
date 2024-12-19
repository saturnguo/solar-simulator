from draw_library import *
from star import Star
import random

class Starscape:
    def __init__(self):
        self.list_of_stars = []
        self.list_of_deleted_stars = []
        self.new_name = "x"

        self.timer = QTimer()
        self.timer.timeout.connect(self.add_star)
        self.timer.start(4000)

        self.initialize()

    def initialize(self):
        for i in range(1, 20):
            self.new_name = self.new_name + "x"
            new_star = Star(random.uniform(0, 399), random.uniform(0, 399), self.new_name)
            self.list_of_stars.append(new_star)
    
    def add_star(self):
        star_x = 0
        star_y = int(random.uniform(0, 400))
        self.new_name = self.new_name + "x"

        new_star = Star(star_x, star_y, self.new_name)
        self.list_of_stars.append(new_star)
    
    def maintain_list(self):

        i = len(self.list_of_stars) - 1
        while i >= 0:
            if self.list_of_stars[i].x >= 400:
                self.list_of_deleted_stars.append(self.list_of_stars[i])
                self.list_of_stars.remove(self.list_of_stars[i])
            i = i - 1

        for i in self.list_of_stars:
            i.x = i.x + .1
            i.draw()

        for i in self.list_of_deleted_stars:
            i.delete()
