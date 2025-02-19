import os
import click
from click_shell import shell

# Define a shell application
@shell(prompt="myapp > ", intro="Welcome to MyApp shell!")
def my_shell():
    pass

# Define a command inside the shell
@my_shell.command()
def hello():
    """Say hello"""
    click.echo("Hello, world!")

@my_shell.command()
@click.argument("cmd")
def run(cmd):
    """Execute a system command"""
    os.system(cmd)

# Define another command
@my_shell.command()
@click.argument("name")
def greet(name):
    """Greet a user"""
    click.echo(f"Hello, {name}!")

# Run the shell
if __name__ == "__main__":
    my_shell()
