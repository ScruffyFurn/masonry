# Imports
import click
from cookiecutter.main import cookiecutter
import subprocess


@click.group()
def cli():
    pass


# Library group
@click.group()
def library():
    pass


# Create new python library
@click.command()
@click.option('--name', default="DataBricks Library", help='Name of the python library being created')
@click.option('--desc', default="A new DataBricks Library", help='Simple description of the python library being created')
@click.option('--author', default="Masonry", help='Name of the python library creator')
@click.option('--dir', default="./", help="Location to create the new Databricks library being created")
def create(name, desc, author, dir):
    config_object = {
        "author_name": author,
        "project_name": name,
        "project_slug": "{{ cookiecutter.project_name.lower().replace(' ', '_').replace('-', '_') }}",
        "project_short_description": desc
    }
    cookiecutter('https://github.com/ScruffyFurn/masonry-slug', output_dir=dir, extra_context=config_object)

# Build group
@click.command()
def build():
    click.echo('Running the build command...')
    subprocess.check_call(["make", "build"])


# Test Group
@click.command()
def test():
    click.echo('Running the python tests...')
    subprocess.check_call(["make", "test"])


# Lint Group
@click.command()
def lint():
    click.echo('Running the linting checks...')
    subprocess.check_call(["make", "lint"])


# Clean Group
@click.command()
def clean():
    click.echo('Running the linting checks...')
    subprocess.check_call(["make", "clean"])


library.add_command(create)
library.add_command(build)
library.add_command(test)
library.add_command(lint)

# Notebook group
@click.group()
def notebook():
    pass


# Create a new DataBrick notebook
@click.command()
@click.option('--name', default="", help='Name of the DataBricks orchistrator notebook being created')
@click.option('--dir', default="../", help="Location to create the new Databricks orchistrator notebook being created")
def create(name, dir):
    click.echo('Creating a new DataBricks orchistrator notebook..')
    try:
        with open(dir + '/orchistrator.py', 'w') as file:
            file.write('Create a new text file!')
    except FileNotFoundError:
        click.echo('The' + dir + ' directory does not exist')


notebook.add_command(create)


cli.add_command(library)
cli.add_command(notebook)

if __name__ == '__main__':
    cli()
