import typer
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def show() -> None:
    """Show the circuit"""
    ...


@app.command()
def simulate() -> None:
    """Simulate the circuit"""
    ...


@app.command()
def list_connections() -> None:
    """List the connections in the circuit"""
    ...


@app.command()
def list_devices() -> None:
    """List the devices in the circuit"""
    ...


if __name__ == "__main__":
    app()
