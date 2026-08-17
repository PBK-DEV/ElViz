import typer
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def show() -> None:
    """Show page"""
    ...


@app.command()
def add_external() -> None:
    """Add external page"""
    ...


@app.command()
def list() -> None:
    """List all pages in the project"""
    ...


if __name__ == "__main__":
    app()
