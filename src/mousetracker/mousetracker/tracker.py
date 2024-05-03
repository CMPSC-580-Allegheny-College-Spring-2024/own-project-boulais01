"""The main functionality of the mouse tracker."""

# create mouse tracker
# reference main for expected return
import pygame
import time

pygame.init()

def tracker(game_func: callable):
    """Uses pygame functionality to track mouse movement."""
    def wrap(*args, **kwargs): 
        start = time.time() 
        result = game_func(*args, **kwargs) 
        end = time.time() 
          
        print(game_func.__name__, end-start) 
        return result 
    return wrap 