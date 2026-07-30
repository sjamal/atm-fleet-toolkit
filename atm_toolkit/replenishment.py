"""
Cash Replenishment & Inventory Optimization Module.
"""

import numpy as np


class CashReplenishmentOptimizer:
    def __init__(
        self,
        daily_dispense_avg: float = 2500.0,
        daily_dispense_std: float = 500.0,
        refill_trip_cost: float = 80.0,
        vault_cash_apr: float = 0.08,
        lead_time_days: int = 1,
        service_level_z: float = 2.33,
    ):
        self.daily_dispense_avg = daily_dispense_avg
        self.daily_dispense_std = daily_dispense_std
        self.refill_trip_cost = refill_trip_cost
        self.vault_cash_apr = vault_cash_apr
        self.lead_time_days = lead_time_days
        self.service_level_z = service_level_z

    def calculate_policy(self) -> dict:
        annual_dispense = self.daily_dispense_avg * 365.0

        eoq_cash = np.sqrt(
            (2.0 * annual_dispense * self.refill_trip_cost) / self.vault_cash_apr
        )

        safety_stock = (
            self.service_level_z
            * np.sqrt(self.lead_time_days)
            * self.daily_dispense_std
        )

        reorder_point = (self.daily_dispense_avg * self.lead_time_days) + safety_stock
        recommended_max_cash = eoq_cash + safety_stock
        refill_frequency_days = eoq_cash / self.daily_dispense_avg if self.daily_dispense_avg > 0 else 0

        return {
            "daily_avg_dispense": self.daily_dispense_avg,
            "safety_stock_cash": float(np.round(safety_stock, -1)),
            "reorder_point_cash": float(np.round(reorder_point, -1)),
            "economic_order_cash": float(np.round(eoq_cash, -1)),
            "recommended_max_vault_load": float(np.round(recommended_max_cash, -1)),
            "refill_frequency_days": float(np.round(refill_frequency_days, 1)),
        }
