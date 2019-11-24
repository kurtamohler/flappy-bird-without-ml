# Class to automatically control a bird.
#
# This is one of the simplest possible ways to solve
# Flappy Bird. First, it calculates the next vertical
# position of the bird based on the current position
# and velocity. Then it determines if the bottom side of
# the bird will be below the top of the current pipe.
# If it is below, the bird jumps; if not, the bird does
# nothing.
#
# An important caveat to this method is that the pipe
# gap must be taller than the bird's jumping arc--which
# is true in the original Flappy Bird game.
class BirdBrainSimple:
    def __init__(self, game):
        # The brain needs to be aware of its environment,
        # so we allow it to access the game's data members
        self.game = game

    def step(self, bird):
        do_jump = False
        min_pos_y = 0

        next_pos_y = bird.pos_y + bird.vel_y - bird.radius

        if len(self.game.pipes) > 0:
            # Find the closest pipe to the right of the bird
            for pipe in self.game.pipes:
                if (pipe.left_pos_x + pipe.width) >= (bird.pos_x-bird.radius):
                    min_pos_y = pipe.gap_bottom_pos_y
                    break

        if next_pos_y <= min_pos_y:
            do_jump = True

        return do_jump