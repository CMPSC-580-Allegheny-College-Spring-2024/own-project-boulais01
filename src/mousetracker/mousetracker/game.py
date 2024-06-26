"""A simple game to display tracker functionality."""

# implement a simple pygame

import pygame

from mousetracker import game_utils, tracker
from typing import Union, Generator, Tuple

@tracker.tracker
def game() -> Union[Generator, Tuple]:
    """Run a simple game."""
    # pygame setup
    pygame.init()
    q1 = False
    q2 = False
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    initial_pos = pygame.mouse.get_pos()

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        yield pygame.mouse.get_pos()
        # fill the screen with a color to wipe away anything from last frame
        screen.fill("purple")

        # render game
        while q1 is False:
            screen.blit(game_utils.questions[1], (360,0))

            screen.blit(game_utils.answers1[1], (540,100))
            screen.blit(game_utils.answers1[2], (540,200))
            screen.blit(game_utils.answers1[3], (540,300))
            # flip() the display to put your work on screen
            pygame.display.flip()

            pygame.event.get()
            button1 = pygame.mouse.get_pressed(num_buttons=3)[0]
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # check that the mouse click was on an option
            if button1 is True and mouse_x in range(540, 540+game_utils.answers1_sizes[1][0]) and mouse_y in range(100, 100+game_utils.answers1_sizes[1][1]):
                movement = pygame.mouse.get_rel()
                yield ("Question 1", "Red", (initial_pos[0] - movement[0], initial_pos[1] - movement[1]))
                q1 = True
            elif button1 is True and mouse_x in range(540, 540+game_utils.answers1_sizes[2][0]) and mouse_y in range(200, 200+game_utils.answers1_sizes[2][1]):
                movement = pygame.mouse.get_rel()
                yield ("Question 1", "Blue", (initial_pos[0] - movement[0], initial_pos[1] - movement[1]))
                q1 = True
            elif button1 is True and mouse_x in range(540, 540+game_utils.answers1_sizes[3][0]) and mouse_y in range(300, 300+game_utils.answers1_sizes[3][1]):
                movement = pygame.mouse.get_rel()
                yield ("Question 1", "Green", (initial_pos[0] - movement[0], initial_pos[1] - movement[1]))
                q1 = True

        # once q1 is complete, bring up q2
        while q1 and not q2:
            screen.fill("purple")

            screen.blit(game_utils.questions[2], (360,0))

            screen.blit(game_utils.answers2[1], (540,100))
            screen.blit(game_utils.answers2[2], (540,200))
            screen.blit(game_utils.answers2[3], (540,300))
            # flip() the display to put your work on screen
            pygame.display.flip()

            pygame.event.get()
            button1 = pygame.mouse.get_pressed(num_buttons=3)[0]
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if button1 is True and mouse_x in range(540, 540+game_utils.answers2_sizes[1][0]) and mouse_y in range(100, 100+game_utils.answers2_sizes[1][1]):
                movement2 = pygame.mouse.get_rel()
                yield ("Question 2", "1", (movement[0] - movement2[0], movement[1] - movement2[1]))
                q2 = True
                pygame.event.post(pygame.event.Event(pygame.QUIT))
            elif button1 is True and mouse_x in range(540, 540+game_utils.answers2_sizes[2][0]) and mouse_y in range(200, 200+game_utils.answers2_sizes[2][1]):
                movement2 = pygame.mouse.get_rel()
                yield ("Question 2", "2", (movement[0] - movement2[0], movement[1] - movement2[1]))
                q2 = True
                pygame.event.post(pygame.event.Event(pygame.QUIT))
            elif button1 is True and mouse_x in range(540, 540+game_utils.answers2_sizes[3][0]) and mouse_y in range(300, 300+game_utils.answers2_sizes[3][1]):
                movement2 = pygame.mouse.get_rel()
                yield ("Question 2", "3", (movement[0] - movement2[0], movement[1] - movement2[1]))
                q2 = True
                pygame.event.post(pygame.event.Event(pygame.QUIT))

        clock.tick(60)  # limits FPS to 60

    pygame.quit()


if __name__ == "__main__":
    answer = game()