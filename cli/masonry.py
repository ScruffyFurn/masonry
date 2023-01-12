# Imports
import click
from library import library
from notebook import notebook


@click.group()
def cli():
    pass


cli.add_command(library)
cli.add_command(notebook)

if __name__ == "__main__":
    cli()
