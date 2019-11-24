#!/usr/bin/env python3
from FlappyBirdGame import *
from FlappyBirdView import *
from Bird import *
from BirdBrainSimple import *


if __name__ == '__main__':
    game_size = (640, 1000)

    game = FlappyBirdGame(game_size[0], game_size[1])

    # Create computer-controlled bird
    game.add_bird(Bird(brain=BirdBrainSimple(game), name="Computer"))

    # Create player's bird
    player_bird = Bird(color=(255,0,0), name="Player")
    game.add_bird(player_bird)

    # Create View, and give it a reference to the player's
    # bird so it can be controlled by the keyboard
    view = FlappyBirdView(game, "Flappy Bird", fps=60, player_bird=player_bird)

    running = True

    num_frames = 0

    while running:
        game.step()

        if view:
            view.update()
            running = view.is_running()

        num_frames += 1

    print("frames: %d" % num_frames)

