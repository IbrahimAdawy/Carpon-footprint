class ReportGenerator:
    def __init__(self, carbon_footprint):
        self.carbon_footprint = carbon_footprint

    def generate(self):
        print("\n--- Carbon Footprint Report ---")
        print(f"Total Carbon Footprint: {self.carbon_footprint:.2f} kg CO2\n")
        print("Suggestions for Reduction:")
        print("- Consider using energy-efficient appliances to save on energy.")
        print("- Try carpooling or public transport to reduce travel emissions.")
        print("- Explore renewable energy options for your home.")