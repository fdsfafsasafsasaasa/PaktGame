from pyglet import app

from window import GameWindow


window = GameWindow(640, 480)

from events import *

app.run()