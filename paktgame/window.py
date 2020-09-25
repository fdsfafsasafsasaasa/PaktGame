from pyglet import window
from pyglet.window import key

from paktgame.player import Player

import pyglet


class Game(window.Window):
    def __init__(self, width, height, player: Player):
            super().__init__(width, height)
            self.width
            self.height
            self.player = player
            pyglet.gl.glClearColor(0.5,0,0,1)

    def on_draw(self):
        self.clear()
        pyglet.gl.glClearColor(0.5,0,0,1)
        self.player.draw()

    def on_key_press(self, symbol, modifiers):
        if symbol == key.A:
            self.player.update()

    @staticmethod
    def run():
        try:
            pyglet.app.run()
        except KeyboardInterrupt:
            print("Exiting.")
            exit(0)
