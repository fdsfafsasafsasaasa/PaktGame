from paktgame.window import Game
from paktgame.player import Player

import pyglet
import os

window = Game(640, 480, Player(640//2, 480//2), "PaktGame")

# from paktgame.events import *

window.run()
