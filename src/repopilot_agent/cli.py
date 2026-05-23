import importlib.metadata
import os
import sys

from google import genai
import typer
from dotenv import load_dotenv
from rich.console import Console
from rich.table import Table

app = typer.Typer(help="RepoPilot local AI agent.")
console = Console()


@app.callback()
def main() -> None:
    """RepoPilot command group."""


def _package_version(package_name: str) -> str:
    try:
        return importlib.metadata.version(package_name)
    except importlib.metadata.PackageNotFoundError:
        return "not installed"


@app.command()
def doctor() -> None:
    """Check the local AI agent development environment."""
    load_dotenv()
    virtualenv = os.environ.get("VIRTUAL_ENV")
    if not virtualenv and sys.prefix != sys.base_prefix:
        virtualenv = sys.prefix

    table = Table(title="RepoPilot Environment")
    table.add_column("Check")
    table.add_column("Value")

    table.add_row("Python", sys.version.split()[0])
    table.add_row("Virtualenv", virtualenv or "not active")
    table.add_row("OPENAI_API_KEY", "set" if os.environ.get(
        "OPENAI_API_KEY") else "missing")
    table.add_row("OPENAI_MODEL", os.environ.get(
        "OPENAI_MODEL", "gpt-4.1-mini"))
    table.add_row("openai", _package_version("openai"))
    table.add_row("pydantic", _package_version("pydantic"))
    table.add_row("typer", _package_version("typer"))

    console.print(table)


@app.command()
def hello() -> None:
    """Print a greeting message."""
    console.print("Hello ")
    api_key = os.environ.get("OPENAI_API_KEY")
    model = os.environ.get("OPENAI_MODEL", "gemini-2.5-flash")
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model=model,
        contents="什么是git"
    )

    console.print(response.text)


if __name__ == "__main__":
    app()
