import click

@click.command()
@click.group()
@click.option('--greeting', default='Hello', help='Greeting message')
@click.option('--name', prompt='Enter your name', help='Your name')
@click.option('--age', required=True, help='Your age')
@click.option('--verbose', is_flag=True, help='Enables verbose mode')
@click.option('--numbers', nargs=3, type=int, help='Three numbers')
@click.option('--names', multiple=True, help='Multiple names')
@click.option('--color', type=click.Choice(['red', 'blue', 'green']), help='Choose a color')
@click.option('--user-name', envvar='USER_NAME', help='Your name (from environment variable)')
def greet(greeting, name, age, verbose, numbers, names, color, user_name):
    """Simple program that greets the user."""
    click.echo(f"{greeting}, {name}!")
    click.echo(f"You are {age} years old.")
    if verbose:
        click.echo("Verbose mode is ON.")
    else:
        click.echo("Verbose mode is OFF.")
    click.echo(f"Sum: {sum(numbers)}")
    for n in names:
        click.echo(f"Hello, {n}!")
    click.echo(f"You chose {color}!")
    click.echo(f"Hello, {user_name}!")

@greet.command()
def hello():
    click.echo("Hello, world!")

@greet.command()
def bye():
    click.echo("Goodbye!")

if __name__ == '__main__':
    greet()
