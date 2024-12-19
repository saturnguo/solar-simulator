import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QBrush, QPen, QColor, QPainter, QMouseEvent
from PyQt5.QtWidgets import (QGraphicsScene, QGraphicsView, QApplication, 
                             QGraphicsEllipseItem, QGraphicsRectItem, QGraphicsView)

WINDOW_WIDTH = 7000
WINDOW_HEIGHT = 7000

class Background(QtWidgets.QWidget):
    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        pen = QPen(QColor(0, 0, 0, 255))
        qp.setPen(pen)
        qp.drawRect(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)

class GraphicsWindow(QtWidgets.QMainWindow):
    def __init__(self, main, x, y, framerate, mouse_press, mouse_release):
        super().__init__()
        self.main = main
        self.x = x
        self.y = y
        self.framerate = framerate
        self.mouse_press = mouse_press
        self.mouse_release = mouse_release
        self.mx = None
        self.my = None
        self.mouse_pressed = None

        self.r = 255
        self.g = 255
        self.b = 255
        self.color = QColor()
        self.brush = QColor(self.r, self.g, self.b, 255)
        self.pen = QColor(self.r, self.g, self.b, 255)

        self.list_of_bodies = []
        self.list_of_stars = []

        self.factor = 1.2
        self.scene = QGraphicsScene(0, 0, self.x, self.y)
        self.view = QGraphicsView(self.scene)
        self.view.setRenderHint(QPainter.Antialiasing)
        self.view.setViewportMargins(0, 0, 0, 0)
        self.setCentralWidget(self.view)
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.rendering)
        self.timer.start(int(950 / self.framerate))

        self.background = Background()
        self.background.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.scene.addWidget(self.background)
        self.zoom_count = 0

        QtWidgets.QShortcut("+", self.view, activated=self.zoom_in)
        QtWidgets.QShortcut("=", self.view, activated=self.zoom_in)
        QtWidgets.QShortcut("-", self.view, activated=self.zoom_out)

    def zoom_in(self):
        self.view.scale(self.factor, self.factor)
        self.zoom_count = self.zoom_count - 1

    def zoom_out(self):
        inverted_factor = 1 / self.factor

        current_rect = self.view.mapToScene(self.view.viewport().geometry()).boundingRect()
        if (current_rect.width() * inverted_factor > WINDOW_WIDTH or
            current_rect.height() * inverted_factor > WINDOW_HEIGHT):
            return
        
        if self.zoom_count < 8:
            self.view.scale(inverted_factor, inverted_factor)
            self.zoom_count = self.zoom_count + 1

    def draw(self):
        self.show()
        app.exec_()

    def rendering(self):
        for i in self.list_of_bodies:
            i.draw()

        self.update()
        self.main()

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

    def draw_circle(self, type, name, x, y, radius):
        if type == "body":
            existing_body = None
            existing_body = next((i for i in self.list_of_bodies if i.name == name), None)
            
            if existing_body:
                existing_body.x = x
                existing_body.y = y
                existing_body.radius = radius

                existing_body.ellipse.setRect(0, 0, existing_body.diameter, existing_body.diameter)
                existing_body.ellipse.setPos(x - radius, y - radius)

            if not existing_body:
                new_object = Circle(x, y, radius, name)

                new_object.ellipse.setBrush(self.brush)
                new_object.ellipse.setPen(self.pen)
                new_object.ellipse.setZValue(5)

                self.list_of_bodies.append(new_object)
                self.scene.addItem(new_object.ellipse)
                new_object.draw()
            
        if type == "star":
            existing_star = None
            existing_star = next((i for i in self.list_of_stars if i.name == name), None)

            if existing_star:
                existing_star.x = x
                existing_star.y = y
                
                existing_star.ellipse.setPos(x - radius, y - radius)
            
            if not existing_star:
                new_object = Circle(x, y, radius, name)

                new_object.ellipse.setBrush(self.brush)
                new_object.ellipse.setPen(self.pen)
                new_object.ellipse.setZValue(1)

                self.list_of_stars.append(new_object)
                self.scene.addItem(new_object.ellipse)
                new_object.draw()
    
    def delete_circle(self, name):
        del_circle = None
        del_circle = next((i for i in self.list_of_stars if i.name == name), None)

        if del_circle:
            if del_circle.ellipse.scene() is not None:
                self.scene.removeItem(del_circle.ellipse)

    def mousePressEvent(self, event: QMouseEvent):
        scene_pos = self.view.mapToScene(event.pos())
        self.mx = scene_pos.x()
        self.my = scene_pos.y()

        super().mousePressEvent(event)
        self.mouse_press(self.mx, self.my)

    def mouseReleaseEvent(self, event: QMouseEvent):
        self.mouse_pressed = False

        self.mouse_release()

class Circle:
    def __init__(self, x, y, radius, name):
        self.x = x
        self.y = y
        self.radius = radius
        self.diameter = self.radius * 2
        self.name = name
        self.ellipse = QGraphicsEllipseItem(0, 0, self.diameter, self.diameter)

    def draw(self):
        self.ellipse.setPos(self.x - self.radius, self.y - self.radius)


app = QApplication(sys.argv)
graphic_window = None

def set_fill(r, g, b):
    graphic_window.set_fill(r, g, b)

def set_line(r, g, b):
    graphic_window.set_line(r, g, b)

def draw_circle(type, name, x, y, r):
    graphic_window.draw_circle(type, name, x, y, r)

def mouse_press():
    if graphic_window.mouse_pressed:
        print(graphic_window.mx)
        print(graphic_window.my)

def delete_circle(name):
    graphic_window.delete_circle(name)

def set_background():
    set_fill(0, 0, 0)
    set_line(0, 0, 0)
    graphic_window.draw_background()

def start_graphics(main, width, height, framerate, mouse_press, mouse_release):
    global graphic_window

    graphic_window = GraphicsWindow(main, width, height, framerate, 
                                    mouse_press, mouse_release)
    
    set_background()
    graphic_window.draw()
