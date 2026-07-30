"""
Unit Economics Engine for Single ATM Terminals.
Models CAPEX, OPEX, Cash Float, Surcharge Revenue, and Payback Horizons.
"""

import numpy as np


class SingleMachineModel:
    def __init__(
        self,
        hardware_cost: float = 2434.00,
        installation_cost: float = 300.00,
        initial_setup_fees: float = 200.00,
        working_capital_float: float = 4000.00,
        surcharge: float = 3.22,
        merchant_split: float = 1.00,
        iso_processing_fee: float = 0.15,
        network_switch_fee: float = 0.005,
        monthly_wireless_fee: float = 20.00,
        monthly_receipt_paper: float = 5.00,
        monthly_maintenance_reserve: float = 25.00,
        monthly_tx_volume: int = 160,
        cost_of_capital_apr: float = 0.06,
    ):
        self.hardware_cost = hardware_cost
        self.installation_cost = installation_cost
        self.initial_setup_fees = initial_setup_fees
        self.working_capital_float = working_capital_float

        self.surcharge = surcharge
        self.merchant_split = merchant_split
        self.iso_processing_fee = iso_processing_fee
        self.network_switch_fee = network_switch_fee

        self.monthly_wireless_fee = monthly_wireless_fee
        self.monthly_receipt_paper = monthly_receipt_paper
        self.monthly_maintenance_reserve = monthly_maintenance_reserve

        self.monthly_tx_volume = monthly_tx_volume
        self.cost_of_capital_apr = cost_of_capital_apr

    @property
    def initial_upfront_capex(self) -> float:
        return self.hardware_cost + self.installation_cost + self.initial_setup_fees

    @property
    def total_initial_capital_outlay(self) -> float:
        return self.initial_upfront_capex + self.working_capital_float

    @property
    def net_fee_per_transaction(self) -> float:
        return (
            self.surcharge
            - self.merchant_split
            - self.iso_processing_fee
            - self.network_switch_fee
        )

    def calculate_monthly_financials(self) -> dict:
        gross_surcharge_revenue = self.surcharge * self.monthly_tx_volume
        merchant_payout = self.merchant_split * self.monthly_tx_volume
        iso_network_fees = (self.iso_processing_fee + self.network_switch_fee) * self.monthly_tx_volume

        total_variable_costs = merchant_payout + iso_network_fees
        fixed_monthly_costs = (
            self.monthly_wireless_fee
            + self.monthly_receipt_paper
            + self.monthly_maintenance_reserve
        )

        monthly_float_cost = (self.working_capital_float * self.cost_of_capital_apr) / 12.0
        net_monthly_profit = gross_surcharge_revenue - total_variable_costs - fixed_monthly_costs - monthly_float_cost

        return {
            "gross_revenue": gross_surcharge_revenue,
            "variable_costs": total_variable_costs,
            "fixed_costs": fixed_monthly_costs,
            "float_opportunity_cost": monthly_float_cost,
            "net_monthly_profit": net_monthly_profit,
            "net_margin_pct": (net_monthly_profit / gross_surcharge_revenue * 100) if gross_surcharge_revenue > 0 else 0.0,
        }

    def get_summary(self) -> dict:
        fin = self.calculate_monthly_financials()
        net_monthly = fin["net_monthly_profit"]

        if net_monthly <= 0:
            payback_months = float("inf")
        else:
            payback_months = self.total_initial_capital_outlay / net_monthly

        annual_net_profit = net_monthly * 12.0
        annual_roi_pct = (annual_net_profit / self.total_initial_capital_outlay) * 100.0

        fixed_plus_float = fin["fixed_costs"] + fin["float_opportunity_cost"]
        net_per_tx = self.net_fee_per_transaction
        breakeven_tx_volume = fixed_plus_float / net_per_tx if net_per_tx > 0 else float("inf")

        return {
            "initial_capex": self.initial_upfront_capex,
            "working_capital_float": self.working_capital_float,
            "total_capital_outlay": self.total_initial_capital_outlay,
            "monthly_net_profit": net_monthly,
            "annual_net_profit": annual_net_profit,
            "payback_period_months": payback_months,
            "annual_roi_pct": annual_roi_pct,
            "breakeven_monthly_tx": int(np.ceil(breakeven_tx_volume)),
        }
