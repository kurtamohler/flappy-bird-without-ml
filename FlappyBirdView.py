import pygame

# Class used to display the current state of a FlappyBirdGame
class FlappyBirdView:
    def __init__(self,
        flappyBirdGame,
        windowName,
        fps=None,
        player_bird=None
    ):
        self.game = flappyBirdGame
        self.fps = fps

        pygame.init()

        (self.x_max, self.y_max) = self.game.get_size()

        self.screen = pygame.display.set_mode(
            (self.x_max, self.y_max)
        )

        pygame.display.set_caption(windowName)

        self.clock = pygame.time.Clock()

        self.running = True
        self.player_bird = player_bird

    def is_running(self):
        return self.running

    def poll_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.player_bird:
                        self.player_bird.schedule_jump()


    def limit_fps(self):
        if self.fps:
            self.clock.tick(self.fps)

    def draw_birds(self):
        for x, y, radius, color, outline_color in self.game.get_alive_birds():

            # pygame's vertical coordinate is upside-down compared
            # to Flappy Bird simulation coordinate, so need to flip
            y = self.y_max - y

            pygame.draw.circle(
                self.screen,
                color,
                (x, y),
                radius
            )

    def draw_pipes(self):
        for pipe in self.game.pipes:
            bottom_rect = pygame.Rect(
                pipe.left_pos_x,
                self.y_max - pipe.gap_bottom_pos_y,
                pipe.width,
                pipe.gap_bottom_pos_y
            )

            top_rect = pygame.Rect(
                pipe.left_pos_x,
                0,
                pipe.width,
                self.y_max - pipe.gap_bottom_pos_y-pipe.gap_height
            )

            pygame.draw.rect(
                self.screen,
                pipe.color,
                bottom_rect
            )

            pygame.draw.rect(
                self.screen,
                pipe.color,
                top_rect
            )



    def update(self):
        self.limit_fps()

        self.screen.fill((100,150,255))

        self.draw_birds()
        self.draw_pipes()

        pygame.display.flip()

        self.poll_events()