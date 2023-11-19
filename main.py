import turtle
from blocks import *
from paddle import *
from ball import *
from scoreboard import *

window_size = (650, 650)    # width, height
screen = turtle.Screen()
screen.tracer(0)
screen.title('Breakout')
screen.setup(width=window_size[0], height=window_size[1])
screen.bgcolor('black')

screen_blocks = Blocks(window_size)
screen_blocks.create_layers()
paddle = Paddle(window_size)
ball = Ball(window_size)
score = Scoreboard(window_size)

paddle_to_ball_max_dis = ((paddle.paddle_length/2)**2 + (10+ball.ball_diameter/2)**2)**(1/2)
screen.listen()
screen.onkey(paddle.move_left, "Left")
screen.onkey(paddle.move_right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    score.update_level()
    ball.move()

    # Detect collision with wall
    if abs(ball.xcor()) > window_size[0]/2 - 10:
        ball.bounce_x()
    elif ball.ycor() > window_size[1]/2 - 50:
        ball.bounce_y()

    # Detect collision with the paddles
    if ball.distance(paddle) < 20:
        ball.bounce_y()
    elif ball.distance(paddle) <= paddle_to_ball_max_dis and abs(ball.ycor()) > (window_size[1]/2) - 40:
        ball.bounce_y()

    # Detect collision with the blocks
    if screen_blocks.collision_detect(ball):
        ball.bounce_y()

    # Detect ball out of bounds
    if ball.ycor() < -(window_size[1]/2):
        game_is_on = score.decrease_lives()
        ball.reset_position()

    # Next Level condition
    #if


screen.exitonclick()






