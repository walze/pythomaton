import pyglet
import numpy as np

# rectangle class


class Rect:

    def __init__(self, x, y, w, h):
        self.set(x, y, w, h)

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


# main function
def main():
    wWidth = 800
    wHeight = 600
    window = pyglet.window.Window(wWidth, wHeight)
    resolution = 20
    spacing = 2

    rects = [[None] * resolution for i in range(resolution)]
    print(rects)

    for x in range(0, resolution):
        for y in range(0, resolution):
            rects[x][y] = Rect(
                x * (wWidth / resolution) + (spacing / 2),
                y * (wHeight / resolution) + (spacing / 2),
                wWidth / resolution - spacing,
                wHeight / resolution - spacing
            )

    # draw func
    @window.event
    def on_draw():
        window.clear()

        for row in rects:
            for rect in row:
                print(rect)
                rect.draw()

    pyglet.app.run()


if __name__ == '__main__':
    main()
