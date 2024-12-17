class CarbonCalculator:
    def __init__(self, electricity_bill, gas_bill, fuel_bill, waste_generated, recycling_percentage, kilometers_traveled, fuel_efficiency):
        self.electricity_bill = electricity_bill
        self.gas_bill = gas_bill
        self.fuel_bill = fuel_bill
        self.waste_generated = waste_generated
        self.recycling_percentage = recycling_percentage
        self.kilometers_traveled = kilometers_traveled
        self.fuel_efficiency = fuel_efficiency

    def calculate_energy_usage(self):
        # Calculate CO2 emissions from energy usage
        electricity_emissions = (self.electricity_bill * 12 * 0.0005)
        gas_emissions = (self.gas_bill * 12 * 0.0053)
        fuel_emissions = (self.fuel_bill * 12 * 2.32)
        return electricity_emissions + gas_emissions + fuel_emissions

    def calculate_waste(self):
        # Calculate CO2 emissions from waste
        waste_emissions = (self.waste_generated * 12 * (0.57 - self.recycling_percentage))
        return waste_emissions

    def calculate_business_travel(self):
        # Calculate CO2 emissions from business travel
        travel_emissions = (self.kilometers_traveled * (1 / self.fuel_efficiency) * 2.31)
        return travel_emissions

    def calculate_total_emissions(self):
        # Sum all emissions
        total_emissions = (
            self.calculate_energy_usage() +
            self.calculate_waste() +
            self.calculate_business_travel()
        )
        return total_emissions