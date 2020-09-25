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
        self.image = pyglet.resource.image("assets/circle.jpg")
        super().__init__(self, self.image, x, y)

    def update(self):
        pass
    
    def move(self, symbol):
        if symbol == key.A:
            self.x -= 10
        elif symbol == key.D:
            self.x += 10
        elif symbol == key.S:
            self.y -= 10
        elif symbol == key.W:
            self.y += 10

