"""
Operational Risk & Annualized Loss Expectancy (ALE) Estimator.
"""


class RiskExposureModel:
    def __init__(
        self,
        fleet_size: int = 1,
        average_cash_per_machine: float = 4000.0,
        machine_hardware_value: float = 2400.0,
    ):
        self.fleet_size = fleet_size
        self.average_cash_per_machine = average_cash_per_machine
        self.machine_hardware_value = machine_hardware_value

    def calculate_annualized_loss_expectancy(
        self,
        annual_ram_raid_prob: float = 0.02,
        annual_derisking_prob: float = 0.08,
        derisking_downtime_days: int = 14,
        avg_daily_profit_per_machine: float = 15.0,
    ) -> dict:
        single_theft_loss = self.average_cash_per_machine + self.machine_hardware_value
        ale_physical_theft = self.fleet_size * (single_theft_loss * annual_ram_raid_prob)

        single_derisking_loss = (
            self.fleet_size * avg_daily_profit_per_machine * derisking_downtime_days
        )
        ale_derisking = single_derisking_loss * annual_derisking_prob
        total_ale = ale_physical_theft + ale_derisking

        return {
            "fleet_size": self.fleet_size,
            "single_ram_raid_loss_exposure": single_theft_loss,
            "annualized_theft_loss_expectancy": ale_physical_theft,
            "annualized_derisking_loss_expectancy": ale_derisking,
            "total_annualized_risk_loss_expectancy": total_ale,
            "recommended_insurance_buffer_monthly": total_ale / 12.0,
        }
