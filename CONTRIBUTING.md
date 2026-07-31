# Contributing to atm-fleet-toolkit

Thanks for your interest in improving this project. This is a personal,
non-commercial simulation/modeling toolkit, but it follows normal open-source
contribution conventions.

## Branch strategy

- **`develop`** is the default branch and the integration branch for all work.
  Open PRs against `develop`, not `main`.
- **`main`** tracks the latest released/stable state and is updated from
  `develop` via a release PR/merge.
- Feature and fix branches should be cut from `develop` and named
  descriptively, e.g.:
  - `feature/risk-analysis-jackpotting-model`
  - `fix/replenishment-eoq-rounding`
  - `docs/update-readme-examples`

## Getting set up

```bash
git clone https://github.com/sjamal/atm-fleet-toolkit.git
cd atm-fleet-toolkit
git checkout develop

python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt

cp .env.example .env         # no secrets required today, but keep the convention
```

## Running tests

```bash
pytest tests/ -v
```

All new behavior should come with test coverage. CI (`.github/workflows/ci.yml`)
runs the test suite on every push/PR to `develop` and `main`.

## Running the dashboard

```bash
streamlit run dashboard.py
```

## Code style

- Keep modules focused: one economics/domain concept per file, matching the
  existing `atm_toolkit/` layout (`unit_economics`, `forecasting`,
  `replenishment`, `fleet_scaling`, `risk_analysis`).
- Prefer `dataclasses` for config objects, consistent with the existing code.
- Format with `black`-compatible style (88-char line length, per `.vscode/settings.json`).

## Documenting decisions

Non-trivial architectural or structural changes should get an ADR in
`docs/adr/` (see `docs/adr/template.md`). Small bug fixes and doc tweaks don't
need one.

## Pull requests

1. Branch from `develop`.
2. Make your change with tests.
3. Ensure `pytest tests/ -v` passes locally.
4. Open a PR against `develop` using the PR template — fill out the checklist.
5. Squash-merge once approved.

## Data & privacy

This project is a synthetic/educational simulation. Please don't add real
personal data, credentials, API keys, or proprietary business data in code,
tests, sample data, or commit history. Use `.env` (git-ignored) for any local
config, never `.env.example` or tracked files.
