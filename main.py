import pyglet
import numpy as np
import random

# rectangle class


class Rect:

    def __init__(self, x, y, w, h):
        self.set(x, y, w, h)

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def draw(self):
        pyglet.graphics.draw(4, pyglet.gl.GL_QUADS, self._quad)

    def set(self, x=None, y=None, w=None, h=None):
        self._x = self._x if x is None else x
        self._y = self._y if y is None else y
        self._w = self._w if w is None else w
        self._h = self._h if h is None else h
        self._quad = ('v2f', (self._x, self._y,
                              self._x + self._w, self._y,
                              self._x + self._w, self._y + self._h,
                              self._x, self._y + self._h))

    def __repr__(self):
        return f"Rect(x={self._x}, y={self._y}, w={self._w}, h={self._h})"


class Window(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        wWidth = self.width
        wHeight = self.height

        resolution = 50
        spacing = 2

        self.rects = [[None] * resolution for i in range(resolution)]

        for x in range(0, resolution):
            for y in range(0, resolution):
                self.rects[x][y] = Rect(
                    x * (wWidth / resolution) + (spacing / 2),
                    y * (wHeight / resolution) + (spacing / 2),
                    wWidth / resolution - spacing,
                    wHeight / resolution - spacing
                )

    def on_draw(self):
        self.clear()

        for row in self.rects:
            for rect in row:
                rect.draw()

    def update(self, dt):
        for row in self.rects:
            for rect in row:
                randX = random.randrange(-1, 2)
                randY = 0
                x = rect.x + randX
                y = rect.y + randY

                rect.set(x, y)


window = Window(1200, 720)
pyglet.clock.schedule_interval(window.update, 1/120)
pyglet.app.run()
