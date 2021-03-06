__author__ = 's15008'

import pyglet
import game

WIDTH = 400
HEIGHT = 600

if __name__ == '__main__':
    block_image = pyglet.resource.image('block.png')
    ball_image = pyglet.resource.image('ball.png')
    window = pyglet.window.Window( WIDTH, HEIGHT)
    g = game.Game( window)
    g.create_blocks( block_image)
    g.create_ball( ball_image)

    @window.event
    def on_draw():
        window.clear()
        g.draw()

    def update(dt):
        g.update()

    pyglet.clock.schedule_interval( update, 1/60.0)
    pyglet.app.run()
