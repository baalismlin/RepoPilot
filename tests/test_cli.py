from typer.testing import CliRunner

from repopilot_agent.cli import app


def test_doctor_command_runs() -> None:
    runner = CliRunner()

    result = runner.invoke(app, ["doctor"])

    assert result.exit_code == 0
    assert "RepoPilot Environment" in result.output
