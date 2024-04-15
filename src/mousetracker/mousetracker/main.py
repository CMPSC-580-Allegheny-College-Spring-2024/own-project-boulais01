"""In which to build the prototype of a mouse tracking tool using pygame"""

import pygame
import typer

from rich.console import Console

cli = typer.Typer()

console = Console()


@cli.command()
def main():
    """Run mouse tracker with some demo game probably."""