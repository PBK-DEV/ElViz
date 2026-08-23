import os

import typer
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def view() -> None:
    """Show page"""
    ...


@app.command()
def add_external() -> None:
    """Add external page"""
    ...


@app.command()
def lint() -> None:
    """Lint the pages dir: rename the page files after their id and order them by adding numerals"""
    ...


@app.command()
def list() -> None:
    """List all pages in the project"""
    path: str = os.path.join(os.getcwd(), "pages")
    for x in os.listdir(path=path):
        if x.endswith(".py"):
            console.print(x)


if __name__ == "__main__":
    app()
