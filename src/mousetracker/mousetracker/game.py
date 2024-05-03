"""A simple game to display tracker functionality."""

# TODO: implement a simple pygame wih 2-3 choices

import pygame

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

    screen.blit(question, (360,0))

    screen.blit(answer1, (540,100))
    screen.blit(answer2, (540,200))
    screen.blit(answer3, (540,300))
    # flip() the display to put your work on screen
    pygame.display.flip()

    for event in pygame.event.get():
        button1 = pygame.mouse.get_pressed(num_buttons=3)[0]
        #if button1 is True:


    clock.tick(60)  # limits FPS to 60

pygame.quit()