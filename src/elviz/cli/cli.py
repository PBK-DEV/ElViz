"""Console script for elviz."""

from enum import Enum
from pathlib import Path

import typer
from rich.console import Console

from .circuit import app as circuit
from .pages import app as pages
from .project import app as project

app = typer.Typer()
app.add_typer(typer_instance=project, name="project")
app.add_typer(typer_instance=circuit, name="circuit")
app.add_typer(typer_instance=pages, name="pages")
console = Console()


class exportFormat(Enum):
    """Enum of export formats"""

    PDF = "pdf"
    DXF = "dxf"
    SVG = "svg"


@app.command()
def export(format: exportFormat, path: Path) -> None:
    """Export to PDF, DXF or SVG"""
    ...


if __name__ == "__main__":
    app()
