# CI-Test

![CI](https://github.com/OWNER/CI-Test/actions/workflows/ci.yml/badge.svg)

A tiny Python package (`citest`: mean / median / rms plus a `citest` command) used to try out
GitHub Actions.

## Layout

| Path | Purpose |
|---|---|
| `src/citest/` | the package |
| `tests/` | pytest tests |
| `pyproject.toml` | package metadata, pytest and ruff settings |
| `.github/workflows/ci.yml` | lint, then tests on Python 3.10–3.13 (Linux) and 3.12 (Windows) |
| `.github/workflows/release.yml` | on a `v*` tag: build, then publish a GitHub Release |
| `.github/dependabot.yml` | weekly PRs that bump the versions of the actions |

## Run the same checks locally

```sh
python3 -m venv .venv && . .venv/bin/activate
pip install -e ".[dev]"
ruff check . && ruff format --check .
pytest --cov=citest
citest 1 2 3
```

Replace `OWNER` in the badge URL above with your GitHub user name.
