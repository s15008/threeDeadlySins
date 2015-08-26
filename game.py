__author__ = 's15008'

import pyglet
import math

class Game:
    def __init__( self, window):
        self.window = window
        self.block_list = []
        self.batch = pyglet.graphics.Batch()
        self.ball = None
        self.ball_angle = math.radians(45)
        self.ball_speed = 5

    def create_blocks( self, block_image):
        for y in range( 5):
            for x in range( 11):
                self.block_list.append(
                    pyglet.sprite.Sprite(
                        block_image, x * 30 + 35, y * 20 + 450,
                        batch = self.batch
                    )
                )

    def create_ball( self, ball_image):
        self.ball = pyglet.sprite.Sprite(
            ball_image, 100, 100, batch = self.batch
        )

    def draw( self):
        self.batch.draw()

    def update( self):
        self.move_ball()

    def change_ball_angele( self, positive=True):
        if positive:
            self.ball_angle += math.radians(90)
        else:
            self.ball_angle -= math.radians(90)

    def move_ball(self):
        x = math.cos( self.ball_angle) * self.ball_speed
        y = math.sin( self.ball_angle) * self.ball_speed

        # Collision Detection
        ## Game window walls
        if self.ball.x + x >= self.window.width:
            x = self.window.width - ( self.ball.x + x)
            self.change_ball_angele( y > 0)

        if self.ball.x + x <= 0:
            x = abs( self.ball.x + x)
            self.change_ball_angele( y < 0)

        if self.ball.y + y >= self.window.height:
            x = self.window.height - ( self.ball.y + y)
            self.change_ball_angele( x < 0)

        self.ball.x += x
        self.ball.y += y

class Block:
    BLOCK_WIDTH = 30
    BLOCK_HEIGHT = 20
    X_MARGIN = 35
    Y_MARGIN = 400

    def __init__( self, x, y, image):
        self.x = x
        self.y = y
        self.image = image

    def draw(self):
        x = self.x * Block.BLOCK_WIDTH + Block.X_MARGIN
        y = self.y * Block.BLOCK_HEIGHT + Block.Y_MARGIN
        self.image.blit( x, y)

