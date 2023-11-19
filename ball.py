import turtle


class Ball(turtle.Turtle):
    def __init__(self, window_size: tuple):
        """This class implements the ball used in the game"""
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.ball_diameter = 20
        self.y_move = -3
        self.x_move = 3
        self.move_speed = 0.1
        self.penup()

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x, y=new_y)

    def bounce_y(self):
        """The bounce will be the same speed in y but in the opposite direction"""
        self.y_move *= -1
        self.move_speed *= 0.9

    def bounce_x(self):
        """The bounce will be in the opposite x direction"""
        self.x_move *= -1

    def reset_position(self):
        """Reset the position of the ball to the center of the screen"""
        self.goto(0,0)
        self.move_speed = 0.1
        self.y_move = 3
        self.bounce_y()

