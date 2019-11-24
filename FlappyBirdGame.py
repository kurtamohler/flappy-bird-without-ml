import copy
import random
from collections import deque
from Pipe import *

# This class hold and controls the simulation state of the game
class FlappyBirdGame:
    def __init__(self,
        x_max=640,
        y_max=480,
        gravity_accel=-0.5,
        pipe_spacing=500,
        pipe_gap=100,
        pipe_width = 100,
        x_vel=4

    ):
        self.x_max = x_max
        self.y_max = y_max
        self.x_vel = x_vel
        self.pipe_spacing = pipe_spacing
        self.pipe_gap = pipe_gap
        self.pipe_width = pipe_width

        # Gravity acceleration unit is pixels per frame
        self.gravity_accel = gravity_accel

        self.birds = []
        self.pipes = deque()


    # Add a bird to the simulation
    def add_bird(self, bird):
        self.birds.append(bird)


    # Get the size of the simulation screen
    def get_size(self):
        return (self.x_max, self.y_max)


    # Remove all pipes and reset birds to the beginning
    def reset_scene(self):
        self.pipes.clear()

        start_x = int(self.x_max/3)
        start_y = int(self.y_max/2)

        for bird in self.birds:
            bird.reset(start_x, start_y)


    # Update bird positions and velocities
    def update_birds(self):
        any_birds_alive = False

        for bird in self.birds:
            if bird.is_alive():
                any_birds_alive = True
                bird.step(self.gravity_accel)

        return any_birds_alive

    # Update pipe positions based on scrolling speed. Spawn
    # new pipes if we've scrolled far enough, and delete
    # pipes that scroll off the edge of the screen
    def update_pipes(self):
        # Create a new pipe if there are none
        if len(self.pipes) == 0:
            self.pipes.append(Pipe(
                self.x_max,
                int(self.y_max/2),
                self.pipe_gap,
                self.pipe_width
            ))

        else:
            max_left_pos_x = 0

            # Update all pipe positions and find the leftmost one
            for pipe in self.pipes:
                pipe.step(-self.x_vel)

                max_left_pos_x = max(max_left_pos_x, pipe.left_pos_x)

            # remove leftmost pipe if it's offscreen
            if self.pipes[0].left_pos_x+self.pipes[0].width < 0:
                self.pipes.popleft()

            # if rightmost pipe is spaced far enough away from
            # right side of screen, add a new pipe
            if (self.x_max - max_left_pos_x) >= self.pipe_spacing:
                self.pipes.append(Pipe(
                    max_left_pos_x + self.pipe_spacing,
                    # int(self.y_max/2),
                    random.randrange(self.y_max/4, self.y_max*3/4),
                    self.pipe_gap,
                    self.pipe_width
                ))

    # Check if a bird and a pipe are colliding
    def check_bird_pipe_collision(self,
        bird,
        pipe
    ):
        collides = False

        # Check if any part of the bird intersects with any pipe
        # coordinates on the x axis
        is_in_pipe_x = ((bird.pos_x + bird.radius) > pipe.left_pos_x) \
            and ((bird.pos_x - bird.radius) < (pipe.left_pos_x + pipe.width))

        if is_in_pipe_x:
            gap_top_y = pipe.gap_bottom_pos_y + pipe.gap_height
            gap_bottom_y = pipe.gap_bottom_pos_y

            center_is_in_gap_y = (bird.pos_y < gap_top_y) and (bird.pos_y > gap_bottom_y)

            # If the center of the bird is not in the gap on the
            # y axis, then it's colliding with the the pipe
            if not center_is_in_gap_y:
                collides = True

            else:
                center_is_in_gap_x = (bird.pos_x > pipe.left_pos_x) \
                    and (bird.pos_x < (pipe.left_pos_x + pipe.width))

                if center_is_in_gap_x:
                    bird_top_is_in_top_pipe = (bird.pos_y + bird.radius) > \
                        (pipe.gap_bottom_pos_y + pipe.gap_height)

                    bird_bottom_is_in_bottom_pipe = (bird.pos_y - bird.radius) < \
                        pipe.gap_bottom_pos_y

                    if bird_bottom_is_in_bottom_pipe or bird_top_is_in_top_pipe:
                        collides = True

                else:
                    # Need to check distance from pipe corners
                    corners = [
                        (pipe.left_pos_x, pipe.gap_bottom_pos_y),
                        (pipe.left_pos_x, pipe.gap_bottom_pos_y+pipe.gap_height),
                        (pipe.left_pos_x+pipe.width, pipe.gap_bottom_pos_y),
                        (pipe.left_pos_x+pipe.width, pipe.gap_bottom_pos_y+pipe.gap_height),
                    ]

                    for corner_x, corner_y in corners:
                        dist_x = bird.pos_x - corner_x
                        dist_y = bird.pos_y - corner_y

                        dist_squ = dist_x*dist_x + dist_y*dist_y

                        if dist_squ < (bird.radius * bird.radius):
                            collides = True
                            break


        return collides


    # Check if all birds are colliding with either the ground
    # or a pipe. Kill any birds that are.
    def check_collisions(self):
        # Check collisions
        for bird in self.birds:
            if bird.is_alive(): 

                # Bird dies if collides with ground or first pipe
                if bird.check_collide_ground() or \
                    (len(self.pipes) > 0 and self.check_bird_pipe_collision(bird, self.pipes[0])):
                    bird.set_alive(False)


    # Step game simulation forward one frame
    def step(self):
        # If all birds are dead, reset scene. If not, perform
        # remaining frame updates
        if not self.update_birds():
            self.reset_scene()

        else:
            self.update_pipes()
            self.check_collisions()


    # Returns only birds that are alive
    def get_alive_birds(self):
        for bird in self.birds:
            if bird.is_alive():
                yield bird.get_display_params()


