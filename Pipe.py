# Class to hold the state of a pipe
class Pipe:
    def __init__(self,
        left_pos_x,
        gap_bottom_pos_y,
        gap_height=100,
        width=50,
        color=(30,200,20)
    ):
        self.left_pos_x = left_pos_x
        self.gap_bottom_pos_y = gap_bottom_pos_y
        self.gap_height = gap_height
        self.width = width
        self.color = color

    def step(self, x_velocity):
        # Integrate position by velocity
        self.left_pos_x += x_velocity
