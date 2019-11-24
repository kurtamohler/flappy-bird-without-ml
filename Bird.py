# This class holds and controls the state of a bird
class Bird:
    def __init__(self,
        pos_x = 0,
        pos_y = 0,
        radius=10,
        color=(255,100,80),
        outline_color=(0,0,0),
        jump_vel=8,
        brain=None,
        name="bird"
    ):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.radius = radius
        self.color = color
        self.outline_color = outline_color
        self.vel_y = 0
        self.jump_vel = jump_vel
        self.is_jumping = False
        self.alive = False 
        self.brain = brain
        self.name = name

    def is_alive(self):
        return self.alive

    def set_alive(self, alive):
        if not alive:
            print("%s died!" % self.name)
        self.alive = alive

    def set_position(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y

    def reset(self, pos_x, pos_y, alive=True, vel_y=0):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.alive = alive
        self.vel_y = vel_y

    def schedule_jump(self):
        self.is_jumping = True

    # Step simulation forward one frame
    def step(self, acceleration):
        # If bird has a brain, get its action
        if self.brain:
            self.is_jumping = self.brain.step(self)


        if self.is_jumping:
            self.vel_y = self.jump_vel
            self.is_jumping = False

        # Integrate position with velocity
        self.pos_y += self.vel_y

        # Integrate velocity with acceleration
        self.vel_y += acceleration

    def check_collide_ground(self):
        return (self.pos_y - self.radius) <= 0


    def get_display_params(self):
        x = int(self.pos_x)
        y = int(self.pos_y)
        radius = int(self.radius)

        return x, y, radius, self.color, self.outline_color
