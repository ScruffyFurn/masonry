# Imports
import click

from masonry import library, notebook


@click.group()
def cli():
    pass


cli.add_command(library.library)
cli.add_command(notebook.notebook)

if __name__ == "__main__":
    cli()
