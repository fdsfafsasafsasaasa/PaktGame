from pyglet import window
from pyglet.window import key

from paktgame.player import Player

import pyglet


class Game(window.Window):
    def __init__(self, width, height, player: Player, title):
            super().__init__(width, height, title)
            self.width
            self.height
            self.player = player
            pyglet.gl.glClearColor(1.0, 1.0, 1.0, 0)

    def on_draw(self):
        self.clear()
        pyglet.gl.glClearColor(1.0, 1.0, 1.0, 0)
        self.player.draw()

    def on_key_press(self, symbol, modifiers):
        self.player.move(symbol)

    @staticmethod
    def run():
        try:
            pyglet.app.run()
        except KeyboardInterrupt:
            print("Exiting.")
            exit(0)
