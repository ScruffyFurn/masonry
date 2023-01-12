import click
import subprocess
from cookiecutter.main import cookiecutter

# Library group
@click.group()
def library():
    pass


# Create new python library
@click.command()
@click.option(
    "--name",
    default="DataBricks Library",
    help="Name of the python library being created",
)
@click.option(
    "--desc",
    default="A new DataBricks Library",
    help="Simple description of the python library being created",
)
@click.option("--author", default="Masonry", help="Name of the \
    python library creator")
@click.option(
    "--dir",
    default="./",
    help="Location to create the new Databricks library being created",
)
def create(name, desc, author, dir):
    config_object = {
        "author_name": author,
        "project_name": name,
        "project_slug": "{{ cookiecutter.project_name.lower().replace(' ', \
            '_').replace('-', '_') }}",
        "project_short_description": desc,
    }
    cookiecutter(
        "https://github.com/ScruffyFurn/masonry-slug",
        output_dir=dir,
        extra_context=config_object,
    )

# Build group
@click.command()
def build():
    click.echo("Running the build command...")
    subprocess.check_call(["make", "build"])


# Test Group
@click.command()
def test():
    click.echo("Running the python tests...")
    subprocess.check_call(["make", "test"])


# Lint Group
@click.command()
def lint():
    click.echo("Running the linting checks...")
    subprocess.check_call(["make", "lint"])


# Clean Group
@click.command()
def clean():
    click.echo("Running the linting checks...")
    subprocess.check_call(["make", "clean"])


library.add_command(create)
library.add_command(build)
library.add_command(test)
library.add_command(lint)
