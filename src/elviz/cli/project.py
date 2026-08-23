from enum import Enum

import typer
from rich.console import Console

app = typer.Typer()
console = Console()


class exportFormat(Enum):
    """Enum of export formats"""

    PDF = "pdf"
    DXF = "dxf"
    SVG = "svg"


@app.command()
def export(format: exportFormat, path: str) -> None:
    """Export to PDF, DXF or SVG"""
    ...


@app.command()
def save_as_template() -> None:
    """Save this project as a template"""
    ...


@app.command()
def render() -> None:
    """Render the project"""
    ...


@app.command()
def view() -> None:
    """Preview the project"""
    ...


if __name__ == "__main__":
    app()
