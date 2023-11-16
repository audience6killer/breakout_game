import turtle


class Block(turtle.Turtle):
    def __init__(self, width, length):
        """This class will implement the blocks that ment to be broken in the game"""
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        if width and length:
            self.shapesize(stretch_wid=width, stretch_len=length)


class Blocks:
    def __init__(self, window_size):
        self.window_size = window_size
        self.top_margin = 100
        self.layers = []
        self.NO_LAYERS = 6
        self.BLOCKS_NUMBER = 14

    def create_layers(self):
        """The window width represents the 100%, the block's represents the 90%
         and the spaces between each block represents the 10% left"""
        window_width = self.window_size[0]
        window_height = self.window_size[1]

        # Turtle default size = 20x20px, we want that no matter the size of the screen, there will be
        # 14 blocks per row
        blocks_space = window_width * 0.9
        blocks_width = blocks_space / self.BLOCKS_NUMBER
        block_stretch_width = blocks_width / 20  # 20px is the width of the turtle, this is the value for width_stretch
        block_width = 20 * block_stretch_width

        spaces_width = window_width - blocks_space
        space_width = spaces_width / (self.BLOCKS_NUMBER - 1)

        # The first part represents the columns and the later the rows
        self.layers = [[Block(width=1, length=block_stretch_width) for _ in range(self.BLOCKS_NUMBER)] for _ in range(self.NO_LAYERS)]

        # We now set the blocks on its place, beginning from the top left corner of the window
        top_y = (window_height / 2) - self.top_margin
        base_color = 0xD0A2F7
        for row in self.layers:
            left_x = - (window_width / 2) + block_width/2
            for block in row:
                color = hex(base_color).split('x')[1]
                block.goto(x=left_x, y=top_y)
                block.color(f"#{color}")
                left_x += block_width + space_width
            base_color += 0x00F000
            top_y -= 30




