import turtle


class BreakoutScreen(turtle.Screen):
    def __init__(self, title, geometry):
        self.tracer(0)
        self.title(title)
        self.setup(width=geometry[0], height=geometry[1])
        self.bgcolor('black')



