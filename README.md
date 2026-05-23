# RepoPilot

Local Python workspace for AI agent development.

## Setup

Install `uv` if it is not already available:

```bash
python3 -m pip install uv
```

Create and sync the local environment:

```bash
uv sync --dev
```

Configure local secrets:

```bash
cp .env.example .env
```

Then edit `.env` and set `OPENAI_API_KEY`.

## Verify

```bash
repopilot doctor
```

## Development

Common commands:

```bash
uv run ruff check .
uv run pytest
```

Project code lives under `src/repopilot_agent`.

## Dependencies

Add runtime dependencies with:

```bash
uv add package-name
```

Add development-only dependencies with:

```bash
uv add --dev package-name
```
