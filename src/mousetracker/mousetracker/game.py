"""A simple game to display tracker functionality."""

# implement a simple pygame

import pygame


def game():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None,50)
    running = True

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("purple")

        # RENDER YOUR GAME HERE
        question = font.render("What's your favorite color?", True, (0,0,0))

        answer1 = font.render("Red", True, (255,0,0))
        answer2 = font.render("Blue", True, (0,0,255))
        answer3 = font.render("Green", True, (0,255,0))

        ans1_size = answer1.get_size()
        ans2_size = answer1.get_size()
        ans3_size = answer1.get_size()

        screen.blit(question, (360,0))

        screen.blit(answer1, (540,100))
        screen.blit(answer2, (540,200))
        screen.blit(answer3, (540,300))
        # flip() the display to put your work on screen
        pygame.display.flip()

        pygame.event.get()
        button1 = pygame.mouse.get_pressed(num_buttons=3)[0]
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if button1 is True and mouse_x in range(540, 540+ans1_size[0]) and mouse_y in range(100, 100+ans1_size[1]):
            return ("Answer 1", pygame.mouse.get_rel())
        elif button1 is True and mouse_x in range(540, 540+ans2_size[0]) and mouse_y in range(200, 200+ans2_size[1]):
            return ("Answer 2", pygame.mouse.get_rel())
        elif button1 is True and mouse_x in range(540, 540+ans3_size[0]) and mouse_y in range(300, 300+ans3_size[1]):
            return ("Answer 3", pygame.mouse.get_rel())


        clock.tick(60)  # limits FPS to 60

    pygame.quit()


if __name__ == "__main__":
    answer = game()
    print(f"Player chose {answer[0]} and their mouse moved {answer[1]}")