"""
Streamlit Web Dashboard for ATM Fleet Financial Modeling & Logistics Toolkit.
Launch via: streamlit run dashboard.py
"""

import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from atm_toolkit import (
    SingleMachineModel,
    MonteCarloSimulator,
    CashReplenishmentOptimizer,
    FleetScalingModel,
    RiskExposureModel,
)

st.set_page_config(
    page_title="ATM Fleet Financial Modeling Toolkit",
    page_icon="💵",
    layout="wide",
)

st.title("💵 ATM Fleet Financial Modeling & Cash Logistics Toolkit")
st.markdown("*Based on industry mechanics & research from Ned Talks Business / Mr. Finance Extra*")

st.markdown("""
> **Disclaimer & Purpose:** Independent educational, simulation, and analytical modeling project. Non-commercial, non-monetized, with no official affiliation or endorsement.
""")

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Unit Economics",
    "🎲 Monte Carlo Simulation",
    "🚚 Cash Replenishment (EOQ)",
    "📈 Fleet Scaling Economics",
    "⚠️ Operational Risk (ALE)",
])

# TAB 1: Unit Economics
with tab1:
    st.header("Single Terminal Unit Economics")
    col1, col2 = st.columns([1, 2])

    with col1:
        st.subheader("Terminal Parameters")
        hw_cost = st.number_input("Hardware Cost ($)", value=2434.0, step=100.0)
        install_cost = st.number_input("Installation Cost ($)", value=300.0, step=50.0)
        cash_float = st.number_input("Cash Working Capital Float ($)", value=4000.0, step=500.0)
        surcharge = st.number_input("Surcharge Fee ($)", value=3.50, step=0.25)
        merchant_split = st.number_input("Merchant Split ($)", value=1.00, step=0.25)
        monthly_tx = st.slider("Monthly Transactions", 20, 600, 250)

    with col2:
        model = SingleMachineModel(
            hardware_cost=hw_cost,
            installation_cost=install_cost,
            working_capital_float=cash_float,
            surcharge=surcharge,
            merchant_split=merchant_split,
            monthly_tx_volume=monthly_tx,
        )
        summary = model.get_summary()

        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Total Capital Outlay", f"${summary['total_capital_outlay']:,.2f}")
        m2.metric("Monthly Net Profit", f"${summary['monthly_net_profit']:,.2f}")
        m3.metric("Annual ROI", f"{summary['annual_roi_pct']:.1f}%")
        m4.metric("Payback Horizon", f"{summary['payback_period_months']:.1f} mos")

        # Waterfall Chart
        fin = model.calculate_monthly_financials()
        fig = go.Figure(go.Waterfall(
            name="Monthly WaterFall",
            orientation="v",
            measure=["relative", "relative", "relative", "relative", "total"],
            x=["Gross Revenue", "Merchant Cut", "ISO/Network Fees", "Fixed Operating Costs", "Net Profit"],
            textposition="outside",
            text=[f"${fin['gross_revenue']:.2f}", f"-${merchant_split*monthly_tx:.2f}", f"-${0.155*monthly_tx:.2f}", f"-${fin['fixed_costs']:.2f}", f"${fin['net_monthly_profit']:.2f}"],
            y=[fin['gross_revenue'], -merchant_split*monthly_tx, -0.155*monthly_tx, -fin['fixed_costs'], fin['net_monthly_profit']],
            connector={"line": {"color": "rgb(63, 63, 63)"}},
        ))
        fig.update_layout(title="Monthly Cash Flow Breakdown", showlegend=False)
        st.plotly_chart(fig, use_container_width=True)

# TAB 2: Monte Carlo
with tab2:
    st.header("Monte Carlo Location Yield Simulation")
    loc_type = st.selectbox("Location Archetype", ["quiet_retail", "convenience_store", "bar_nightclub", "high_volume_venue"], index=2)
    sim_surcharge = st.slider("Surcharge Rate ($)", 2.0, 6.0, 3.5, 0.25, key="mc_surcharge")

    sim = MonteCarloSimulator(iterations=3000)
    res = sim.simulate_location(location_type=loc_type, surcharge=sim_surcharge)

    mc1, mc2, mc3 = st.columns(3)
    mc1.metric("P10 Downside Monthly Profit", f"${res['p10_net_profit']:,.2f}")
    mc2.metric("P50 Expected Monthly Profit", f"${res['p50_net_profit']:,.2f}")
    mc3.metric("P90 Upside Monthly Profit", f"${res['p90_net_profit']:,.2f}")

    fig_hist = px.histogram(
        res["simulated_profits"],
        nbins=50,
        title=f"Simulated Monthly Net Profit Distribution ({loc_type.replace('_', ' ').title()})",
        labels={"value": "Monthly Net Profit ($)"},
        color_discrete_sequence=["#2E7D32"],
    )
    st.plotly_chart(fig_hist, use_container_width=True)

# TAB 3: Replenishment
with tab3:
    st.header("Cash Inventory & Replenishment (EOQ Model)")
    col_r1, col_r2 = st.columns(2)
    with col_r1:
        daily_avg = st.number_input("Average Daily Cash Dispensed ($)", value=2500.0, step=250.0)
        daily_std = st.number_input("Daily Cash Dispense StdDev ($)", value=500.0, step=50.0)
        trip_cost = st.number_input("Refill Trip Operational Cost ($)", value=75.0, step=5.0)

    optimizer = CashReplenishmentOptimizer(
        daily_dispense_avg=daily_avg,
        daily_dispense_std=daily_std,
        refill_trip_cost=trip_cost,
    )
    plan = optimizer.calculate_policy()

    with col_r2:
        st.subheader("Optimal Replenishment Policy")
        st.write(f"• **Recommended Vault Load Capacity:** ${plan['recommended_max_vault_load']:,.2f}")
        st.write(f"• **Economic Order Quantity (EOQ):** ${plan['economic_order_cash']:,.2f}")
        st.write(f"• **Reorder Point Trigger:** ${plan['reorder_point_cash']:,.2f}")
        st.write(f"• **Safety Stock Buffer:** ${plan['safety_stock_cash']:,.2f}")
        st.write(f"• **Optimal Refill Cycle:** Every **{plan['refill_frequency_days']}** days")

# TAB 4: Fleet Scaling
with tab4:
    st.header("Fleet Scaling & Overhead Economics")
    fleet_size = st.slider("Total Terminal Fleet Size", 1, 100, 15)

    fleet_model = FleetScalingModel(fleet_size=fleet_size)
    fleet_info = fleet_model.analyze_fleet_structure()

    st.subheader(f"Operational Tier: {fleet_info['operational_tier']}")
    st.info(fleet_info["description"])

    sizes = list(range(1, 101))
    overheads = [FleetScalingModel(s).analyze_fleet_structure()["total_monthly_fleet_overhead"] for s in sizes]

    fig_fleet = px.line(
        x=sizes,
        y=overheads,
        title="Monthly Fleet Overhead Scaling ($)",
        labels={"x": "Fleet Size (Units)", "y": "Total Overhead ($)"},
    )
    st.plotly_chart(fig_fleet, use_container_width=True)

# TAB 5: Risk Analysis
with tab5:
    st.header("Operational Risk & Annual Loss Expectancy (ALE)")
    risk_fleet = st.slider("Fleet Units Exposed", 1, 50, 10, key="risk_fleet")
    risk_model = RiskExposureModel(fleet_size=risk_fleet)
    risk_res = risk_model.calculate_annualized_loss_expectancy()

    r1, r2, r3 = st.columns(3)
    r1.metric("Single Ram Raid Theft Exposure", f"${risk_res['single_ram_raid_loss_exposure']:,.2f}")
    r2.metric("Annualized Loss Expectancy (ALE)", f"${risk_res['total_annualized_risk_loss_expectancy']:,.2f}")
    r3.metric("Recommended Monthly Risk Provision", f"${risk_res['recommended_insurance_buffer_monthly']:,.2f}")
