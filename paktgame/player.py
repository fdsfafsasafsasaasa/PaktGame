from pyglet import sprite, image
from pyglet.window import key

import pyglet

class Player(sprite.Sprite):
    def __init__(self, x, y):
        """Player object extends pyglet.sprite.Sprite

        Args:
            x (int): x position
            y (int): y position
        """
        image = pyglet.image.load("assets/circle.png")
        super().__init__(image, x, y)
        self.image = image

    def update(self, symbol=None, collision=None):
        if collision:
            self.collide(collision)
        elif symbol:
            self.move(symbol)
    
    def move(self, symbol):
        if symbol == key.A:
            self.x -= 10
        elif symbol == key.D:
            self.x += 10
        elif symbol == key.S:
            self.y -= 10
        elif symbol == key.W:
            self.y += 10

