"""Console script for elviz."""

import typer
from rich.console import Console

from .circuit import app as circuit
from .pages import app as pages
from .project import app as project

app = typer.Typer()
app.add_typer(typer_instance=project, name="project", help="Manage the project")
app.add_typer(typer_instance=circuit, name="circuit", help="Manage the circuit")
app.add_typer(typer_instance=pages, name="pages", help="Manage the pages")
console = Console()


@app.command()
def new() -> None:
    """Init new project"""
    ...


@app.command()
def list_templates() -> None:
    """List available templates"""
    ...


if __name__ == "__main__":
    app()
