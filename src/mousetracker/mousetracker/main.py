"""In which to build the prototype of a mouse tracking tool using pygame"""

# data we're looking for:
# choice, time to choice, mouse location at each point in time
# perhaps a dictionary;
# {"choice_point_or_id": {"choice": [(1sec, point), (2sec, point), ..., (Lastsec, point)]}}

import pygame
import typer

from rich.console import Console

cli = typer.Typer()

console = Console()


@cli.command()
def main():
    """Run mouse tracker with some demo game probably."""
    # TODO: Establish calls outline
    # TODO: fix doc string
    # idea: make a simple two choice thing
    # run it here - by passing into tool main function?
    # display output neatly