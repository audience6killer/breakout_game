import turtle

class Scoreboard(turtle.Turtle):
    def __init__(self, window_size: tuple):
        """This class implements the scoreboard
        window_size: (width, height)"""
        super().__init__()
        self.window_size = window_size
        self.current_level = 1
        self.lives_left = 4
        self.FONT = ('Ubuntu', 24, 'bold')
        self.color('white')
        self.penup()
        self.hideturtle()

    def update_level(self):
        margin = 40
        self.goto(x=0, y=self.window_size[1]/2 - margin)
        self.clear()
        score_msg = f"Level {self.current_level}\tLives {self.lives_left}"
        self.write(arg=score_msg, move=False, align='center', font=self.FONT)

    def decrease_lives(self) -> bool:
        """This method decreases the lives left and tell if the game is over"""
        self.lives_left -= 1
        if not self.lives_left:
            self.game_over()
            return False
        else:
            return True

    def game_over(self):
        margin = 40
        self.goto(x=0, y=0)
        self.clear()
        score_msg = "Game Over"
        self.write(arg=score_msg, move=False, align='center', font=('Ubuntu', 30, 'bold'))
