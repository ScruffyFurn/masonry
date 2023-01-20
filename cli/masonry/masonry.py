# Imports
import click
import masonry


@click.group()
def cli():
    pass


cli.add_command(masonry.library.library)
cli.add_command(masonry.notebook.notebook)

if __name__ == "__main__":
    cli()
