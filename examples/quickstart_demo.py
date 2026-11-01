"""
Executable Quickstart Demonstration Script.
Run via: python examples/quickstart_demo.py
"""

import os
import sys

# Ensure the repo root (parent of this examples/ dir) is on sys.path so this
# script works when run directly (python examples/quickstart_demo.py), not
# just via `python -m`.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from atm_toolkit import (
    SingleMachineModel,
    MonteCarloSimulator,
    CashReplenishmentOptimizer,
    FleetScalingModel,
    RiskExposureModel,
)


def main():
    print("=" * 65)
    print("  ATM FLEET FINANCIAL MODELING & LOGISTICS TOOLKIT DEMO")
    print("=" * 65)

    # 1. Unit Economics
    print("\n[1] SINGLE MACHINE UNIT ECONOMICS MODEL")
    machine = SingleMachineModel(
        hardware_cost=2434.00,
        installation_cost=300.00,
        working_capital_float=4000.00,
        surcharge=3.50,
        merchant_split=1.00,
        monthly_tx_volume=250,
    )
    summary = machine.get_summary()
    print(f"  • Upfront Capital Needed : ${summary['total_capital_outlay']:,.2f}")
    print(f"  • Monthly Net Income     : ${summary['monthly_net_profit']:,.2f}")
    print(f"  • Annual ROI             : {summary['annual_roi_pct']:.1f}%")
    print(f"  • Payback Period         : {summary['payback_period_months']:.1f} months")
    print(f"  • Breakeven Volume       : {summary['breakeven_monthly_tx']} transactions/mo")

    # 2. Monte Carlo Simulation
    print("\n[2] MONTE CARLO LOCATION YIELD SIMULATION (5,000 Iterations)")
    sim = MonteCarloSimulator(iterations=5000)
    mc_results = sim.simulate_location(location_type="bar_nightclub", surcharge=3.50)
    print(f"  • Archetype              : {mc_results['location_type']}")
    print(f"  • P10 (Downside) Profit  : ${mc_results['p10_net_profit']:,.2f}/mo")
    print(f"  • P50 (Expected) Profit  : ${mc_results['p50_net_profit']:,.2f}/mo")
    print(f"  • P90 (Upside) Profit    : ${mc_results['p90_net_profit']:,.2f}/mo")
    print(f"  • Probability Profitable : {mc_results['probability_profitable']*100:.1f}%")

    # 3. Replenishment Optimization
    print("\n[3] CASH INVENTORY & REPLENISHMENT OPTIMIZATION (EOQ)")
    replenish = CashReplenishmentOptimizer(
        daily_dispense_avg=2500.0,
        daily_dispense_std=500.0,
        refill_trip_cost=75.0,
    )
    plan = replenish.calculate_policy()
    print(f"  • Optimal Vault Load     : ${plan['economic_order_cash']:,.2f}")
    print(f"  • Safety Stock Buffer    : ${plan['safety_stock_cash']:,.2f}")
    print(f"  • Reorder Point Trigger  : ${plan['reorder_point_cash']:,.2f}")
    print(f"  • Refill Cycle Frequency : Every {plan['refill_frequency_days']} days")

    # 4. Fleet Scaling Economics
    print("\n[4] FLEET SCALING OVERHEAD ANALYSIS")
    for size in [3, 15, 60]:
        fleet = FleetScalingModel(fleet_size=size)
        analysis = fleet.analyze_fleet_structure()
        print(f"  • Fleet Size {size:2d} Units -> Tier: {analysis['operational_tier']}")
        print(f"    Total Monthly Fleet Overhead: ${analysis['total_monthly_fleet_overhead']:,.2f}")

    # 5. Risk Analysis
    print("\n[5] OPERATIONAL RISK & ANNUAL LOSS EXPECTANCY (ALE)")
    risk = RiskExposureModel(fleet_size=10)
    risk_summary = risk.calculate_annualized_loss_expectancy()
    print(f"  • Total Fleet Annual Risk Exposure (10 Units) : ${risk_summary['total_annualized_risk_loss_expectancy']:,.2f}")
    print(f"  • Recommended Monthly Risk Provision           : ${risk_summary['recommended_insurance_buffer_monthly']:,.2f}/mo")

    print("\n" + "=" * 65)
    print("  DEMO COMPLETE")
    print("=" * 65)


if __name__ == "__main__":
    main()
