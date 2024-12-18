import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QBrush, QPen, QColor, QPainter, QMouseEvent
from PyQt5.QtWidgets import (QGraphicsScene, QGraphicsView, QApplication, 
                             QGraphicsEllipseItem, QGraphicsRectItem, QGraphicsView)


class GraphicsWindow(QGraphicsView):
    def __init__(self, main, x, y, framerate, mouse_press, mouse_release):
        super().__init__()
        self.main = main
        self.x = x
        self.y = y
        self.framerate = framerate
        self.mouse_press = mouse_press
        self.mouse_release = mouse_release
        self.scene = QGraphicsScene(0, 0, self.x, self.y)
        self.scene.setSceneRect(0, 0, self.x, self.y)
        self.view = self.setScene(self.scene)
        self.setRenderHint(QPainter.Antialiasing)
        self.r = 255
        self.g = 255
        self.b = 255
        self.color = QColor()
        self.brush = QColor(self.r, self.g, self.b, 255)
        self.pen = QColor(self.r, self.g, self.b, 255)
        self.list_of_circles = []
        self.mx = None
        self.my = None
        self.mouse_pressed = None
        self.timer = QTimer()
        self.timer.timeout.connect(self.rendering)
        self.timer.start(int(950 / self.framerate))
        self.setViewportMargins(0, 0, 0, 0)

    def draw(self):
        self.show()
        app.exec_()

    def rendering(self):
        for i in self.list_of_circles:
            i.draw()

        self.scene.clear()
        self.list_of_circles = []
        self.main()
        self.update()

    def set_fill(self, red, green, blue):
        self.r = int(red)
        self.g = int(green)
        self.b = int(blue)

        self.color = QColor(self.r, self.g, self.b, 255)
        self.brush = QBrush(self.color)

    def set_line(self, red, green, blue):
        self.r = int(red)
        self.g = int(green)
        self.b = int(blue)

        self.color = QColor(self.r, self.g, self.b, 255)
        self.pen = QPen(self.color)
    
    def draw_background(self):
        rect = QGraphicsRectItem(0, 0, self.x * 2, self.y * 2)
        rect.setPos(0, 0)
        rect.setPen(self.pen)
        rect.setBrush(self.brush)
        rect.setZValue(0)

        self.scene.addItem(rect)

    def draw_circle(self, x, y, radius):
        new_object = Circle(x, y, radius)
        new_object.ellipse.setBrush(self.brush)
        new_object.ellipse.setPen(self.pen)
            
        new_object.draw()
        self.list_of_circles.append(new_object)
        self.scene.addItem(new_object.ellipse)

    def mousePressEvent(self, event: QMouseEvent):
        self.mx = event.x()
        self.my = event.y()
        self.mouse_pressed = True
        super().mousePressEvent(event)
        
        self.mouse_press(self.mx, self.my)

    def mouseReleaseEvent(self, event: QMouseEvent):
        self.mouse_pressed = False

        self.mouse_release()

class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.diameter = radius * 2
        self.ellipse = QGraphicsEllipseItem(0, 0, self.diameter, self.diameter)

    def draw(self):
        self.ellipse.setPos(self.x - self.radius, self.y - self.radius)


app = QApplication(sys.argv)
graphic_window = None

def set_fill(r, g, b):
    graphic_window.set_fill(r, g, b)

def set_line(r, g, b):
    graphic_window.set_line(r, g, b)

def draw_circle(x, y, r):
    graphic_window.draw_circle(x, y, r)

def mouse_press():
    if graphic_window.mouse_pressed:
        print(graphic_window.mx)
        print(graphic_window.my)

def set_background():
    set_fill(0, 0, 0)
    set_line(0, 0, 0)
    graphic_window.draw_background()

def start_graphics(main, width, height, framerate, mouse_press, mouse_release):
    global graphic_window

    graphic_window = GraphicsWindow(main, width, height, framerate, 
                                    mouse_press, mouse_release)
    graphic_window.draw()

