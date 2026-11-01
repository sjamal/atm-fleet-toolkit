---
name: project-context
description: Domain model and conventions for atm-fleet-toolkit. Read this before making non-trivial changes to atm_toolkit/ modules, dashboard.py, or tests.
---

# atm-fleet-toolkit — project context

## What this project models

Independent ATM (IAD/ISO) operations: per-machine unit economics, Monte
Carlo transaction forecasting, EOQ-based cash replenishment/routing, fleet
scaling economics, and risk/loss modeling (de-risking, ram-raids, cash
trapping, jackpotting).

Content is synthetic/educational, formalizing concepts from a public YouTube
finance series (see README "Primary Media Source"). No real business,
banking, or location data.

## Domain modules (`atm_toolkit/`)

- `unit_economics.py` — `SingleMachineModel`: surcharge revenue, interchange/
  ISO splits, cash float opportunity cost, payback/ROI for one machine.
- `forecasting.py` — `MonteCarloSimulator`: probabilistic transaction volume
  and yield simulation across many trials.
- `replenishment.py` — `CashReplenishmentOptimizer`: EOQ-style cash inventory
  and route replenishment optimization to minimize cash-out risk.
- `fleet_scaling.py` — `FleetScalingModel`: overhead and CIT (cash-in-transit)
  logistics economics as fleet size grows (solo → software-monitored →
  enterprise armored-carrier tiers).
- `risk_analysis.py` — `RiskExposureModel`: quantitative loss expectancy for
  de-risking, physical crime, and cyberattack scenarios.

All five are re-exported from `atm_toolkit/__init__.py`.

## Conventions

- Config/model classes are `@dataclass` where practical, with sensible
  defaults, matching the pattern used in `vending-route-ops` and
  `ecommerce-funnel-ops` (this repo predates and inspired those two).
- Tests live in `tests/test_toolkit.py`.
- `dashboard.py` is the Streamlit entry point — sidebar sliders feed the
  `atm_toolkit` engines, outputs shown as `st.metric` + Plotly charts.
- License is MIT — copyright line uses the generic "ATM Fleet Toolkit
  Contributors" placeholder (updated from a personal name during this
  scaffolding pass, for consistency with the sibling repos).

## Running things

```bash
pip install -r requirements.txt
pytest tests/ -v
streamlit run dashboard.py
python examples/quickstart_demo.py
```
