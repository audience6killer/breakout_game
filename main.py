import turtle
from blocks import *


window_size = (650, 650)    # width, height
screen = turtle.Screen()
screen.tracer(0)
screen.title('Breakout')
screen.setup(width=window_size[0], height=window_size[1])
screen.bgcolor('black')

screen_blocks = Blocks(window_size)
screen_blocks.create_layers()

while True:
    screen.update()

screen.exitonclick()






