import click


# Notebook group
@click.group()
def notebook():
    pass


# Create a new DataBrick notebook
@click.command()
@click.option(
    "--name",
    default="",
    help="Name of the DataBricks orchistrator notebook being created",
)
@click.option(
    "--dir",
    default="../",
    help="Location to create the new Databricks orchistrator notebook \
         being created",
)
def create(name, dir):
    click.echo("Creating a new DataBricks orchistrator notebook..")
    try:
        with open(dir + "/orchistrator.py", "w") as file:
            file.write("Create a new text file!")
    except FileNotFoundError:
        click.echo("The" + dir + " directory does not exist")


notebook.add_command(create)
