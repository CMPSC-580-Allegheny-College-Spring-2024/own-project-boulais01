"""In which to build the prototype of a mouse tracking tool using pygame"""

# data we're looking for:
# choice, time to choice, mouse location at each point in time
# perhaps a dictionary;
# {"choice_point_or_id": {"choice": [(1sec, point), (2sec, point), ..., (Lastsec, point)]}}
# for the bigger/final complete work it can be made into a json

import typer

from rich.console import Console
from mousetracker import game, processing

cli = typer.Typer()

console = Console()


@cli.command()
def main():
    """Run mouse tracker with demo game."""
    # run game
    # save file
    # display output
    game_output = game.game()
    file_save = processing.save(game_output)
    processing.display(file_save)
