import typer

app = typer.Typer()

@app.command()
def greet(name: str):
    typer.echo(f"Hello {name}!")

@app.command()
def farewell(name: str):
    typer.echo(f"Goodbye {name}!")

def main(name: str, age: int = typer.Option(18, help="Your age")):
    typer.echo(f"Hello {name}, you are {age} years old!")

if __name__ == "__main__":
    app()
    typer.run(main)
