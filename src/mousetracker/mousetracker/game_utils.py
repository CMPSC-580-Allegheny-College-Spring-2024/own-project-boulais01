"""Define useful variables for the game."""

import pygame

pygame.init()
font = pygame.font.SysFont(None,50)

# define the questions
questions = {1: font.render("What's your favorite color?", True, (0,0,0)), 2: font.render("What's your favorite number?", True, (0,0,0))}

# define answers to question one and how much space they take up
answers1 = {1: font.render("Red", True, (255,0,0)), 2: font.render("Blue", True, (0,0,255)), 3: font.render("Green", True, (0,255,0))}
answers1_sizes = {1: answers1[1].get_size(), 2: answers1[2].get_size(), 3: answers1[3].get_size()}

# define answers to question two and how much space they take up
answers2 = {1: font.render("1", True, (255,0,0)), 2: font.render("2", True, (0,0,255)), 3: font.render("3", True, (0,255,0))}
answers2_sizes = {1: answers2[1].get_size(), 2: answers2[2].get_size(), 3: answers2[3].get_size()}