# Quality, Testing, and Security

Career Bridge AI uses a requirements-based Python workflow.

## Install Development Tooling

```bash
pip install -r requirements.txt -r requirements-dev.txt
```

## Local Linting and Formatting

```bash
ruff check .
ruff format --check .
mypy
flake8 .
pylint --fail-under=0 app.py career_engine.py config.py database.py opportunity_engine.py resume_parser.py roadmap_engine.py scheme_engine.py scholarship_engine.py
vulture .
semgrep --config .semgrep.yml --error
```

`pyupgrade` is configured through pre-commit and GitLab CI:

```bash
pyupgrade --py39-plus app.py career_engine.py config.py database.py opportunity_engine.py resume_parser.py roadmap_engine.py scheme_engine.py scholarship_engine.py
```

## Testing and Coverage

```bash
pytest
coverage report --fail-under=1
```

Coverage settings live in `pyproject.toml` and `setup.cfg`. The current fail-under threshold is 1% while the first test suite is established; raise it as coverage grows.

## Security Scanning

```bash
bandit -c pyproject.toml -r .
pip-audit -r requirements.txt -r requirements-dev.txt --ignore-vuln GHSA-rrmf-rvhw-rf47 --ignore-vuln PYSEC-2025-217 --ignore-vuln GHSA-69w3-r845-3855
gitleaks detect --source . --config .gitleaks.toml --verbose
```

The audit exceptions cover currently unresolved or incompatible transitive ML advisories from `torch` and `transformers` pulled by `sentence-transformers==2.2.2`. Revisit them when a compatible `sentence-transformers` upgrade is planned.

Semgrep uses the repository-local `.semgrep.yml` policy:

```bash
semgrep --config .semgrep.yml --error
```

## Pre-Commit

Install hooks once per clone:

```bash
pre-commit install
```

Run all hooks manually:

```bash
pre-commit run --all-files
```

## CI/CD

GitLab CI runs Ruff, Mypy, Flake8, Pylint, Vulture, Pyupgrade, Bandit, Semgrep, pip-audit, Gitleaks, pytest, and coverage. The pipeline is defined in `.gitlab-ci.yml`.

## Changelog

Git-Cliff is configured in `cliff.toml`.

```bash
git-cliff --unreleased --strip header
```
