"""
Monte Carlo Simulation Engine for Location Performance and Transaction Volatility.
"""

import numpy as np


class MonteCarloSimulator:
    LOCATION_ARCHETYPES = {
        "quiet_retail": (50, 15),
        "convenience_store": (160, 35),
        "bar_nightclub": (300, 75),
        "high_volume_venue": (550, 120),
    }

    def __init__(self, iterations: int = 5000, seed: int = 42):
        self.iterations = iterations
        self.seed = seed
        np.random.seed(self.seed)

    def simulate_location(
        self,
        location_type: str = "bar_nightclub",
        surcharge: float = 3.50,
        merchant_split: float = 1.00,
        fixed_monthly_costs: float = 45.0,
        initial_outlay: float = 7000.0,
    ) -> dict:
        if location_type not in self.LOCATION_ARCHETYPES:
            raise ValueError(f"Unknown location_type. Choose from {list(self.LOCATION_ARCHETYPES.keys())}")

        mean_tx, std_tx = self.LOCATION_ARCHETYPES[location_type]
        simulated_volumes = np.maximum(0, np.random.normal(mean_tx, std_tx, self.iterations))

        net_per_tx = surcharge - merchant_split - 0.155
        simulated_gross_profit = simulated_volumes * net_per_tx
        simulated_net_profit = simulated_gross_profit - fixed_monthly_costs

        p10 = np.percentile(simulated_net_profit, 10)
        p50 = np.percentile(simulated_net_profit, 50)
        p90 = np.percentile(simulated_net_profit, 90)

        prob_profitable = np.mean(simulated_net_profit > 0)
        payback_months = np.where(
            simulated_net_profit > 0,
            initial_outlay / np.maximum(1.0, simulated_net_profit),
            999.0
        )

        return {
            "location_type": location_type,
            "mean_simulated_volume": float(np.mean(simulated_volumes)),
            "p10_net_profit": float(p10),
            "p50_net_profit": float(p50),
            "p90_net_profit": float(p90),
            "probability_profitable": float(prob_profitable),
            "median_payback_months": float(np.median(payback_months)),
            "simulated_profits": simulated_net_profit,
        }
