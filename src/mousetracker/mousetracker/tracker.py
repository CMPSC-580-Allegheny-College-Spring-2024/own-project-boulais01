"""The main functionality of the mouse tracker."""

# create mouse tracker
# reference main for expected return
import pygame
import time

pygame.init()

def tracker(game_func: callable) -> tuple:
    """Uses pygame functionality to track mouse movement."""
    def wrap(*args, **kwargs): 
        start = time.perf_counter()
        result = game_func(*args, **kwargs) 
        end = time.perf_counter()
          
        return (result, end - start) 
    return wrap 