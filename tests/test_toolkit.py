"""
Pytest Verification Suite for ATM Toolkit.
Run using: pytest tests/ -v
"""

import pytest
from atm_toolkit import (
    SingleMachineModel,
    MonteCarloSimulator,
    CashReplenishmentOptimizer,
    FleetScalingModel,
    RiskExposureModel,
)


def test_single_machine_model_profitability():
    model = SingleMachineModel(
        surcharge=3.50,
        merchant_split=1.00,
        monthly_tx_volume=200,
    )
    fin = model.calculate_monthly_financials()
    summary = model.get_summary()

    assert fin["gross_revenue"] == 700.00
    assert summary["monthly_net_profit"] > 0
    assert summary["payback_period_months"] < 100


def test_monte_carlo_simulation():
    sim = MonteCarloSimulator(iterations=500, seed=123)
    res = sim.simulate_location("convenience_store")

    assert res["mean_simulated_volume"] > 100
    assert res["p90_net_profit"] > res["p10_net_profit"]
    assert 0.0 <= res["probability_profitable"] <= 1.0


def test_replenishment_optimizer():
    opt = CashReplenishmentOptimizer(daily_dispense_avg=2000.0)
    policy = opt.calculate_policy()

    assert policy["reorder_point_cash"] > 0
    assert policy["economic_order_cash"] > policy["safety_stock_cash"]


def test_fleet_scaling_tiers():
    small_fleet = FleetScalingModel(3).analyze_fleet_structure()
    large_fleet = FleetScalingModel(50).analyze_fleet_structure()

    assert small_fleet["cit_armored_cost_per_unit"] == 0.0
    assert large_fleet["cit_armored_cost_per_unit"] > 0.0


def test_risk_exposure_model():
    risk = RiskExposureModel(fleet_size=5)
    summary = risk.calculate_annualized_loss_expectancy()

    assert summary["total_annualized_risk_loss_expectancy"] > 0
    assert summary["recommended_insurance_buffer_monthly"] > 0
