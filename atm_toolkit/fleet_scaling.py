"""
Fleet Scaling Economics & Overhead Model.
"""


class FleetScalingModel:
    def __init__(self, fleet_size: int):
        self.fleet_size = fleet_size

    def analyze_fleet_structure(self) -> dict:
        if self.fleet_size <= 5:
            tier = "Solo Operator (Low Overhead)"
            software_cost_per_unit = 0.0
            cit_cost_per_unit = 0.0
            labor_overhead_per_unit = 0.0
            description = "Owner handles cash replenishment, maintenance, and phone calls directly."

        elif self.fleet_size <= 25:
            tier = "Regional Route (Semi-Automated)"
            software_cost_per_unit = 15.0
            cit_cost_per_unit = 0.0
            labor_overhead_per_unit = 50.0
            description = "Requires automated real-time cash tracking software & scheduled weekly route driving."

        else:
            tier = "Enterprise Fleet (Armored Service & Vault Financing)"
            software_cost_per_unit = 25.0
            cit_cost_per_unit = 175.0
            labor_overhead_per_unit = 120.0
            description = "Armored carriers handle transit; capital provided via bank vault cash financing."

        monthly_fixed_overhead_per_unit = (
            software_cost_per_unit + cit_cost_per_unit + labor_overhead_per_unit
        )
        total_monthly_fleet_overhead = monthly_fixed_overhead_per_unit * self.fleet_size

        return {
            "fleet_size": self.fleet_size,
            "operational_tier": tier,
            "software_cost_per_unit": software_cost_per_unit,
            "cit_armored_cost_per_unit": cit_cost_per_unit,
            "labor_overhead_per_unit": labor_overhead_per_unit,
            "total_monthly_fleet_overhead": total_monthly_fleet_overhead,
            "description": description,
        }
