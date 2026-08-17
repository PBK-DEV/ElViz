import typer
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def new() -> None:
    """Init new project"""
    ...


@app.command()
def save_as_template() -> None:
    """Save this project as a template"""
    ...


if __name__ == "__main__":
    app()
