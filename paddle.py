import turtle


class Paddle(turtle.Turtle):
    def __init__(self, window_size: tuple):
        """This class implements a paddle which the player will move along the bottom screen width"""
        super().__init__()
        self.window_size = window_size
        self.shape("square")
        self.color('white')
        self.penup()

        self.paddle_length = window_size[0] * 0.1
        paddle_stretch_length = self.paddle_length / 20
        self.shapesize(stretch_wid=1, stretch_len=paddle_stretch_length)
        margin = 20
        self.goto(y=(-window_size[1]/2)+margin, x=0)

    def move_right(self):
        if abs(self.xcor() + 20) < (self.window_size[0] - self.paddle_length)/2:
            new_x = self.xcor() + 20
            self.goto(x=new_x, y=self.ycor())

    def move_left(self):
        if abs(self.xcor() - 20) < (self.window_size[0] - self.paddle_length)/2:
            new_x = self.xcor() - 20
            self.goto(x=new_x, y=self.ycor())

