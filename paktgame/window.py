from pyglet import window

import pyglet

class GameWindow(window.Window):
    def __init__(self, width, height):
            super().__init__(width, height)
            self.width
            self.height

    @staticmethod
    def run():
        pyglet.app.run()